from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import DateTime


class BaseModel(object):
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.now)

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, default=datetime.now, onupdate=datetime.now)


Base = declarative_base(cls=BaseModel)
