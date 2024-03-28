from dataclasses import dataclass
from typing import Any
from datetime import date

from src.domain.exceptions.domain_validation_error import DomainValidationError

@dataclass
class DateValidator:
    @staticmethod
    def validate(value: Any, field_name: str):
        DomainValidationError.when(isinstance(value, date) is False, f"{field_name} must be a date. [value={value}]")