# src/suite/operation/vector/suite.py

"""
Module: suite.operation.vector.suite
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import VectorValidator
from fabrication import VectorBuilder
from kit import OperationSuite, VectorToolkit
from model import Vector


class VectorOperationSuite(OperationSuite[Vector]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Vector.

    Attributes:
        toolkit: Optional[VectorToolkit]
        builder: Optional[VectorBuilder]
        validator: Optional[VectorValidator]

    Provides:

    Super Class:
        OperationSuite

    Notes:
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    
    def __init__(
            self,
            toolkit: Optional[VectorToolkit] | None = None,
            builder: Optional[VectorBuilder] | None = None,
            validator: Optional[VectorValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[VectorToolkit]
            builder: Optional[VectorBuilder]
            validator: Optional[VectorValidator]
        """
        super().__init__(
            toolkit=toolkit or VectorToolkit(),
            builder=builder or VectorBuilder(),
            validator=validator or VectorValidator(),
        )
    
    @property
    def toolkit(self) -> VectorToolkit:
        return cast(VectorToolkit, super().bundle)
    
    @property
    def builder(self) -> VectorBuilder:
        return cast(VectorBuilder, super().builder)
    
    @property
    def validator(self) -> VectorValidator:
        return cast(VectorValidator, super().validator)


