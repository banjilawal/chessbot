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
from authorization import Checker
from domain import Actor
from exchange import ValidationService

T = TypeVar("T", bound="Actor")

class PrincipalChecker(Checker[T], ABC, Generic[T]):
    
    def __init__(self, validation_service: ValidationService[T]):
        super().__init__(validation_service=validation_service)
    
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass