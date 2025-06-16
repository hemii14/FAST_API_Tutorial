from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from blog.JWTtoken import verify_token  # ✅ Use correct custom function

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # ✅ Match your router prefix and endpoint

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(data, credentials_exception)  # ✅ Token validation
