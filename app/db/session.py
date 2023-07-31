from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # Base 생성
from sqlalchemy.orm import sessionmaker

from app.common.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    )

Base = declarative_base()