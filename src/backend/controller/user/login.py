from src.backend.routes.routes import ROUTE_USER
from typing import Dict
from src.backend.body_models.user_login_body import UserLoginBody
import bcrypt
from fastapi import Response, status, Request
from src.backend.database.DQL.get_user_by_email import get_user_by_email
import bcrypt

@ROUTE_USER.post("/login")
async def register_user(user: UserLoginBody, req: Request, res: Response) -> Dict[str, bool]:
    credentials: Dict[str, int | str | bool] = await get_user_by_email(user.email, pool = req.app.state.pool)
    #Checking existence of the user in the database
    if not credentials["present"]:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return {"authorized" : False}
    #Checking password if the user is in the database
    attempted_pw_bytes: bytes = user.password.encode("utf-8")
    hashed_pw: str = credentials["password"].encode("utf-8")
    is_ok: bool = bcrypt.checkpw(attempted_pw_bytes, hashed_pw)
    if is_ok:
        res.status_code = status.HTTP_200_OK
        return {"authorized" : True}
    else:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return {"authorized" : False}