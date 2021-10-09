from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import sessionmaker

from ..config import DATABASE_URL

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session
sessionLocal = sessionmaker(bind=engine)

# Create base class for ORMs
Base = declarative_base()
