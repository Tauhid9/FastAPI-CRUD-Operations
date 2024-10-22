from sqlalchemy.orm import Session
from models import Book
from schemas import BookSchema
import models

# get all book data
def get_book(db:Session,skip:int=0,limit:int=100):
    return db.query(Book).offset(skip).limit(limit).all()
# get by book id
def get_book_by_id(db:Session,book_id:int):
    return db.query(Book).filter(Book.id == book_id).first()

# create book data

def create_book(db:Session,book:BookSchema):
    __book = Book(name=book.name,description=book.description)
    db.add(__book)
    db.commit()
    db.refresh(__book)
    return __book

# remove book data
def remove_book(db:Session,book_id:int):
    __book= get_book_by_id(db=db,book_id=book_id)
    db.delete(__book)
    db.commit()

# update book data
def update_book(db:Session,book_id:int,name:str,description:str):
    __book = get_book_by_id(db=db,book_id=book_id)
    __book.name=name
    __book.description=description
    db.commit()
    db.refresh(__book)
    return __book
