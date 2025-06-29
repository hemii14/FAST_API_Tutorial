from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from blog import models, database, schemas
from blog import JWTtoken  # ✅ Correct import
from ..hashing import Hash

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token = JWTtoken.create_access_token(data={"sub": user.email})  # ✅ use your custom function

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
