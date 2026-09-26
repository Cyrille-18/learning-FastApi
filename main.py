"""
Simple FastAPI app for learning purpose

"""


from fastapi import FastAPI # import FastAPI class from fastapi module

app = FastAPI() # Create a FastAPI instance

# request methods: GET, POST, PUT, DELETE
@app.get("/")
def read_root() : 
    return {"message": "Welcome to FastApi world"}

@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}

@app.put("/items/{item_id}") 
def update_item(item_id: int, name:str, price: float) :
    return {"item_id": item_id, "name": name, "price": price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int) :
    return {"item_id": item_id, "message":"Item deleted successfully"}

#Query Parameters
@app.get("/users/")
def read_users(user_id: int, name: str = None) :
    return {"user_id": user_id, "name": name}