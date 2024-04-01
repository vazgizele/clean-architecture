from typing import List
from src.domain.entities.atendente import Atendente
from src.infra.adapters.db_handler.idb_handler import IDbHandler
from src.infra.repositories.iatentende_repository import IAtendenteRepository

class  AtendenteRepository(IAtendenteRepository):
    def __init__(self, db: IDbHandler):
        self.session = db.get_session()

    def get(self, id: int) -> Atendente:
        return self.session.query(Atendente).filter_by(id=id).first()
    
    def get_all(self) -> List[Atendente]:
        return self.session.query(Atendente).all()
    
    def get_byname(self, nome: str) -> Atendente:
        return self.session.query(Atendente).filter_by(nome=nome).first()
    
    def get_byemail(self, email: str) -> Atendente:
        return self.session.query(Atendente).filter_by(email=email).first()
    
    def add(self, new: Atendente) -> None:
        new.validade()
        new.id = None
        self.session.add(new)
        self.session.flush()

    def delete(self, id: int) -> None:
        self.session.query(Atendente).filter_by(id=id).delete()
        self.session.flush()