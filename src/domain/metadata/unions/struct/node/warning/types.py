# src/domain/metadata/unions/strcture/node/warning/manifest.py

"""
Module: domain.metadata.unions.struct.node.warning.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import EncounterWarningNode, EncounterWarningNodeBlueprint, NodeTypeUnion 

class EncounterWarningNodeTypeUnion(NodeTypeUnion[EncounterWarningNode]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a EncounterWarningNode.

    Attributes:
        model: Type[EncounterWarningNode]
        carrier: Type[EncounterWarningNodeCarrier]
        blueprint: Type[EncounterWarningNodeBlueprint]
        
    Provides:

    Super Class:
        EncounterWarningNodeTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EncounterWarningNodeCarrier],
            model: Optional[Type[EncounterWarningNode]] | None = None,
            blueprint: Optional[Type[EncounterWarningNodeBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[EncounterWarningNode]
            carrier: Type[EncounterWarningNodeCarrier]
            blueprint: Type[EncounterWarningNodeBlueprint]
        """
        super().__init__(
            model=model or EncounterWarningNode,
            blueprint=blueprint or EncounterWarningNodeBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[EncounterWarningNode]:
        return cast(Type[EncounterWarningNode], super().model)
    
    @property
    def carrier(self) -> Type[EncounterWarningNodeCarrier]:
        return cast(Type[EncounterWarningNodeCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[EncounterWarningNodeBlueprint]:
        return cast(Type[EncounterWarningNodeBlueprint], super().model)