
from fastapi import APIRouter,Depends, HTTPException,status
from blog import models, schemas
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog.repository import user
 
router=APIRouter(
    tags=['Users'],
    prefix="/user"
)

@router.post("/",response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request,db)


@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.show(id,db)