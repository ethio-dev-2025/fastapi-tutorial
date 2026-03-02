from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# MySQL configuration
MYSQL_USER = "root"
MYSQL_PASSWORD = "0928534003"  # Your actual password
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "fastapi_db"

# ✅ CORRECT DATABASE URL - use this line
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


# Connection - use DATABASE_URL instead
engine = create_engine(DATABASE_URL)

# Session
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base
Base = declarative_base()