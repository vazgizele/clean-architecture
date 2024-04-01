from dataclasses import dataclass

from src.services.inserted_atendente_service.DTO.create_atendente_request import CreateAtendenteRequestService
from src.services.inserted_atendente_service.DTO.create_atendente_response import CreateAtendenteResponseService
from src.infra.adapters.db_handler.idb_handler import IDbHandler
from src.domain.entities.atendente import Atendente
from src.infra.repositories.iatentende_repository import IAtendenteRepository


@dataclass
class CreateAtendenteService:
    @staticmethod
    def execute(db_conn: IDbHandler, repo: IAtendenteRepository, data: CreateAtendenteRequestService) -> CreateAtendenteResponseService:
        response = CreateAtendenteResponseService()
        new_atendente = Atendente(id=1, nome=data.nome, data_nascimento=data.data_nascimento, telefone1=data.telefone1, telefone2=data.telefone2, email=data.email)
        new_atendente.validade()

        atendente = repo.get_byemail(email=data.email)
        if atendente:
            response.msg = f"Já existe atendente cadastrado(a) com esse email '{new_atendente.email}.'"
            return response
        
        repo.add(new_atendente)
        db_conn.session.commit()
        response.id = new_atendente.id
        response.nome = new_atendente.nome
        response.data_nascimento = new_atendente.data_nascimento
        response.telefone1 = new_atendente.telefone1
        response.telefone2 = new_atendente.telefone2
        response.email = new_atendente.email
        return response
        
