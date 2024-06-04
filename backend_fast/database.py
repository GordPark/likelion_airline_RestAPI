# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 URL 설정
# DATABASE_URL = "postgresql+asyncpg://psql_admin:1234@localhost:5432/psql_db"

# SQLite 데이터베이스 파일 경로
DATABASE_URL = "sqlite:///./fastapi.db"

# utf-8의 인코딩 방식으로 DB 접속 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)
# 비동기 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # class_=AsyncSession


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
