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
from fabrication import CartesianToggleBuilder
from kit import ToggleOperationSuite, CartesianToggleToolkit
from domain.structure.toggle import CartesianToggle


class CartesianToggleSuite(ToggleOperationSuite[CartesianToggle]):
    """
    Role:
        - Dependency Container
        -  Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a CartesianToggle.

    Attributes:
        toolkit: Optional[CartesianToggleToolkit]
        builder: Optional[CartesianToggleBuilder]
        validator: Optional[CartesianToggleValidator]

    Provides:

    Super Class:
        ToggleOperationSuite
    """

    def __init__(
            self,
            toolkit: Optional[CartesianToggleToolkit] | None = None,
            builder: Optional[CartesianToggleBuilder] | None = None,
            validator: Optional[CartesianToggleValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[CartesianToggleToolkit]
            builder: Optional[CartesianToggleBuilder]
            validator: Optional[CartesianToggleValidator]
        """
        super().__init__(
            toolkit=toolkit or CartesianToggleToolkit(),
            builder=builder or CartesianToggleBuilder(),
            validator=validator or CartesianToggleValidator(),
        )
    
    @property
    def toolkit(self) -> CartesianToggleToolkit:
        return cast(CartesianToggleToolkit, super().bundle)
    
    @property
    def builder(self) -> CartesianToggleBuilder:
        return cast(CartesianToggleBuilder, super().builder)
    
    @property
    def validator(self) -> CartesianToggleValidator:
        return cast(CartesianToggleValidator, super().validator)
    
