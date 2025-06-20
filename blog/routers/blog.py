from typing import List
from fastapi import APIRouter, Depends, Response,status,HTTPException
from sqlalchemy.orm import Session
from blog import schemas,database,models
from blog import oauth2
from blog.oauth2 import get_current_user
from blog.repository import blog

router=APIRouter(
    tags=['Blogs'],
    prefix="/blog"
)

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return blog.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.get('/{id}', response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.show(id,db)
