# src/assurance/depend/toolkit/struct/register/square/toolkit.py

"""
Module: assurance.depend.toolkit.struct.register.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import RegisterLayerToolkit, SquareRegisterDependency
from domain import (
    SquareRegister, SquareRegisterManifest, SquareRegisterNullWarningSet,
    SquareRegisterLayer
)


class SquareRegisterLayerToolkit(RegisterLayerToolkit[SquareRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: SquareRegisterDependency
            manifest: SquareRegisterManifest

    Provides:

    Super Class:
       RegisterLayerToolkit
    """
    
    def __init__(
            self,
            dependency: Optional[SquareRegisterDependency] | None = None,
            manifest: Optional[SquareRegisterManifest] | None = None,
    ):
        """
            wrapper: Optional[SquareRegisterDependency]
            manifest: Optional[SquareRegisterManifest]
        """
        super().__init__(
            dependency=dependency or SquareRegisterDependency(),
            manifest=manifest or SquareRegisterManifest(),
        )
    
    @property
    def dependency(self) -> SquareRegisterDependency:
        return cast(SquareRegisterDependency, super().dependency)
    
    @property
    def manifest(self) -> SquareRegisterManifest:
        return cast(SquareRegisterManifest, super().manifest)
    
    @property
    def nulls(self) -> SquareRegisterNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> SquareRegisterLayer:
        return self.manifest.types