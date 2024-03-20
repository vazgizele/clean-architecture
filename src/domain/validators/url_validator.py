import re
from typing import Any
from src.domain.exceptions.domain_validation_error import DomainValidationError

class UrlValidator:
    @staticmethod
    def validate(value: Any, field_name: str)->None:
        DomainValidationError.when(value is None, "invalid Url. [value=]")
        DomainValidationError.when(isinstance(value, str) is False, f"{field_name} must be a string. [value={value}]")
        value = value.strip()

        url_regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"# checar se o regex tá no formato que Sérgio quer
        resultado = re.match(url_regex,value)
        DomainValidationError.when(resultado == None, f"{field_name} must be in format [https://www.example.com], [value={value}]") # checar com Sérgio essa mensagem de erro