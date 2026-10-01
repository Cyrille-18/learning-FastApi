""""
    Data validation using Pydantic models in FastAPI
"""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, conint, constr, field_validator


#Advanced validators
# Regular expressions
#Custom validation

class User(BaseModel) :
    username : constr(regex=r'^[a-zA-Z0-9_]+$', min_length=3, max_length=20) # use constr to set constraints on username field (regex pattern, min and max length)
    email : EmailStr
    age : conint(gt=0)

    @field_validator("username") # use field_validator decorator to validate the username field
    def username_must_not_contains_spaces(cls,v):
        if " " in v:
            raise ValueError("Username must not contain spaces")
        return v

app = FastAPI()

@app.post("/register/") 
async def register_user(user: User) :
    return user