# src/production/endpoint/authorization/checker.py

"""
Module: production.endpoint.authorization.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from exchange import ValidationService

T = TypeVar("T")

class Checker(ABC, Generic[T]):
    _validation_service: ValidationService[T]
    
    def __init__(self, validation_service: ValidationService[T]):
        self._validation_service = validation_service
        
    @property
    def validation_service(self) -> ValidationService:
        return self._validation_service
    
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass