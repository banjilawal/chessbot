# src/suite/operation/toggle/vector/suite.py

"""
Module: suite.operation.toggle.vector.suite
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import VectorToggleValidator
from fabrication import VectorToggleBuilder
from kit import ToggleOperationSuite, VectorToggleToolkit
from domain.toggle import VectorToggle


class VectorToggleSuite(ToggleOperationSuite[VectorToggle]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

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
            validator: Optional[VectorToggleValidator] | None = None,
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
            validator=validator or VectorToggleValidator(),
        )
    
    @property
    def toolkit(self) -> VectorToggleToolkit:
        return cast(VectorToggleToolkit, super().bundle)
    
    @property
    def builder(self) -> VectorToggleBuilder:
        return cast(VectorToggleBuilder, super().builder)
    
    @property
    def validator(self) -> VectorToggleValidator:
        return cast(VectorToggleValidator, super().validator)
    
