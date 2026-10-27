# src/assurance/depend/toolkit/struct/register/coord/toolkit.py

"""
Module: assurance.depend.toolkit.struct.register.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import RegisterLayerToolkit, CoordRegisterDependency
from domain import (
    CoordRegister, CoordRegisterManifest, CoordRegisterNullWarningSet,
    CoordRegisterLayer
)


class CoordRegisterLayerToolkit(RegisterLayerToolkit[CoordRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: CoordRegisterDependency
            manifest: CoordRegisterManifest

    Provides:

    Super Class:
       RegisterLayerToolkit
    """
    
    def __init__(
            self,
            dependency: Optional[CoordRegisterDependency] | None = None,
            manifest: Optional[CoordRegisterManifest] | None = None,
    ):
        """
            wrapper: Optional[CoordRegisterDependency]
            manifest: Optional[CoordRegisterManifest]
        """
        super().__init__(
            dependency=dependency or CoordRegisterDependency(),
            manifest=manifest or CoordRegisterManifest(),
        )
    
    @property
    def dependency(self) -> CoordRegisterDependency:
        return cast(CoordRegisterDependency, super().dependency)
    
    @property
    def manifest(self) -> CoordRegisterManifest:
        return cast(CoordRegisterManifest, super().manifest)
    
    @property
    def nulls(self) -> CoordRegisterNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> CoordRegisterLayer:
        return self.manifest.types