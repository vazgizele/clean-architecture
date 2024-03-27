from dataclasses import dataclass
from datetime import date
from src.domain.validators.string_validator import StringValidator
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
        StringValidator.validate(value=self.nome, field_name="nome", exact_length=0, min_length=3, max_length=30)