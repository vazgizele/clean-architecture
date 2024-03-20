import re
from typing import Any

from src.domain.exceptions.domain_validation_error import DomainValidationError

class PhoneValidator:
    @staticmethod
    def validate(value: Any, field_name: str):

        DomainValidationError.when(isinstance(value, str) is False, f"{field_name} must be a string. [value={value}]")
        value = value.strip()

        regex = "^\\+?[1-9][0-9]{8,11}$"
        test = re.match(regex, value)
        DomainValidationError.when(test == None, f"{field_name} must be in format [123456789], [value={value}]") # checar com Sérgio essa mensagem de erro
