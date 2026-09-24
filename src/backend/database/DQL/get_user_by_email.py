from typing import Dict, List, Tuple
from asyncmy import Pool

async def get_user_by_email(email: str, pool: Pool) -> Dict[str, int | str | bool] | None:
    user_credential: List[Tuple[int, str]] = list()
    async with pool.acquire() as cnx:
        async with cnx.cursor() as cursor:
            await cursor.execute("SELECT uid, password FROM user WHERE email = %s", (email,))
            user_credential = await cursor.fetchall()
    if len(user_credential) == 0:
        return {"present": False}
    else:
        return {
            "id" : user_credential[0][0],
            "password" : user_credential[0][1],
            "present": True
        }