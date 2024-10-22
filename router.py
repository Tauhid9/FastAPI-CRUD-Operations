from fastapi import APIRouter, HTTPException, Path, Depends
from pyexpat.errors import messages
from sqlalchemy.testing.plugin.plugin_base import exclusions

from database import SessionLocal
from sqlalchemy.orm import Session, defer
from schemas import BookSchema, RequestBook
# Response

import crud,models

router= APIRouter()

def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request:RequestBook,db:Session=Depends(get_db)):
    __book=crud.create_book(db,book=request.parameter)
    return {
        "code": 200,
        "status": "ok",
        "message": "Book create successfully",
        "result": __book

    }


@router.get('/')
async def get(db:Session=Depends(get_db)):
    __book=crud.get_book(db,0,100)
    return {"liat of Book": __book}


@router.get('/{id}')
async def get_by_id(id:int, db:Session=Depends(get_db)):
    __book = crud.get_book_by_id(db,id)
    # Check if the book exists
    if not __book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Return the result in a structured format
    return {
        "code": 200,
        "status": "ok",
        "message": "Success getting data",
        "result": __book
    }

@router.put("/update")
async def update_book(request: RequestBook, db:Session=Depends(get_db)):
    __book = crud.update_book(db,book_id=request.parameter.id,name=request.parameter.name,description=request.parameter.description)
    if not __book:
        raise HTTPException(status_code=404, detail="Book not update")

        # Return the result in a structured format
    return {
        "code": 200,
        "status": "ok",
        "message": "Success update data",
        "result": __book
    }

@router.delete("/{id}")

async def delete(id:int,db:Session=Depends(get_db)):
   crud.remove_book(db,book_id=id)
   return {  # return Response(code=200, status='ok', message="success delete data").dict(exclude_none=True)
       "code": 200,
       "status": "ok",
       "message": "Success delete data"

   }


