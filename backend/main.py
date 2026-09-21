import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text

app = FastAPI(title="SkyCare API")

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)


def get_db_engine():
    if not DATABASE_URL:
        raise HTTPException(
            status_code=500,
            detail="DATABASE_URL environment variable is not set"
        )
    return create_engine(DATABASE_URL)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "SkyCare Backend is running!"}


@app.get("/health/db")
def check_db_connection():
    try:
        engine = get_db_engine()
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1;"))
            return {
                "status": "connected",
                "database": "PostgreSQL",
                "test_query_result": result.scalar()
            }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )


@app.get("/users")
def get_users():
    """Получение списка пользователей из базы данных"""
    try:
        engine = get_db_engine()
        with engine.connect() as connection:
            # Запрос к таблице users
            result = connection.execute(text("SELECT * FROM users LIMIT 50;"))

            # Преобразуем строки таблицы в список словарей
            users = [dict(row._mapping) for row in result]

            return {
                "count": len(users),
                "users": users
            }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching users: {str(e)}"
        )