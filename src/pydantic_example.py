"""
// C# record
public record User(string Name, int Age, string Email);
"""

from pydantic import BaseModel, field_validator, EmailStr
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: str

u = User(name="Ravi", age=30, email="ravi@gmail.com")
print(u)

u = User(name="Ravi", age="thirty", email=12345) # gives error

# Pydantic tries to coerce before rejecting
u = User(name="Ravi", age="30", email="ravi@gmail.com")
print(u.age)         # 30  ← integer, not string. Pydantic converted it.
print(type(u.age))   # <class 'int'>

class User(BaseModel):
    name: str
    age: int
    role: str = "viewer"              # default value
    bio: Optional[str] = None         # nullable — doesn't need to be provided



class User(BaseModel):
    name: str
    age: int
    email: EmailStr                   # validates email format automatically

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v: int) -> int:
        if v < 18:
            raise ValueError("Must be at least 18")
        return v

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be blank")
        return v.strip()             # clean and return

User(name="Ravi", age=15, email="ravi@gmail.com")
User(name="Ravi", age=19, email="ravimail.com")
u = User(name="Ravi", age=19, email="ravi@mail.com")
u.model_dump_json() # gets class object in JSON format, can be used to send data over network or save to file

data = {"name": "Ravi", "age": 30, "email": "ravi@gmail.com"}
u = User(**data)       # ** unpacks dict as keyword arguments

u = User.model_validate_json('{"name":"Ravi","age":30,"email":"ravi@gmail.com"}')

