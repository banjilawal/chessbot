# src/chess/scalar/service/service.py

"""
Module: chess.scalar.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import Any

from chess.system import BuildResult, Service, ValidationResult
from chess.scalar import Scalar, ScalarBuilder, ScalarValidator



class ScalarService(Service):
    """
    # ROLE: Service

    # RESPONSIBILITIES:
    An interface that provides access to a Scalar object's state and methods without
    exposing the Scalar directly.

    # PROVIDES:
        * ScalarBuilder
        * ScalarValidator
        * Scalar exceptions

    # ATTRIBUTES:
        *   scalar_builder (ScalarBuilder):     Builds new Scalar instances that meet the application's
                                                safety contract.
                                                
        * scalar_validator (ScalarValidator):   Validates candidates are Scalar objects complying with
                                                safety contracts.
    """
    SERVICE_NAME = "ScalarService"
    _scalar_builder: type[ScalarBuilder]
    _scalar_validator: type[ScalarValidator]
    
    def __init__(
            self,
            int: id,
            name: str = SERVICE_NAME,
            scalar_builder: type[ScalarBuilder]=ScalarBuilder,
            scalar_validator: type[ScalarValidator]=ScalarValidator
    ):
        super().__init__(id=id, name=name)
        self._scalar_builder = scalar_builder
        self._scalar_validator = scalar_validator
    
    @property
    def validator(self) -> type[ScalarValidator]:
        return self._scalar_validator
    
    def build_scalar(self, value: int) -> BuildResult[Scalar]:
        return self._scalar_builder.build(value)