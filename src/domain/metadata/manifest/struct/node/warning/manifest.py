# src/domain/metadata/manifest/struct/node/warning/manifest.py

"""
Module: domain.metadata.manifest.struct.node.warning.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    NodeManifest, EncounterWarningNode, EncounterWarningNodeNullWarningSet,
    EncounterWarningNodeLayer
)


class EncounterWarningNodeManifest(NodeManifest[EncounterWarningNode]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the EncounterWarningNode
            security lifecycle.

     Attributes:
        types: EncounterWarningNodeTypeUnion
        nulls: EncounterWarningNodeNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[EncounterWarningNodeLayer] | None = None,
            nulls: Optional[EncounterWarningNodeNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[EncounterWarningNodeTypeUnion]
            nulls: Optional[EncounterWarningNodeNullGroup]
        """
        super().__init__(
            types=types or EncounterWarningNodeLayer(),
            nulls=nulls or EncounterWarningNodeNullWarningSet(),
        )

        
    @property
    def types(self) -> EncounterWarningNodeLayer:
        return cast(EncounterWarningNodeLayer, super().types)
    
    @property
    def nulls(self) -> EncounterWarningNodeNullWarningSet:
        return cast(EncounterWarningNodeNullWarningSet, super().nulls)