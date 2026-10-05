# src/assurance/depend/toolkit/struct/register/coord/toolkit.py

"""
Module: assurance.depend.toolkit.struct.register.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import RegisterValidatorToolkit, CoordRegisterDependency
from domain import (
    CoordRegister, CoordRegisterManifest, CoordRegisterNullGroup,
    CoordRegisterTypeUnion
)


class CoordRegisterValidatorToolkit(RegisterValidatorToolkit[CoordRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: CoordRegisterDependency
            metadata: CoordRegisterManifest

    Provides:

    Super Class:
       RegisterValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[CoordRegisterDependency] | None = None,
            metadata: Optional[CoordRegisterManifest] | None = None,
    ):
        """
            wrapper: Optional[CoordRegisterDependency]
            metadata: Optional[CoordRegisterManifest]
        """
        super().__init__(
            wrapper=wrapper or CoordRegisterDependency(),
            metadata=metadata or CoordRegisterManifest(),
        )
    
    @property
    def wrapper(self) -> CoordRegisterDependency:
        return cast(CoordRegisterDependency, super().wrapper)
    
    @property
    def metadata(self) -> CoordRegisterManifest:
        return cast(CoordRegisterManifest, super().metadata)
    
    @property
    def nulls(self) -> CoordRegisterNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> CoordRegisterTypeUnion:
        return self.metadata.types