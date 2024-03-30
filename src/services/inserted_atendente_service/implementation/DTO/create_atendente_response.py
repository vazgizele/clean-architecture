from dataclasses import dataclass
from datetime import date


@dataclass
class CreateAtendenteResponseService():
    msg: str = 'OK'
    id: int = 0
    nome: str = ''
    data_nascimento: date = ''
    telefone1: str = ''
    telefone2: str = ''
    email: str = ''