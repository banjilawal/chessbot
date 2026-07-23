# src/certifier/certifier.py

"""
Module: certifier.certifier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from blueprint import Blueprint
from result import ValidationResult
from root import EntityCarrierValidator
from toolkit import Toolkit
from util import LoggingLevelRouter

T = TypeVar("T",)


class RootCertifier(ABC, Generic[T]):
    """
    Role
        -   Validator
        -   Integrity Assurance
        -   Consistency Assurance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        toolkit: Toolkit

    Provides:
        -   def validate(candidate: Any, toolkit: Toolkit,) -> ValidationResult[Blueprint[T]]:

    Super Class:
    """
    _toolkit: Toolkit
    _carrier_validator: EntityCarrierValidator
    
    def __init__(
            self,
            toolkit: Toolkit,
            carrier_validator: Optional[EntityCarrierValidator] | None = EntityCarrierValidator()
    ):
        """
        Args:
            toolkit: Toolkit,
            carrier_validator: Optional[EntityCarrierValidator]
        """
        self._toolkit = toolkit
        self._carrier_validator = carrier_validator
        
    @property
    def toolkit(self) -> Toolkit:
        return self._toolkit
    
    @property
    def carrier_validator(self) -> EntityCarrierValidator:
        return self._carrier_validator
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[Blueprint[T]]:
        pass
    
    
