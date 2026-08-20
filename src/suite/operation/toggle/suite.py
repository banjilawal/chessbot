# src/suite/operation/toggle/suite.py

"""
Module: suite.operation.toggle.suite
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from assurance import ToggleValidator
from fabrication import ToggleBuilder
from kit import OperationSuite, ToggleToolkit


T = TypeVar("T", bound="Toggle")

class ToggleOperationSuite(OperationSuite, Generic[T]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Toggle.

    Attributes:
        toolkit: ToggleToolkit[T]
        builder: ToggleBuilder[T]
        validator: ToggleValidator[T]

    Provides:

    Super Class:
        OperationSuite
    """
    
    def __init__(
            self,
            toolkit: ToggleToolkit[T],
            builder: ToggleBuilder[T],
            validator: ToggleValidator[T],
    ):
        """
        Args:
            toolkit: ToggleToolkit[T]
            builder: ToggleBuilder[T]
            validator: ToggleValidator[T]
        """
        super().__init__(toolkit=toolkit, builder=builder, validator=validator)
    
    @property
    def toolkit(self) -> ToggleToolkit[T]:
        return cast(ToggleToolkit[T], super().bundle)
    
    @property
    def builder(self) -> ToggleBuilder[T]:
        return cast(ToggleBuilder[T], super().builder)
    
    @property
    def validator(self) -> ToggleValidator[T]:
        return cast(ToggleValidator[T], super().validator)



    