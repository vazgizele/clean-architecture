from sqlalchemy import BigInteger, Column, Identity, Table, VARCHAR, String, DATE
from sqlalchemy.exc import ArgumentError

from src.domain.entities.atendente import Atendente


def atentende_mapper(mapper):
    atendente_schema = Table(
        'tb_atendente_gizele',
        mapper.metadata,
        Column('id', BigInteger, Identity(start=1),primary_key=True, autoincrement=True),
        Column('nome', String(50), nullable=False),
        Column('data_nascimento', DATE, nullable=False),
        Column('telefone1', String(11)),
        Column('telefone2', String(11)),
        Column('email', VARCHAR(100), nullable=False),
        schema="academy"
    )
    
    try:
        mapper.map_imperatively(Atendente, atendente_schema)
    except ArgumentError:
        return "Ocorreu um erro"