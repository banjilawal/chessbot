# src/chess/scalar/service/service.py

"""
Module: chess.scalar.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from chess.system import BuildResult, IntegrityService, ValidationResult
from chess.scalar import Scalar, ScalarBuilder, ScalarValidator


class ScalarIntegrityService(IntegrityService[Scalar]):
    """
    # ROLE: IntegrityService, Encapsulation, API layer.
    
    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for ScalarValidator and ScalarBuilder.
    2.  Protects Scalar objects from direct manipulation.
    3.  Extends behavior and functionality of Scalar objects.
    4.  Public facing API for Scalar modules.

    # PROVIDES:
        *   Scalar building
        *   Scalar validation

    # ATTRIBUTES:
        *   builder (ScalarBuilder)
        *   validator (ScalarValidator)
    """
    SERVICE_NAME = "ScalarIntegrityService"
    
    _item_builder: ScalarBuilder
    _item_validator: ScalarValidator
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: ScalarBuilder = ScalarBuilder(),
            validator: ScalarValidator = ScalarValidator()
    ):
        super().__init__(id=id, name=name)
        self._builder = builder
        self._validator = validator
    
    @property
    def item_validator(self) -> ScalarValidator:
        return self._validator
    
    def build(self, value: int) -> BuildResult[Scalar]:
        return self._builder.build(value, self._validator)
