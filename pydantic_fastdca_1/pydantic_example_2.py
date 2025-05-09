from pydantic import BaseModel, EmailStr

# Define a nested model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr  
    addresses: list[Address] 

# Valid data with nested structure
user_data = {
    "id": 2,
    "name": "Sakina",
    "email": "sakina@example.com",
    "addresses": [
        {"street": "6", "city": "Karachi", "zip_code": "101201"},
        {"street": "7", "city": "Lahore", "zip_code": "209706"},
    ],
}
user = UserWithAddress.model_validate(user_data)
print(user.model_dump())