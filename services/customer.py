from fastapi import HTTPException
from schema.customer import Customer, CustomerCreate, customers

class CustomerServices:

    @staticmethod
    def validate_username(payload: CustomerCreate):
        username: str = payload.username
        for customer in customers:
            if customer.username == username:
                raise HTTPException(status_code=400, detail="Customer already exist")
            return payload
        
