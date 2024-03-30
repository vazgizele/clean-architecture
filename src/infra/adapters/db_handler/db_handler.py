from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker
from .idb_handler import IDbHandler

@dataclass
class DbHandler(IDbHandler):
    db_path: str
    db_timeout: str
    session: Session
    
    def __init__(self, db_path: str, db_timeout:int=300):
        self.db_path=db_path
        self.db_timeout=db_timeout
       
    def get_session(self) -> Session:
        return self.session 

    def __enter__(self):
        self.open()
        return self
       
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def open(self) -> None:
        self.engine = create_engine(self.db_path, echo=True, hide_parameters=False, 
        connect_args={"connect_timeout": self.db_timeout} )
        self.session_maker = sessionmaker()
        self.session = self.session_maker(bind=self.engine)