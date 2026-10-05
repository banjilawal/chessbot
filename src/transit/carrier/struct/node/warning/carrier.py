# src/transit/carrier/struct/node/warning/carrier.py

"""
Module: transit.carrier.struct.node.warning.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterWarningNode, EncounterWarningNodeBlueprint
from transit import NodeCarrier


class EncounterWarningNodeCarrier(NodeCarrier[EncounterWarningNode]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated EncounterWarningNode its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [EncounterWarningNode | EncounterWarningNodeBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[EncounterWarningNodeBlueprint]

    Super Class:
        NodeCarrier
    """
    
    def __init__(
            self,
            model: Optional[EncounterWarningNode] | None = None,
            blueprint: Optional[EncounterWarningNodeBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[EncounterWarningNode]
            blueprint: Optional[EncounterWarningNodeBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[EncounterWarningNode | EncounterWarningNodeBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(EncounterWarningNode, entity)
        return cast(EncounterWarningNodeBlueprint, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, EncounterWarningNode)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, EncounterWarningNodeBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[EncounterWarningNodeBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(EncounterWarningNodeBlueprint, self.entity)
            return blueprint
        
        model = cast(EncounterWarningNode, self.entity)
        next_node = EncounterWarningNode()
        previous = EncounterWarningNode()
        
        if model.next is not None:
            next_node = model.next
        if model.previous is not None:
            previous = model.previous
        return EncounterWarningNodeBlueprint(
            payload=model.payload
        )


    