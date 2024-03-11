from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    username: str
    address: str

class CustomerCreate(BaseModel):
    username: str
    address: str


# class CustomerUpdate(BaseModel):
#     username: str = None
#     address: str = None


customers: list[Customer] = [
    Customer(id=1, username="damilare", address="3, olusola str"),
    Customer(id=2, username="sweetboy", address="23, johnson str")
]