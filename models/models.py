from sqlalchemy import *
import sqlalchemy.ext.declarative
Base = sqlalchemy.ext.declarative.declarative_base()
url = 'sqlite:///' + 'db/db.db'
engine = sqlalchemy.create_engine(url)
Session = sqlalchemy.orm.sessionmaker(bind=engine)


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    todo = Column(Text, nullable=False)
    done = Column(Boolean, nullable=False)


def create_tables():
    Base.metadata.create_all(engine)