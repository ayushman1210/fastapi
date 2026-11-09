from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from src.api.schemas import PostCreate, PostResponse
from src.db import models
from src.db.database import get_db

router = APIRouter(tags=["posts"])


@router.get("/post", response_model=list[PostResponse])
def get_posts(db: Annotated[Session, Depends(get_db)]):
    statement = select(models.Post).options(selectinload(models.Post.author))
    return db.scalars(statement).all()


@router.get("/post/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    statement = (
        select(models.Post)
        .options(selectinload(models.Post.author))
        .where(models.Post.id == post_id)
    )
    post = db.scalar(statement)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )
    return post


@router.post(
    "/create",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post(post: PostCreate, db: Annotated[Session, Depends(get_db)]):
    if db.get(models.User, post.user_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    db_post = models.Post(
        title=post.title,
        content=post.content,
        user_id=post.user_id,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
