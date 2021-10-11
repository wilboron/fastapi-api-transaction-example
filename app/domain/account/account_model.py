from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from app.commons.base_model import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    born_date = Column(Date)
    document = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
