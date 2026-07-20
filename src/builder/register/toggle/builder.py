# src/builder/register/toggle/builder.py

"""
Module: builder.register.toggle.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import RegisterBuilder
from register import VectorToggleRegister, Register
from result import BuildResult
from toggle import VectorToggle
from util import LoggingLevelRouter
from validator import VectorToggleValidator, VectorValidator


class VectorToggleRegisterBuilder(RegisterBuilder[VectorToggle]):
    """
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains VectorToggles passed to vector algebra.

    Attributes:
        a: VectorToggle
        b: VectorToggle
        endpoint_validator: Optional[VectorToggleValidator]

    Super Class:
        RegisterBuilder
    """
    
    def __init__(
            self,
            a: VectorToggle,
            b: VectorToggle,
            endpoint_validator: Optional[VectorToggleValidator] | None = VectorToggleValidator(),
    ):
        """
        Args:
            a: VectorToggle
            b: VectorToggle
            endpoint_validator: Optional[VectorToggleValidator]
        """
        super().__init__(a=a, b=b, endpoint_validator=endpoint_validator)
        
    @property
    def u(self) -> VectorToggle:
        return cast(VectorToggle, self.u)
    
    @property
    def v(self) -> VectorToggle:
        return cast(VectorToggle, self.v)
    
    @property
    def a(self) -> VectorToggle:
        return cast(VectorToggle, self.a)
    
    @property
    def b(self) -> VectorToggle:
        return cast(VectorToggle, self.b)
    
    @property
    def endpoint_validator(self) -> VectorToggleValidator:
        return cast(VectorToggleValidator, self.endpoint_validator)
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[VectorToggleRegister]:
        pass
        