from dataclasses import dataclass
from datetime import date

from src.domain.validators.int_validator import IntValidator


@dataclass
class Atendente:
    id: int
    nome: str
    data_nascimento: date
    telefone1: str
    telefone2: str
    email: str

    def validade(self):
        IntValidator.validate(value=self.id, field_name="id")