from sqlalchemy.orm.session import Session
from app.domain.account.account_model import Account
from app.domain.account.account_repository import AccountRepository
from app.domain.account.account_schema import (AccountSchema,
                                               AccountSchemaCreate)


def create(db: Session, body: AccountSchemaCreate) -> AccountSchema:
    account = Account(**body.dict())
    return AccountRepository().create(db, account)


def get_accounts(db: Session) -> AccountSchema:
    return AccountRepository().all(db, Account)
