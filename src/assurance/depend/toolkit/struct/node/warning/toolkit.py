# src/assurance/depend/toolkit/struct/node/warning/toolkit.py

"""
Module: assurance.depend.toolkit.struct.node.warning.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import NodeLayerToolkit, EncounterWarningNodeDependency
from domain import (
    EncounterWarningNode, EncounterWarningNodeManifest, EncounterWarningNodeNullWarningSet,
    EncounterWarningNodeLayer
)


class EncounterWarningNodeLayerToolkit(NodeLayerToolkit[EncounterWarningNode]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: EncounterWarningNodeDependency
            manifest: EncounterWarningNodeManifest

    Provides:

    Super Class:
       NodeLayerToolkit
    """
    
    def __init__(
            self,
            dependency: Optional[EncounterWarningNodeDependency] | None = None,
            manifest: Optional[EncounterWarningNodeManifest] | None = None,
    ):
        """
            wrapper: Optional[EncounterWarningNodeDependency]
            manifest: Optional[EncounterWarningNodeManifest]
        """
        super().__init__(
            dependency=dependency or EncounterWarningNodeDependency(),
            manifest=manifest or EncounterWarningNodeManifest(),
        )
    
    @property
    def dependency(self) -> EncounterWarningNodeDependency:
        return cast(EncounterWarningNodeDependency, super().dependency)
    
    @property
    def manifest(self) -> EncounterWarningNodeManifest:
        return cast(EncounterWarningNodeManifest, super().manifest)
    
    @property
    def nulls(self) -> EncounterWarningNodeNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> EncounterWarningNodeLayer:
        return self.manifest.types