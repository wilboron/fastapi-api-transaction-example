from datetime import date, datetime
from pydantic import BaseModel


class AccountSchema(BaseModel):
    id: int
    name: str
    born_date: date
    email: str
    document: str
    phone_number: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AccountSchemaCreate(BaseModel):
    name: str
    born_date: date
    document: str
    email: str
    phone_number: str

    class Config:
        orm_mode = True
