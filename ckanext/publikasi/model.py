import uuid
import ckan.model as model
from sqlalchemy import create_engine, Column, Integer, String, Text, \
    BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Initialize the base class for SQLAlchemy models
Base = declarative_base(metadata=model.meta.metadata)

# Define the publikasi model
class Publikasi(Base):
    __tablename__ = 'ckanext_publikasi'

    id = Column(Integer, primary_key=True, autoincrement=True)
    unique_id = Column(Text, unique=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    author = Column(String, nullable=True)
    type = Column(String, nullable=True)
    file_path = Column(Text, nullable=True)
    user_own = Column(String, nullable=True)
    cover_image = Column(Text, nullable=True)
    meta_catalog_number = Column(String, nullable=True)
    meta_publication_number = Column(String, nullable=True)
    meta_isbn_issn = Column(String, nullable=True)
    meta_release_frequency = Column(String, nullable=True)
    meta_release_date = Column(DateTime, nullable=True)
    meta_language = Column(String, nullable=True)
    meta_file_size = Column(BigInteger, nullable=True)
    created = Column(DateTime, default=datetime.datetime.now())
    modified = Column(DateTime, nullable=True)

    def __init__(self, unique_id, title, description=None, author=None, \
                type=None, file_path=None, user_own=None, cover_image=None, \
                meta_catalog_number=None, meta_publication_number=None, meta_isbn_issn=None, \
                meta_release_frequency=None, meta_release_date=None, meta_language=None, \
                meta_file_size=None, created=None, modified=None):
        self.unique_id = unique_id
        self.title = title
        self.description = description
        self.author = author
        self.type = type
        self.file_path = file_path
        self.user_own = user_own
        self.cover_image = cover_image
        self.meta_catalog_number = meta_catalog_number
        self.meta_publication_number = meta_publication_number
        self.meta_isbn_issn = meta_isbn_issn
        self.meta_release_frequency = meta_release_frequency
        self.meta_release_date = meta_release_date
        self.meta_language = meta_language
        self.meta_file_size = meta_file_size
        self.created = created
        self.modified = modified

    def __repr__(self):
        return f"<Publikasi(id={self.id}, unique_id={self.unique_id}, title={self.title}, \
            description={self.description} )"

# Database utility function
def get_engine(database_url):
    return create_engine(database_url)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

