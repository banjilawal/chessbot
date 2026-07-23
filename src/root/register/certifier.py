# src/certifier/validator.py

"""
Module: certifier.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar


from result import ValidationResult
from toolkit import RegisterToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")


class RegisterRootCertifier(ABC, Generic[T]):
    """
    Role
        -   Validator
        -   Integrity Assurance
        -   Consistency Assurance

    Responsibilities:
        1.  Runs integrity checks on an object or its blueprint before they are used.b
        3.  Pluggable validation module.

    Attributes:
        toolkit: RegisterToolkit

    Provides:
        -   def validate(candidate: Any, toolkit: RegisterToolkit[T],) -> ValidationResult[Blueprint[T]]:

    Super Class:
    """

    
    def __init__(self, toolkit: RegisterToolkit[T]):
        super().__init__(toolkit=toolkit)
        
    @property
    @abstractmethod
    def toolkit(self) -> RegisterToolkit[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        pass
    
    
