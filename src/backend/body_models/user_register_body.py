from pydantic import BaseModel, Field

class UserRegisterBody(BaseModel):

    fname: str = Field(..., max_length = 50, min_length = 3)
    lname: str = Field(..., max_length = 50, min_length = 3)
    email: str
    password: str = Field(..., min_length = 8)
    phone: str = Field(..., min_length = 6, max_length = 30)
    sex: str
    country: str = Field(..., max_length = 50, min_length = 3)
    province: str = Field(..., max_length = 50, min_length = 2)
    city: str = Field(..., max_length = 50, min_length = 2)