from asyncmy import Pool

async def load_new_user(
    fname: str,
    lname: str,
    email: str,
    password: str,
    phone: str,
    sex: str,
    country: str,
    province: str,
    city: str,
    pool: Pool
    ) -> bool:
    signal: bool = False
    async with pool.acquire() as cnx:
        async with cnx.cursor() as cursor:
            try:
                await cursor.execute("INSERT INTO address (country, province, city) VALUES (%s, %s, %s)",
                            (country, province, city))
                address_id: int = cursor.lastrowid
                print((fname, lname, email, password, phone, sex, address_id))
                await cursor.execute("INSERT INTO user (first_name, last_name, email, password, phone, sex, address_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                (fname, lname, email, password, phone, sex, address_id))
            except:
                print(3)
                await cnx.rollback()
            else:
                await cnx.commit()
                signal = True
    return signal