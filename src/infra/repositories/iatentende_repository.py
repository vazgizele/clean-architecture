from abc import ABC
from typing import List

from src.domain.entities.atendente import Atendente
from src.infra.adapters.db_handler.idb_handler import IDbHandler

class IAtendenteRepository(ABC):
    def __init__(self, db: IDbHandler):
        raise Exception("Not Implemented")
    
    def get(self, id: int) -> Atendente:
        raise Exception("Not Implemented")

    def get_all(self) -> List[Atendente]:
        raise Exception("Not Implemented")
    
    def get_byname(self, name: str) -> Atendente:
        raise Exception("Not Implemented")
    
    def get_byemail(self, email: str) -> Atendente:
        raise Exception("Not Implemented")
    
    def add(self, new: Atendente) -> None:
        raise Exception("Not Implemented")
    
    def delete(self, id: int) -> None:
        raise Exception("Not Implemented")