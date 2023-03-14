import psycopg2.extras
from fastapi import APIRouter, Depends, HTTPException, Query, Body, File, UploadFile, Form, Request
from sqlalchemy.orm import Session
from pydantic import BaāseModel
from typing import Optional
from loguru import logger
from init import get_raw_db, get_db
from src.db.alchemy_models import table

router = APIRouter()


class add(BaseModel):
    id : int
    name: str


@router.post('/create/test', tags=["Test"])
def add(
        info : add,
        db: Session = Depends(get_db)
):
    try:
        new_update = table(
            id=info.id,
            name=info.name
        )
        db.add(new_update)
        db.commit()

        return {
            "details": "success",
        }
    except HTTPException as e:
        logger.error(f'{e}')
        raise e
    except Exception as e:
        logger.error(f'{e}')
        raise HTTPException(status_code=500, detail=f'{e}')


@router.get('/test/list', tags=["Test"])
def test_list(
        db: Session = Depends(get_db)

):

    try:
        res = db.query(table).all()
        return{
            "data" : res
        }
    except HTTPException as e:
        logger.error(f'{e}')
        raise e
    except Exception as e:
        logger.error(f'{e}')
        raise HTTPException(status_code=500, detail=f'{e}')
