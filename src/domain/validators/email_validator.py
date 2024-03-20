import re
from typing import Any

from src.domain.exceptions.domain_validation_error import DomainValidationError

class EmailValidator:
    @staticmethod
    def validate(value: Any, field_name: str):
        DomainValidationError.when(value is None, "invalid E-mail. [value=]")
        DomainValidationError.when(isinstance(value, str) is False, f"{field_name} must be a string. [value={value}]")
        value = value.strip()

        email_regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
        email_validator = re.findall(email_regex,value)
        DomainValidationError.when(value not in email_validator, f"{field_name} must be in format [User@Domain.com.br[br=Optional], [value={value}]") # checar com Sérgio essa mensagem de erro
