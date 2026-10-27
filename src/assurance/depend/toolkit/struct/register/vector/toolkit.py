# src/assurance/depend/toolkit/struct/register/vector/toolkit.py

"""
Module: assurance.depend.toolkit.struct.register.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import RegisterLayerToolkit, VectorRegisterDependency
from domain import (
    VectorRegister, VectorRegisterManifest, VectorRegisterNullWarningSet,
    VectorRegisterLayer
)


class VectorRegisterLayerToolkit(RegisterLayerToolkit[VectorRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: VectorRegisterDependency
            manifest: VectorRegisterManifest

    Provides:

    Super Class:
       RegisterLayerToolkit
    """
    
    def __init__(
            self,
            dependency: Optional[VectorRegisterDependency] | None = None,
            manifest: Optional[VectorRegisterManifest] | None = None,
    ):
        """
            wrapper: Optional[VectorRegisterDependency]
            manifest: Optional[VectorRegisterManifest]
        """
        super().__init__(
            dependency=dependency or VectorRegisterDependency(),
            manifest=manifest or VectorRegisterManifest(),
        )
    
    @property
    def dependency(self) -> VectorRegisterDependency:
        return cast(VectorRegisterDependency, super().dependency)
    
    @property
    def manifest(self) -> VectorRegisterManifest:
        return cast(VectorRegisterManifest, super().manifest)
    
    @property
    def nulls(self) -> VectorRegisterNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> VectorRegisterLayer:
        return self.manifest.types