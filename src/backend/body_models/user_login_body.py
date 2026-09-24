from pydantic import BaseModel

class UserLoginBody(BaseModel):

    email: str
    password: str