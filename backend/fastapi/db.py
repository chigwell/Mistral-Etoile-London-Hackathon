from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    JSON,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

# Define the path to the SQLite database
DATABASE_FILENAME = "database.db"

# Create the database engine
engine = create_engine(f"sqlite:///{DATABASE_FILENAME}")

# Base class for models
Base = declarative_base()


class Screenshot(Base):
    __tablename__ = "screenshots"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    link = Column(String)
    description = Column(String)
    source_code = Column(String)
    graph = Column(JSON)


class Risk(Base):
    __tablename__ = "risks"
    id = Column(Integer, primary_key=True)
    risk_type = Column(String)
    screen_id = Column(Integer, ForeignKey("screenshots.id"))
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    screenshot = relationship("Screenshot", back_populates="risks")


class Graph(Base):
    __tablename__ = "graphs"
    id = Column(Integer, primary_key=True)
    node_from = Column(String)
    node_to = Column(String)
    relation = Column(String)
    screen_id = Column(Integer, ForeignKey("screenshots.id"))
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    screenshot = relationship("Screenshot", back_populates="graphs")


class Insight(Base):
    __tablename__ = "insights"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    psychological_insight = Column(JSON)
    professional_potential = Column(String)
    interests = Column(JSON)


# Relationship backref
Screenshot.risks = relationship("Risk", order_by=Risk.id, back_populates="screenshot")
Screenshot.graphs = relationship(
    "Graph", order_by=Graph.id, back_populates="screenshot"
)

# Create all tables in the database
Base.metadata.create_all(engine)
