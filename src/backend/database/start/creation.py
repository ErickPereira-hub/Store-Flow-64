from src.backend.database.infra.cnx import Cnx
from mysql.connector.abstracts import MySQLConnectionAbstract
from typing import Any
import os
import asyncio

class GenerateDatabase:
    
    async def gen_all(self) -> None:
        self.__cnx_instance: Cnx = Cnx()
        self.__wcnx: MySQLConnectionAbstract = await self.__cnx_instance.get_wcnx()
        self.__cursor: Any = await self.__wcnx.cursor()
        await self.__gen_db(self.__cursor) #<--- Generating the database if it doesn't exist yet
        await self.__cursor.close()
        await self.__wcnx.close()
        self.__cnx: MySQLConnectionAbstract = await self.__cnx_instance.get_cnx()
        self.__cursor: Any = await self.__cnx.cursor()
        #Creating the tables if they do not exist
        await self.__gen_address(self.__cursor)
        await self.__gen_user(self.__cursor)
        await self.__gen_store(self.__cursor)
        await self.__gen_employee(self.__cursor)
        await self.__gen_supplier(self.__cursor)
        await self.__gen_category(self.__cursor)
        await self.__gen_product(self.__cursor)
        await self.__gen_customer(self.__cursor)
        await self.__gen_order(self.__cursor)
        await self.__cursor.close()
        await self.__cnx.close()
    
    async def __gen_db(self, cursor: Any) -> None:
        await cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")

    async def __gen_address(self, cursor: Any) -> None:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS address (
                id INT PRIMARY KEY AUTO_INCREMENT,
                country VARCHAR(50) NOT NULL,
                province VARCHAR(50) NOT NULL,
                city VARCHAR(50) NOT NULL
            )
        """)
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS address_details (
                id INT PRIMARY KEY AUTO_INCREMENT,
                neighborhood VARCHAR(100) NOT NULL,
                house_number VARCHAR(10) NOT NULL,
                complement VARCHAR(200) NOT NULL,
                address_id INT NOT NULL,
                FOREIGN KEY (address_id) REFERENCES address(id)
            )
        """)

    async def __gen_user(self, cursor) -> None:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                uid INT PRIMARY KEY AUTO_INCREMENT,
                password VARCHAR(500) NOT NULL,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                phone VARCHAR(30) NOT NULL,
                sex ENUM("M", "F", "U") NOT NULL,
                vip ENUM("A", "B", "C", "D") NOT NULL,
                address_id INT NOT NULL,
                FOREIGN KEY (address_id) REFERENCES address(id),
                CONSTRAINT unique_uemail UNIQUE(email),
                CONSTRAINT email_format CHECK(email LIKE "%_@_%.com")
            )
        """)

    async def __gen_store(self, cursor: Any) -> None:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS store (
                store_id INT PRIMARY KEY AUTO_INCREMENT,
                company_name VARCHAR(50) NOT NULL,
                registration_date DATETIME NOT NULL,
                uid INT NOT NULL,
                FOREIGN KEY (uid) REFERENCES user(uid)
            )
        """)

    async def __gen_employee(self, cursor: Any) -> None:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                employee_id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                phone VARCHAR(30) NOT NULL,
                hire_date DATE NOT NULL,
                sex ENUM("M", "F", "U") NOT NULL,
                address_id INT NOT NULL,
                store_id INT NOT NULL,
                FOREIGN KEY (address_id) REFERENCES address(id),
                FOREIGN KEY (store_id) REFERENCES store (store_id)
            )
        """)

    async def __gen_supplier(self, cursor: Any) -> None:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS supplier (
                supplier_id INT PRIMARY KEY AUTO_INCREMENT,
                supplier_name VARCHAR(50) NOT NULL,
                supplier_desc VARCHAR(2000) NOT NULL,
                store_id INT NOT NULL,
                address_id INT NOT NULL,
                FOREIGN KEY (store_id) REFERENCES store(store_id),
                FOREIGN KEY (address_id) REFERENCES address(id)
            )
        """)

    async def __gen_category(self, cursor: Any) -> None:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS category (
                category_id INT PRIMARY KEY AUTO_INCREMENT,
                category_name VARCHAR(50) NOT NULL,
                description VARCHAR(255) NOT NULL,
                store_id INT NOT NULL,
                FOREIGN KEY (store_id) REFERENCES store(store_id)
            )
        """)

    async def __gen_product(self, cursor: Any) -> None:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS product (
                product_id INT PRIMARY KEY AUTO_INCREMENT,
                product_name VARCHAR(50) NOT NULL,
                description VARCHAR(255) NOT NULL,
                price DECIMAL(8, 2) NOT NULL,
                stock_units INT NOT NULL,
                supplier_id INT,
                store_id INT NOT NULL,
                category_id INT NOT NULL,
                FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id),
                FOREIGN KEY (store_id) REFERENCES store(store_id),
                FOREIGN KEY (category_id) REFERENCES category(category_id)
            )
        """)

    async def __gen_customer(self, cursor: Any) -> None:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                phone VARCHAR(30) NOT NULL,
                sex ENUM("M", "F", "U") NOT NULL,
                email VARCHAR(100) NOT NULL,
                address_id INT NOT NULL,
                store_id INT NOT NULL,
                CONSTRAINT unique_cemail CHECK(email LIKE "%_@_%.com"),
                FOREIGN KEY (address_id) REFERENCES address(id),
                FOREIGN KEY (store_id) REFERENCES store(store_id)
            )
        """)

    async def __gen_order(self, cursor: Any) -> None:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_unit (
                order_id INT PRIMARY KEY AUTO_INCREMENT,
                purchase_date DATETIME NOT NULL,
                online_purchase ENUM("ON", "OFF") NOT NULL,
                shipped_date DATETIME NOT NULL,
                quantity_bought INT NOT NULL,
                arrived_at DATETIME NOT NULL,
                employee_id INT,
                customer_id INT NOT NULL,
                product_id INT NOT NULL,
                store_id INT NOT NULL,
                FOREIGN KEY (store_id) REFERENCES store(store_id),
                FOREIGN KEY (product_id) REFERENCES product(product_id),
                FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
                FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
            )
        """)