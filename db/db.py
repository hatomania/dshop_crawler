# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import settings

DB_SERVER=settings.DB_SERVER
DB_PORT=settings.DB_PORT
DB_USERNAME=settings.DB_USERNAME
DB_PASSWORD=settings.DB_PASSWORD
DB_DBNAME=settings.DB_DBNAME

# 例: postgresql://user:password@localhost:5432/yourdatabase
DATABASE_URL =  f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DBNAME}"

# DBエンジンの作成
engine = create_engine(DATABASE_URL)

# セッションの生成関数
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
