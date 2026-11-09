from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.schemas import UserCreate, UserResponse
from src.db import models
from src.db.database import get_db

router = APIRouter(tags=["users"])


@router.post(
    "/create/user",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def user_create(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.scalar(
        select(models.User).where(
            (models.User.username == user.username)
            | (models.User.email == user.email)
        )
    )
    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this username or email already exists",
        )

    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.get(models.User, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user