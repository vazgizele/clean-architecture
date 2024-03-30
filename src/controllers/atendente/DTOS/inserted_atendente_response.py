from dataclasses import dataclass
from datetime import date


@dataclass
class InsertedAtendenteResponse:
    id: int
    nome: str
    data_nascimento: date
    telefone1: str
    telefone2: str
    email: str