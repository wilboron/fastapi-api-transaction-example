from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session
from app.config.database import get_db

from app.domain.account.account_schema import (AccountSchema,
                                               AccountSchemaCreate)
from app.domain.account import account_service

router = APIRouter()


@router.post("/",
             summary="Operação responsável por criar uma nova conta.",
             response_model=AccountSchema)
def create_account(body: AccountSchemaCreate, db: Session = Depends(get_db)):
    return account_service.create(db, body)


@router.get("/",
            summary="Operação responsável por retornar a conta por filtro.",
            response_model=List[AccountSchema])
def get_accounts(db: Session = Depends(get_db)):
    return account_service.get_accounts(db)
