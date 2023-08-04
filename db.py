from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()
import os

engine = create_async_engine(
    url=os.environ.get("DATABASE_URL"),
    echo=True
)


class Base(DeclarativeBase):
    pass
