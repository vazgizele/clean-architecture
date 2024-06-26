from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Response
import uvicorn

from .db_config import DbConfig
from src.infra.adapters.db_handler.db_handler import DbHandler
from src.infra.ORM.mappers.start_mappers import start_mappers
from src.infra.repositories.atendente_repository import AtendenteRepository

from src.services.list_all_atendentes_service.implementation.list_atendente_service import ListAllAtendenteService
from src.services.inserted_atendente_service.DTO.create_atendente_request import CreateAtendenteRequestService
from src.services.update_atendente_service.implementation.update_atendente_service import UpdateAtendenteService
from src.services.get_atendente_service.implementation.get_atendente_service import GetAtendenteService
from src.services.delete_atendente_service.implementation.delete_atendente_service import DeleteAtendenteService
from src.services.inserted_atendente_service.implementation.create_atendente_service import CreateAtendenteService
from src.services.update_atendente_service.DTOs.update_atendente_request_service import UpdateAtendenteRequestService

from src.controllers.atendente.DTOs.create_atendente_response import CreateAtendenteResponse
from src.controllers.atendente.DTOs.create_atendente_request import CreateAtendenteRequest
from src.controllers.atendente.DTOs.get_atendente_response import GetAtendenteResponse
from src.controllers.atendente.DTOs.update_atendente_request import UpdateAtendenteRequest

app = FastAPI(title='webapp_settings.title', 
              version='webapp_settings.version',
              debug=True)

db_config = DbConfig()

def create_db() ->DbHandler:
    return DbHandler(db_path=db_config.db_path, db_timeout=db_config.db_timeout)

def execute_webapp():
    load_dotenv()
    start_mappers()
    uvicorn.run(app, host='127.0.0.1', port=8000)

@app.get("/api/atendendes/{id}",  response_model=GetAtendenteResponse, status_code=200)
async def get_atendente(id: int):
    with create_db() as db_conn:
        repo = AtendenteRepository(db_conn)
        atendente = GetAtendenteService.execute(db_conn,repo,id)
        if not atendente:
            raise HTTPException(status_code=404, detail=f'Atendente não existe. [Id={id}]')
    return GetAtendenteResponse(id=atendente.id, nome=atendente.nome, data_nascimento=atendente.data_nascimento, telefone1=atendente.telefone1, telefone2=atendente.telefone2, email=atendente.email)

@app.get("/api/atendendes", response_model=List[GetAtendenteResponse], status_code=200)
async def get_all_atendentes():
    ret = []
    
    with create_db() as db_conn:
        repo = AtendenteRepository(db_conn)
        for data in ListAllAtendenteService.execute(db_conn,repo):
            ret.append(GetAtendenteResponse(id=data.id, nome=data.nome, data_nascimento=data.data_nascimento, telefone1=data.telefone1, telefone2=data.telefone2, email=data.email))
        
    return ret

@app.post("/api/atendentes", response_model=CreateAtendenteResponse, status_code=201)
async def new_atendente(create_atendente_request: CreateAtendenteRequest):
    if not isinstance(create_atendente_request.nome, str):
        raise HTTPException(status_code=400, detail="O campo 'nome' não pode ser vazio.")
   
    with create_db() as db_conn:
        new_atendente = CreateAtendenteRequestService(nome=create_atendente_request.nome, data_nascimento=create_atendente_request.data_nascimento, telefone1=create_atendente_request.telefone1, telefone2=create_atendente_request.telefone2, email=create_atendente_request.email)
        repo = AtendenteRepository(db_conn)
        atendente_service_response = CreateAtendenteService().execute(db_conn, repo, new_atendente)
        if atendente_service_response.msg != 'OK':
            raise HTTPException(status_code=400, detail=atendente_service_response.msg)
       
        return CreateAtendenteResponse(id=atendente_service_response.id, nome=atendente_service_response.nome, data_nascimento=atendente_service_response.data_nascimento, telefone1=atendente_service_response.telefone1, telefone2=atendente_service_response.telefone2, email=atendente_service_response.email)
    
@app.delete("/api/atendentes/{id}")
async def delete_atendente(id: int):
    with create_db() as db_conn:
      repo = AtendenteRepository(db_conn)
      msg = DeleteAtendenteService().execute(db_conn, repo, id)
 
      if msg != 'OK':
          raise HTTPException(status_code=404, detail=msg)
     
      db_conn.session.commit()
    return Response(status_code=204)
     
@app.put("/api/atendentes/{id}")
async def update_atendente(id: int, update_atendente_request: UpdateAtendenteRequest):
    with create_db() as db_conn:

        atendente_data = UpdateAtendenteRequestService(nome=update_atendente_request.nome, data_nascimento=update_atendente_request.data_nascimento, telefone1=update_atendente_request.telefone1, telefone2=update_atendente_request.telefone2, email=update_atendente_request.email)

        repo = AtendenteRepository(db_conn)
        msg = UpdateAtendenteService().execute(db_conn, repo, atendente_data, id)
 
        if msg != "OK":
            raise HTTPException(status_code=404, detail=msg)
       
        db_conn.session.commit()
   
    return Response(status_code=204)