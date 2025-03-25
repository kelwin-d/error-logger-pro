from fastapi import APIRouter, HTTPException, Depends
from app.auth import require_admin
from app.models.user_model import User
from app.database import get_db

@router.get("/")
async def get_users():
    return [{"id": 1, "name": "Admin"}, {"id": 2, "name": "Developer"}]

@router.post("/create-user", dependencies=[Depends(require_admin)])
async def create_user(username: str, password: str, role: str, db: AsyncSession = Depends(get_db)):
    new_user = User(username=username, password=password, role=role)
    db.add(new_user)
    await db.commit()
    return {"message": "User created successfully"}

