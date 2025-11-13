# chess/scalar/service.py

"""
Module: chess.scalar.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""


from chess.scalar import ScalarBuilder, ScalarValidator


class ScalarService:
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
      * scalar_builder (ScalarBuilder): Builds new Scalar instances that meet
            the application's safety contract.
      * scalar_validator (ScalarValidator): Validates existing Scalar instances that meet
            the application's safety contract.
    """
    
    _scalar_builder: [ScalarBuilder]
    _scalar_validator: [ScalarValidator]
    
    def __init__(
            self,
            scalar_builder: type[ScalarBuilder]=ScalarBuilder,
            scalar_validator: type[ScalarValidator]=ScalarValidator
    ):
        self._scalar_builder = scalar_builder
        self._scalar_validator = scalar_validator
        
    @property
    def scalar_builder(self) -> type[ScalarBuilder]:
        return self._scalar_builder
    
    @property
    def scalar_validator(self) -> type[ScalarValidator]:
        return self._scalar_validator