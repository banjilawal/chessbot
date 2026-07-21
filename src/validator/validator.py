# src/validator/validator.py

"""
Module: validator.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from err.root import RootCertifier
from result import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T")


class Validator(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
        
    Naming Conventions:
        -   Workers are named <EntityName>Validator.
        -   Worker modules are named validator.
        -   Exception modules are named transaction.

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.
        
    Attributes:
    
    Provides:
        -   execute(candidate: Any) -> ValidationResult
        
    super Class:
    """
    _root_certifier: RootCertifier[T]
    
    def __init__(self, root_certifier: RootCertifier[[T]]):
        self._root_certifier = root_certifier
        
    @property
    def root_certifier(self) -> RootCertifier[T]:
        return self._root_certifier

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """Implement in subclass."""
        pass
