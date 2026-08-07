from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Point to a local file named ecoroute.db
DATABASE_URL = "sqlite:///./ecoroute.db"

# 2. Create the database connection engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 3. Define how our Smart Bin table looks inside the database
class BinModel(Base):
    __tablename__ = "smart_bins"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    fill_level = Column(Float, default=0.0)
    last_updated = Column(String, nullable=True)

# Helper function to open/close database connections safely
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()