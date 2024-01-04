from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import  List, Optional
from .. import models, schemas, oauth2


router = APIRouter(
    prefix="/wines",
    tags=["Wines"]
)

@router.get("/", response_model=List[schemas.WineResponse])
def get_wines(db: Session = Depends(get_db)):
    wines = db.query(models.Wine).all()
    return wines


# router = APIRouter(
#     prefix="/posts",
#     tags=["Posts"]
# )

# # @router.get("/", response_model=List[schemas.PostResponse])
# @router.get("/")
# def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 100, skip: int = 0, search: Optional[str] = ''):
#     # cursor.execute("""SELECT * FROM posts""")
#     # posts = cursor.fetchall()
#     posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

#     results = db.query(models.Post, func.count(models.Vote.post_id)).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()

#     return results


# @router.get("/own", response_model=List[schemas.PostResponse])
# def get_own_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     # cursor.execute("""SELECT * FROM posts""")
#     # posts = cursor.fetchall()
#     posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
#     return posts


# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse) # define a default HTTP status code for the operation
# def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)): # this is a control schema syntact provided by pydantic. Compare the imput (post) to the schema we want to follow (Post class that we defined before)
#     # cursor.execute(f"INSERT INTO posts (title, content, published) VALUES ({post.title}, {post.content}, {post.published})")
#     # this string ABOVE actually works, but makes you vulnerable from SQL injection (i.e. manipulating database from outside input)
    
#     # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published)) # COMMAND WHAT YOU WANT
#     # new_post = models.Post(title=post.title, content=post.content, published=post.published) NOT A GOOD PRACTICE
#     new_post = models.Post(owner_id=current_user.id, **post.model_dump()) # compact notatio with unpack methods
#     # new_post = cursor.fetchone() #EXECUTE WHAT YOU WANT
#     db.add(new_post)
#     # conn.commit() #UPDATE DATABASE
#     db.commit()
#     # this act like RETURNING *
#     db.refresh(new_post)
    
#     return new_post


# @router.get("/{id}", response_model=schemas.PostResponse) #id is a path parameter
# def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     # post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")
#     return post


# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     # cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id)))
#     post_query = db.query(models.Post).filter(models.Post.id == id)

#     post = post_query.first()
#     # deleted_post = cursor.fetchone()
#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")
    
#     if post.owner_id != current_user.id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not authorized to perform requested action')
    
#     post_query.delete(synchronize_session=False)

#     # conn.commit()
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)
    

# @router.put("/{id}", response_model=schemas.PostResponse)
# def update_post(id: int, updated_post: schemas.PostBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     post = post_query.first()

#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")      
#     if post.owner_id != current_user.id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not authorized to perform requested action')
#     # modified_post = cursor.fetchone()
#     # conn.commit()
#     post_query.update(updated_post.model_dump(), synchronize_session=False)

#     db.commit()

#     return post_query.first()