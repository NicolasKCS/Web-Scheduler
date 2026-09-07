# app/database.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

# We will hardcode this for now, but usually, this goes in a .env file.
# Format: postgresql+asyncpg://user:password@host:port/database_name
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/cronops"

# The Engine is the core connection to the database
engine = create_async_engine(DATABASE_URL, echo=True)

# The Session is what we use to actually query the database in our routes
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Base is the parent class for our database models
Base = declarative_base()

# Dependency function to get a database session for each API request
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session