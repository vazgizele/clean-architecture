from dataclasses import dataclass
from typing import Any
from src.domain.exceptions.domain_validation_error import DomainValidationError

@dataclass
class IntValidator:
    @staticmethod
    def validate(value: int, field_name: str) -> None:
        DomainValidationError.when(isinstance(value, int) is False, f"{field_name} must be a integer. [value={value}]")

        DomainValidationError.when(value < 0, f"{field_name} must be a positive integer. [value={value}]")
