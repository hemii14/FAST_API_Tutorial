from fastapi import HTTPException,status
from sqlalchemy.orm import Session

from blog import schemas
from .. import models


def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session ):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id=request.user_id  
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id{id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Blog,db:Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog = blog_query.first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    # ✅ FIX: Convert request to dict
    blog_query.update(request.dict())
    db.commit()

    return {"message": "Updated successfully"}


def show(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available"
        )

    return blog
