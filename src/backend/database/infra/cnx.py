import os
from mysql.connector.aio import connect
from mysql.connector.abstracts import MySQLConnectionAbstract
from typing import Optional

class Cnx:

    def __init__(self):
        self.__db_password: Optional[str] = os.getenv("MYSQL_PASSWORD")
        if self.__db_password is None: raise Exception("Password couldn't be found")

    async def get_wcnx(self) -> MySQLConnectionAbstract:
        return await connect(
            user = "root",
            host = "localhost",
            password = self.__db_password
        )

    async def get_cnx(self) -> MySQLConnectionAbstract:
        return await connect(
            user = "root",
            host = "localhost",
            database = os.getenv("DB_NAME"),
            password = self.__db_password
        )