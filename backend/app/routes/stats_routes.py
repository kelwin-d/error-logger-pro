from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.error_model import ErrorLog
from app.database import get_db

router = APIRouter()

@router.get("/stats")
async def get_error_stats(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        "SELECT severity, COUNT(*) FROM error_logs GROUP BY severity"
    )
    return dict(result.fetchall())
