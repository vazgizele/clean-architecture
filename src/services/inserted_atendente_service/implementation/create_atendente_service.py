from dataclasses import dataclass

from src.infra.adapters.db_handler.idb_handler import IDbHandler
from src.domain.entities.atendente import Atendente
from src.infra.repositories.iatentende_repository import IAtendenteRepository
from src.services.inserted_atendente_service.implementation.DTO.create_atendente_request import CreateAtendenteRequestService
from src.services.inserted_atendente_service.implementation.DTO.create_atendente_response import CreateAtendenteResponseService


@dataclass
class CreateAtendenteService:
    @staticmethod
    def execute(db_conn: IDbHandler, repo: IAtendenteRepository, new_atendente: CreateAtendenteRequestService) -> CreateAtendenteResponseService:
        response: CreateAtendenteResponseService
        atendente = repo.get_byname(new_atendente.nome)
        if atendente:
            response.msg = f"Já existe atendente com esse nome '{new_atendente.nome}.'"
            return response
        
        new_atendente = Atendente(id=1, nome=new_atendente.nome, data_nascimento=new_atendente.data_nascimento, telefone1=new_atendente.telefone1, telefone2=new_atendente.telefone2, email=new_atendente.email)
        repo.add(new_atendente)
        db_conn.session.commit()
        response.id = new_atendente.id
            
