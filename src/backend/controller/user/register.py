from src.backend.routes.routes import ROUTE_USER
from typing import Dict
from src.backend.body_models.user_register_body import UserRegisterBody
import bcrypt
from src.backend.database.DTL.new_user_in import load_new_user
from fastapi import Response, status, Request

@ROUTE_USER.post("/register")
async def register_user(user: UserRegisterBody, req: Request, res: Response) -> Dict[str, bool]:
    pw_bytes: bytes = user.password.encode("utf-8")
    salt: bytes = bcrypt.gensalt() #<--- salt of 12
    hashed_pw: str = bcrypt.hashpw(pw_bytes, salt).decode("utf-8")
    inside: bool = await load_new_user(
        fname = user.fname,
        lname = user.lname,
        email = user.email,
        password = hashed_pw,
        phone = user.phone,
        sex = user.sex,
        country = user.country,
        province = user.province,
        city = user.city,
        pool = req.app.state.pool
    )
    if inside:
        res.status_code = status.HTTP_201_CREATED
        return {"success" : True}
    else:
        res.status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
        return {"success" : False}