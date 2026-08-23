# src/assurance/checker/register/assurance/checker.py

"""
Module: assurance.checker.register/assurance/checker.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat.result import ValidationResult
from assurance.checker import Checker
from operation.toolkit import RegisterToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")


class RegisterChecker(Checker, Generic[T]):
    """
    Role
        -   Validator
        -   Integrity Assurance
        -   Consistency Assurance

    Responsibilities:
        1.  Runs integrity checks on an object or its blueprint before they are used.b
        3.  Pluggable validation module.

    Attributes:
        bundle: RegisterToolkit

    Provides:
        -   def execute(self, candidate: Any,) -> ValidationResult[T]

    Super Class:
        RootChecker
    """

    
    def __init__(self, bundle: RegisterToolkit[T]):
        super().__init__(bundle=bundle)
        
    @property
    def toolkit(self) -> RegisterToolkit[T]:
        return  cast(RegisterToolkit, super().bundle)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult[T]:
        pass
    
    
