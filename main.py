from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from contextlib import asynccontextmanager

import models
import schemas
import crud
from database import engine, get_db
from config import get_settings

settings = get_settings()

# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables
    print("Creating database tables...")
    models.Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
    yield
    # Shutdown: Add cleanup code here if needed
    print("Shutting down...")

app = FastAPI(
    title=settings.APP_NAME,
    description="FastAPI with MySQL and SQLAlchemy",
    version="1.0.0",
    lifespan=lifespan
)

# Health check endpoint
@app.get("/", tags=["Health"])
def root():
    return {
        "message": "Welcome to FastAPI with MySQL",
        "status": "healthy"
    }

@app.get("/health", tags=["Health"])
def health_check(db: Session = Depends(get_db)):
    try:
        # Test database connection
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}

# User endpoints
@app.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Item endpoints
@app.post("/users/{user_id}/items/", response_model=schemas.Item, tags=["Items"])
def create_item_for_user(
    user_id: int,
    item: schemas.ItemCreate,
    db: Session = Depends(get_db)
):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get("/items/", response_model=List[schemas.Item], tags=["Items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)