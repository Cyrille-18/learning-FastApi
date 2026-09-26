"""
Handling request and responses bodies with data validation using Pydantic models in FastAPI

"""

from fastapi import FastAPI
from pydantic import BaseModel, field_validator, Field

app = FastAPI()

# model for user data
class User(BaseModel):
    name: str
    age: int = Field(...,gt=0,le=120) # use Field to set constraints on age field (greater than 0 and less than or equal to 120)

    @field_validator("name") # use field_validator decorator to validate the name field
    def name_must_not_be_empty(cls,v):
        """
        Validate that the name field is not empty
        param cls: class
        param v: value of the name field
        """
        if not v:
            raise ValueError("Name cannot be empty")
        return v

# apply response_model to specify the response model for the endpoint
@app.post("/users/")
def create_user(user: User):
    return {"sended user": user.name, "sended age": user.age}

# apply response_model and validator 
@app.get("/users/{user_id}", response_model= User)
async def get_users(user_id : int) :
    #example user data
    return {"name": "John", "age": 30}