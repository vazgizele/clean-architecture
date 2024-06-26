from dataclasses import dataclass
from datetime import date
from typing import Optional
from src.domain.validators.email_validator import EmailValidator
from src.domain.validators.phone_validator import PhoneValidator
from src.domain.validators.date_validator import DateValidator
from src.domain.validators.string_validator import StringValidator
from src.domain.validators.int_validator import IntValidator

@dataclass
class Atendente:
    id: int =0
    nome: str =''
    data_nascimento: date = date.today()
    telefone1: str = ''
    telefone2: Optional[str] = None
    email: str = ''

    def validade(self):
        IntValidator.validate(value=self.id, field_name="id")
        StringValidator.validate(value=self.nome, field_name="nome", exact_length=0, min_length=3, max_length=30)
        self.nome = self.nome.strip()

        DateValidator.validate(value=self.data_nascimento, field_name="data_nascimento")
        PhoneValidator.validate(value=self.telefone1, field_name="telefone1")
        
        if self.telefone2 != None:
            PhoneValidator.validate(value=self.telefone1, field_name="telefone2")

        EmailValidator.validate(value=self.email, field_name="email")