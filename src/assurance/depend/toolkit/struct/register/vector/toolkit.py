# src/assurance/depend/toolkit/struct/register/vector/toolkit.py

"""
Module: assurance.depend.toolkit.struct.register.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import RegisterValidatorToolkit, VectorRegisterDependency
from domain import (
    VectorRegister, VectorRegisterManifest, VectorRegisterNullGroup,
    VectorRegisterTypeUnion
)


class VectorRegisterValidatorToolkit(RegisterValidatorToolkit[VectorRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: VectorRegisterDependency
            metadata: VectorRegisterManifest

    Provides:

    Super Class:
       RegisterValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[VectorRegisterDependency] | None = None,
            metadata: Optional[VectorRegisterManifest] | None = None,
    ):
        """
            wrapper: Optional[VectorRegisterDependency]
            metadata: Optional[VectorRegisterManifest]
        """
        super().__init__(
            wrapper=wrapper or VectorRegisterDependency(),
            metadata=metadata or VectorRegisterManifest(),
        )
    
    @property
    def wrapper(self) -> VectorRegisterDependency:
        return cast(VectorRegisterDependency, super().wrapper)
    
    @property
    def metadata(self) -> VectorRegisterManifest:
        return cast(VectorRegisterManifest, super().metadata)
    
    @property
    def nulls(self) -> VectorRegisterNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> VectorRegisterTypeUnion:
        return self.metadata.types