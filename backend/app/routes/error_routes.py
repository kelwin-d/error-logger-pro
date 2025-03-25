from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.error_model import ErrorLog
from app.database import get_db
from app.auth import require_admin

router = APIRouter()

@router.get("/", dependencies=[Depends(require_admin)])
async def get_errors(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM error_logs")
    return result.fetchall()

@router.post("/", dependencies=[Depends(require_admin)])
async def log_error(request: Request, error: dict, db: AsyncSession = Depends(get_db)):
    user_agent = request.headers.get('user-agent', 'Unknown')

    new_error = ErrorLog(
        message=error["message"],
        severity=error["severity"],
        source=error.get("source", "Unknown"),
        stack_trace=error.get("stack_trace", None),
        user_agent=user_agent,
        request_url=str(request.url),
        request_method=request.method
    )

    db.add(new_error)
    await db.commit()
    return {"message": "Error logged successfully"}
