from dataclasses import dataclass
from typing import List

from src.infra.adapters.db_handler.idb_handler import IDbHandler
from src.infra.repositories.atendente_repository import AtendenteRepository
from src.infra.repositories.iatentende_repository import IAtendenteRepository
from src.services.list_all_atendentes_service.implementation.DTOS.list_all_atendentes_response_service import ListAllAtendenteResponseService


@dataclass
class ListAllAtendenteService:
    @staticmethod
    def execute(db_conn: IDbHandler, repo: IAtendenteRepository) ->List[ListAllAtendenteResponseService]:
        repo = AtendenteRepository(db_conn)
        ret = []
        for item in repo.get_all():
            ret.append(ListAllAtendenteResponseService(item.id, item.nome, item.data_nascimento, item.telefone1, item.telefone2, item.email))
        
        return ret