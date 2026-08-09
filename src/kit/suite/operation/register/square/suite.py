# src/kit/suite/operation/register/vector/suite.py

"""
Module: kit.suite.operation.register.vector.suite
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication import SquareRegisterBuilder
from kit import RegisterOperationSuite, SquareRegisterToolkit
from register import SquareRegister


class SquareRegisterSuite(RegisterOperationSuite[SquareRegister]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a SquareRegister.

    Attributes:
        toolkit: Optional[SquareRegisterToolkit]
        builder: Optional[SquareRegisterBuilder]
        validator: Optional[SquareRegisterValidator]

    Provides:

    Super Class:
        RegisterOperationSuite
    """
    
    def __init__(
            self,
            toolkit: Optional[SquareRegisterToolkit] | None = None,
            builder: Optional[SquareRegisterBuilder] | None = None,
            validator: Optional[SquareRegisterValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[SquareRegisterToolkit]
            builder: Optional[SquareRegisterBuilder]
            validator: Optional[SquareRegisterValidator]
        """
        super().__init__(
            toolkit=toolkit or SquareRegisterToolkit(),
            builder=builder or SquareRegisterBuilder(),
            validator=validator or SquareRegisterValidator(),
        )
    
    @property
    def toolkit(self) -> SquareRegisterToolkit:
        return cast(SquareRegisterToolkit, super().toolkit)
    
    @property
    def builder(self) -> SquareRegisterBuilder:
        return cast(SquareRegisterBuilder, super().builder)
    
    @property
    def validator(self) -> SquareRegisterValidator:
        return cast(SquareRegisterValidator, super().validator)
    
