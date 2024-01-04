from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import  List
from .. import models, schemas, utils


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.model_dump())

    user_check = db.query(models.User).filter(models.User.email == new_user.email).first()
    if user_check:
        raise HTTPException(status_code=status.HTTP_226_IM_USED, detail=f'User with email: {new_user.email} already registered')

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.get("/", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    users = db.query(models.User).all()
    return users


# router = APIRouter(
#     prefix="/users",
#     tags=["Users"]
# )


# @router.get("/", response_model=List[schemas.UserResponse])
# def get_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
# def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password
    
#     new_user = models.User(**user.model_dump())

#     user_check = db.query(models.User).filter(models.User.email == new_user.email).first()
#     if user_check:
#         raise HTTPException(status_code=status.HTTP_226_IM_USED, detail=f'User with email: {new_user.email} already registered')

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
    
#     return new_user


# @router.get("/{id}", response_model=schemas.UserResponse)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id: {id} does not exist')
    
#     return user