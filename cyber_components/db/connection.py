from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session as _Session


class Connection:
    Base = declarative_base()
    Session = sessionmaker()
    session: _Session = None

    @staticmethod
    def connect(db_url):
        engine = create_engine(db_url, connect_args={
            "check_same_thread": False,
        })

        Connection.Base.metadata.bind = engine
        Connection.Session.configure(bind=engine)

        Connection.session = Connection.Session()

        Connection.Base.metadata.create_all()
