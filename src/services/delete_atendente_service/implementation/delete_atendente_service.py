from dataclasses import dataclass

from src.infra.adapters.db_handler.idb_handler import IDbHandler
from src.domain.entities.atendente import Atendente
from src.infra.repositories.iatentende_repository import IAtendenteRepository

@dataclass
class DeleteAtendenteService:
    @staticmethod
    def execute(db_conn: IDbHandler, repo: IAtendenteRepository, id: int=0) -> str:
        atendente = repo.get(id)
        
        if not atendente:
            return f'Atentende não existe [Id={id}]'
        repo.delete(id)

        return 'Ok'