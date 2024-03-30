from dataclasses import dataclass
from typing import List

from src.infra.repositories.iatentende_repository import IAtendenteRepository
from src.infra.adapters.db_handler.idb_handler import IDbHandler
from src.services.get_atendente_service.implementation.DTOS.get_atendente_response_service import AtendenteResponseService


@dataclass
class GetAtendenteService:
    @staticmethod
    def execute(db_conn: IDbHandler, repo: IAtendenteRepository, id: int)->AtendenteResponseService:
       return repo.get(id)

        
