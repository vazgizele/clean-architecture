from sqlalchemy import MetaData
from sqlalchemy.orm import registry

from src.infra.ORM.mappers.mapper_atendente import atentende_mapper

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

def start_mappers():
    atentende_mapper(mapper_registry)