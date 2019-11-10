from sqlalchemy import Column, String, Boolean, create_engine, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = 'sqlite:///D:/Users/Nikhil KM/Projects/sanlap/models.db'

db_session = None

Base = declarative_base()


def _init_db(url):
    global db_session
    db_engine = create_engine(url, echo=True)
    db_session = sessionmaker(bind=db_engine)()
    Base.metadata.create_all(db_engine)


def get_db(url=DATABASE):
    """
    Gets the DB Session created for SQ Lite
    :param url: the URL to connect to
    :return: db object
    """
    global db_session
    if not db_session:
        _init_db(url)
    return db_session


class TrainedModel(Base):
    __tablename__ = 'trained_model'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    version = Column(Float)
    path = Column(String, nullable=False)
    is_active = Column(Boolean, type_nullable=False)

    def __repr__(self):
        return f'<TrainedModel(name={self.name}, version={self.version}, path={self.path}, is_active={self.is_active})>'


class Intent(Base):
    __tablename__ = 'intent'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    model = Column(String)
    action_class = Column(String)
