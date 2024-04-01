from dataclasses import dataclass
from datetime import date
from typing import Optional
from pydantic import BaseModel


@dataclass
class CreateAtendenteRequest(BaseModel):
    nome: str
    data_nascimento: date
    telefone1: str
    telefone2: Optional[str] = None
    email: str