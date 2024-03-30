from dataclasses import dataclass
from typing import List

from src.services.inserted_atendente_service.DTO.create_atendente_response import CreateAtendenteResponseService
from src.infra.repositories.iatentende_repository import IAtendenteRepository
from src.infra.adapters.db_handler.idb_handler import IDbHandler

@dataclass
class GetAtendenteService:
    @staticmethod
    def execute(db_conn: IDbHandler, repo: IAtendenteRepository, id: int)->CreateAtendenteResponseService:
       return repo.get(id)