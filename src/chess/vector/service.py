# chess/vector/service.py

"""
Module: chess.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from chess.vector import VectorBuilder, VectorValidator


class VectorService:
    """
    # ROLE: Service

    # RESPONSIBILITIES:
    An interface that provides access to a Vector object's state and methods without
    exposing the Vector directly.

    # PROVIDES:
        * VectorBuilder
        * VectorValidator
        * Vector exceptions

    # ATTRIBUTES:
      * vector_builder (VectorBuilder): Builds new Vector instances that meet
            the application's safety contract.
      * vector_validator (VectorValidator): Ensures an existing Vector will not raise an
            exception when used by a client.
    """
    
    _vector_builder: [VectorBuilder]
    _vector_validator: [VectorValidator]
    
    def __init__(
            self,
            vector_builder: type[VectorBuilder] = VectorBuilder,
            vector_validator: type[VectorValidator] = VectorValidator
    ):
        self._vector_builder = vector_builder
        self._vector_validator = vector_validator
    
    @property
    def vector_builder(self) -> type[VectorBuilder]:
        return self._vector_builder
    
    @property
    def vector_validator(self) -> type[VectorValidator]:
        return self._vector_validator