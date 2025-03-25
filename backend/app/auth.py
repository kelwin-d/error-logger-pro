from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.config import SECRET_KEY

# JWT Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock User Data
users_db = {
    "admin": {"username": "admin", "password": "admin123", "role": "admin"},
    "viewer": {"username": "viewer", "password": "viewer123", "role": "viewer"}
}

def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if user and user['password'] == password:
        return user
    return None

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return users_db.get(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

async def require_admin(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Access denied")
    return user
