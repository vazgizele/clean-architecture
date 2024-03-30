from dataclasses import dataclass

from src.services.update_atendente_service.DTOs.update_atendente_request_service import UpdateAtendenteRequestService
from src.infra.repositories.iatentende_repository import IAtendenteRepository
from src.infra.repositories.atendente_repository import AtendenteRepository
from src.infra.adapters.db_handler.idb_handler import IDbHandler


@dataclass
class UpdateAtendenteService():
    @staticmethod
    def execute(db_conn: IDbHandler, repo: IAtendenteRepository, atendente_data: UpdateAtendenteRequestService, id: int=0) ->str:
            update_atendente = repo.get(id)

            if not update_atendente:
                  return f"Atendente não existe. [Id={id}]"
            
            update_atendente.nome = atendente_data.nome
            update_atendente.data_nascimento = atendente_data.data_nascimento
            update_atendente.telefone1 = atendente_data.telefone1
            update_atendente.telefone2 = atendente_data.telefone2
            update_atendente.email = atendente_data.email
         

            return 'OK'