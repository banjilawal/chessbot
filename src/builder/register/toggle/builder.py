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
            endpoint_validator: Optional[VectorToggleValidator] | None = VectorToggleValidator(),
    ):
        """
        Args:
            endpoint_validator: Optional[VectorToggleValidator]
        """
        super().__init__(endpoint_validator=endpoint_validator)

    
    @property
    def endpoint_validator(self) -> VectorToggleValidator:
        return cast(VectorToggleValidator, self.endpoint_validator)
    
    @LoggingLevelRouter.monitor
    def execute(
            u: VectorToggle,
            v: VectorToggle,
    ) -> BuildResult[VectorToggleRegister]:
        pass
        