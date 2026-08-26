# src/operation/suite/operation/toggle/vector/suite.py

"""
Module: operation.suite.operation.toggle.vector.suite
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import CartesianToggleValidator
from fabrication import VectorToggleBuilder
from kit import ToggleOperationSuite, VectorToggleToolkit
from domain.structure.toggle import CartesianToggle


class VectorToggleSuite(ToggleOperationSuite[CartesianToggle]):
    """
    Role:
        -  Dependency Container
        -  Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a VectorToggle.

    Attributes:
        toolkit: Optional[VectorToggleToolkit]
        builder: Optional[VectorToggleBuilder]
        validator: Optional[VectorToggleValidator]

    Provides:

    Super Class:
        ToggleOperationSuite
    """

    def __init__(
            self,
            toolkit: Optional[VectorToggleToolkit] | None = None,
            builder: Optional[VectorToggleBuilder] | None = None,
            validator: Optional[CartesianToggleValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[VectorToggleToolkit]
            builder: Optional[VectorToggleBuilder]
            validator: Optional[VectorToggleValidator]
        """
        super().__init__(
            toolkit=toolkit or VectorToggleToolkit(),
            builder=builder or VectorToggleBuilder(),
            validator=validator or CartesianToggleValidator(),
        )
    
    @property
    def toolkit(self) -> VectorToggleToolkit:
        return cast(VectorToggleToolkit, super().bundle)
    
    @property
    def builder(self) -> VectorToggleBuilder:
        return cast(VectorToggleBuilder, super().builder)
    
    @property
    def validator(self) -> CartesianToggleValidator:
        return cast(CartesianToggleValidator, super().validator)
    
