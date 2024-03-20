from dataclasses import dataclass
from typing import Any

from src.domain.exceptions.domain_validation_error import DomainValidationError

@dataclass
class StringValidator:
    @staticmethod
    def validate(value: Any, field_name: str, exact_length: int = 0, min_length: int = 0, max_length: int = 0) -> None:
        DomainValidationError.when(isinstance(value, str) is False, f"{field_name} must be a string. [value={value}]")
        value = value.strip()

        DomainValidationError.when(len(value) == 0, f"{field_name} must not be empty.")

        if exact_length > 0:
            DomainValidationError.when(len(value) != exact_length, f"{field_name}'s length must be exactly {exact_length}. [value={value}]")
        else:
            DomainValidationError.when(min_length > 0 and len(value) < min_length, f'{field_name} minimum size is - {min_length}')
            DomainValidationError.when(max_length > 0 and len(value) > max_length, f'{field_name} maximum size is - {max_length}')