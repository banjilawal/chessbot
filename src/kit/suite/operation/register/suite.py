# src/kit/suite/operation/register/suite.py

"""
Module: kit.suite.operation.register.suite
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from assurance import RegisterValidator
from fabrication import RegisterBuilder
from kit import OperationSuite, RegisterToolkit

T = TypeVar("T", bound="Register")


class RegisterOperationSuite(OperationSuite, Generic[T]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Register.

    Attributes:
        toolkit: RegisterToolkit[T]
        builder: RegisterBuilder[T]
        validator: RegisterValidator[T]

    Provides:

    Super Class:
        OperationSuite
    """
    
    def __init__(
            self,
            toolkit: RegisterToolkit[T],
            builder: RegisterBuilder[T],
            validator: RegisterValidator[T],
    ):
        """
        Args:
            toolkit: RegisterToolkit[T]
            builder: RegisterBuilder[T]
            validator: RegisterValidator[T]
        """
        super().__init__(toolkit=toolkit, builder=builder, validator=validator)
    
    @property
    def toolkit(self) -> RegisterToolkit[T]:
        return cast(RegisterToolkit[T], super().toolkit)
    
    @property
    def builder(self) -> RegisterBuilder[T]:
        return cast(RegisterBuilder[T], super().builder)
    
    @property
    def validator(self) -> RegisterValidator[T]:
        return cast(RegisterValidator[T], super().validator)

    