import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text

app = FastAPI(title="SkyCare API")

# Получаем ссылку на базу данных из переменных окружения
# На Render она хранится в DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Обработка особенности Render: Render выдает URL начиная с 'postgres://', 
# но SQLAlchemy требует 'postgresql://'
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "SkyCare Backend is running!"}


@app.get("/health/db")
def check_db_connection():
    if not DATABASE_URL:
        raise HTTPException(
            status_code=500,
            detail="DATABASE_URL environment variable is not set"
        )

    try:
        # Создаем подключение и выполняем тестовый запрос
        engine = create_engine(DATABASE_URL)
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