from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from annotated_types import MaxLen, MinLen

class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr
