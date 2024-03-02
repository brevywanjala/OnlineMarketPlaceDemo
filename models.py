from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey,Float,Date
from sqlalchemy.orm import sessionmaker, relationship ,foreign
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,date


Base = declarative_base()
db_url = 'sqlite:///market_store.db'


engine = create_engine(db_url,pool_size=10, max_overflow=5)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username=Column(Integer)# Add user-related fields (e.g., name, email, password, etc.)
    email = Column(String(20),unique=True)  # 'teacher' or 'parent'
    phone= Column(String(255))
    password=Column(String(255))
    usertype=Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    

  




Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()