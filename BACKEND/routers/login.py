from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, oauth2, schemas
from ..database import get_db
from ..utils import verify


router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post('/', response_model=schemas.LoginOutput)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    # When retrieving the useremail ftrom OAuth2PasswordRequestForm it will be stored as username.
    # In Postman it will be given no longer as a raw json but as a form-data
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data = {"user_mail": user.email})

    return {'access_token': access_token, "token_type": "bearer"}


# router = APIRouter(tags=['Authentication'])

# @router.post('/login', response_model=schemas.Token)
# def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
#     # When retrieving the useremail ftrom OAuth2PasswordRequestForm it will be stored as username.
#     # In Postman it will be given no longer as a raw json but as a form-data
#     user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

#     if not verify(user_credentials.password, user.password):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

#     access_token = oauth2.create_access_token(data = {"user_id": user.id})

#     return {'access_token': access_token, "token_type": "bearer"}