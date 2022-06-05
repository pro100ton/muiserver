from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from db.constants import DATABASE_URL

# TODO: change sqlite engine to PostgreSQL engine
# Creating db engine
engine = create_async_engine(DATABASE_URL, future=True, echo=True)
# expire_on_commit - we make sure that our DB entities and fields will be available even after commit was made
#   on the session
# class_ - declaring new Async session
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()