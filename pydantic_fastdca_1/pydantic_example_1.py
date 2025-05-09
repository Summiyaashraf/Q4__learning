from pydantic import BaseModel, ValidationError

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None

# Valid data
user_data = {"id": 1, "name": "Summiya", "email": "summiya@example.com", "age": 21}
user = User(**user_data)
print(user)  
print(user.model_dump())  

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="Sakina", email="sakina@example.com")
except ValidationError as e:
    print(e)