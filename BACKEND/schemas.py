from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from pydantic.types import SecretStr, constr
from typing import Optional
import uuid

# THE FOLLOWING SNIPPET WILL BE THE NEXT UPDATE USER HANDLING
# IT WILL TAKE IN CONSIDERATION ACCEPTANCE OF TERMS&CONDITIONS AND PROFILE PICTURE UPDATE
# USER ROUTERS AND MODELS MUST BE UPDATED AS WELL.
# IT FOLLOWS THAT, OBVIOUSLY, A VERSION CONTROL SYSTEM AND A MIGRATION TOOL MUST BE IMPLEMENTED 

# class UserLogin(BaseModel):
#     email: Optional[EmailStr] = Field(unique=True)
#     password: Optional[SecretStr]

# class UserRegister(UserLogin):
#     first_name: Optional[str]
#     last_name: Optional[str]
#     username: Optional[constr(to_lower=True)]
#     terms_of_service_accepted: Optional[bool] = Field(default=False)

# class UserUpdate(UserRegister):
#     is_active: Optional[bool] = True
#     is_superuser: Optional[bool] = False
#     is_deleted: Optional[bool] = False

# class User(UserUpdate):
#     profile_picture: Optional[str] = None


class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    
class UserResponse(BaseModel):
    email: EmailStr
    
    class Config:
        from_attributes = True

class LoginInput(BaseModel):
    email: EmailStr
    password: str

class LoginOutput(BaseModel):
    access_token: str
    token_type: str


class WineBase(BaseModel):
    # id: uuid.UUID
    name: str
    winery: str
    grapes: str

class WineCreate(WineBase):
    id: uuid.UUID
    name: str
    harvest: str
    winery: str
    cover: str
    grapes: str
    production_area: str
    type_of_land: str
    breeding_system: str
    fermentation: str
    refinement: str
    months_of_refinement: str
    alcohol_content: str
    total_acidity: str
    residual_sugars: str
    first_year_of_production: str
    description: str
    refinement_bottle: str
    image: str
    link_site: str
    link_ecommerce: str
    decanting_time: str
    video: str
    pass

class WineResponse(WineBase):

    class Config:
        from_attributes = True


# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     id: Optional[int] = None
