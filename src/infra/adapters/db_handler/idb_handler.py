from abc import ABC
from dataclasses import dataclass
from sqlalchemy.orm.session import Session


@dataclass
class IDbHandler(ABC):
    def get_session(self) -> Session:
        raise Exception("Not Implemented")
    
    def __enter__(self):
        raise Exception("Not Implemented")

    def __exite__(self):
            raise Exception("Not Implemented")

    def open(self) -> None:
            raise Exception("Not Implemented")    
        