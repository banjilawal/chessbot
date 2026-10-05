# src/assurance/depend/toolkit/struct/register/square/toolkit.py

"""
Module: assurance.depend.toolkit.struct.register.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import RegisterValidatorToolkit, SquareRegisterDependency
from domain import (
    SquareRegister, SquareRegisterManifest, SquareRegisterNullGroup,
    SquareRegisterTypeUnion
)


class SquareRegisterValidatorToolkit(RegisterValidatorToolkit[SquareRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: SquareRegisterDependency
            metadata: SquareRegisterManifest

    Provides:

    Super Class:
       RegisterValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[SquareRegisterDependency] | None = None,
            metadata: Optional[SquareRegisterManifest] | None = None,
    ):
        """
            wrapper: Optional[SquareRegisterDependency]
            metadata: Optional[SquareRegisterManifest]
        """
        super().__init__(
            wrapper=wrapper or SquareRegisterDependency(),
            metadata=metadata or SquareRegisterManifest(),
        )
    
    @property
    def wrapper(self) -> SquareRegisterDependency:
        return cast(SquareRegisterDependency, super().wrapper)
    
    @property
    def metadata(self) -> SquareRegisterManifest:
        return cast(SquareRegisterManifest, super().metadata)
    
    @property
    def nulls(self) -> SquareRegisterNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> SquareRegisterTypeUnion:
        return self.metadata.types