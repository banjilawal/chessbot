# src/domain/metadata/manifest/strcture/node/warning/manifest.py

"""
Module: domain.metadata.manifest.struct.node.warning.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    NodeManifest, EncounterWarningNode, EncounterWarningNodeNullGroup,
    EncounterWarningNodeTypeUnion
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
            types: Optional[EncounterWarningNodeTypeUnion] | None = None,
            nulls: Optional[EncounterWarningNodeNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[EncounterWarningNodeTypeUnion]
            nulls: Optional[EncounterWarningNodeNullGroup]
        """
        super().__init__(
            types=types or EncounterWarningNodeTypeUnion(),
            nulls=nulls or EncounterWarningNodeNullGroup(),
        )

        
    @property
    def types(self) -> EncounterWarningNodeTypeUnion:
        return cast(EncounterWarningNodeTypeUnion, super().types)
    
    @property
    def nulls(self) -> EncounterWarningNodeNullGroup:
        return cast(EncounterWarningNodeNullGroup, super().nulls)