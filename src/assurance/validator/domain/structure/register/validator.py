# src/assurance/validator/structure/register/assurance/validator.py

"""
Module: assurance.validator.register/assurance/validator.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance.validator import Validator
from operation.toolkit import RegisterToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")


class RegisterValidator(Validator, Generic[T]):
    """
    Role
        - Validator
        - Integrity Assurance
        - Consistency Assurance

    Responsibilities:
        1.  Runs integrity checks on an object or its blueprint before they are used.b
        3.  Pluggable validation module.

    Attributes:
        toolkit: RegisterToolkit

    Provides:
        - def execute(self, candidate: Any,) -> ValidationResult[T]

    Super Class:
        RootValidator
    """

    
    def __init__(self, toolkit: RegisterToolkit[T]):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> RegisterToolkit[T]:
        return  cast(RegisterToolkit, super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult[T]:
        pass
    
    
