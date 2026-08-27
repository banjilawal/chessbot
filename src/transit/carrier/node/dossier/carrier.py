# src/transit/carrier/structure/node/dossier/carrier.py

"""
Module: transit.carrier.structure.node.dossier.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from fabrication import DossierNodeBlueprint
from transit.structure.node import DossierNode
from transit.carrier import NodeCarrier


class DossierNodeCarrier(NodeCarrier):
    """
    Role:
        - Boundary Carrier

    Responsibilities:
        1.  Transport either a hydrated DossierNode or its Blueprint across validation and
            other processing boundaries.
    
    Attributes:
        model: Optional[DossierNode]
        blueprint: Optional[DossierNodeBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        NodeCarrier
    """
    _model: Optional[DossierNode]
    _blueprint: Optional[DossierNodeBlueprint]
    
    def __init__(
            self,
            model: Optional[DossierNode] | None = None,
            blueprint: Optional[DossierNodeBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[DossierNode]
            blueprint: Optional[DossierNodeBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
        
    @property
    def entity(self) -> Optional[DossierNode|DossierNodeBlueprint]:
        if self.is_not_carrying_anything:
            return None
        if self.is_carrying_model:
            return self._model
        return self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, DossierNode)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, DossierNodeBlueprint)
        )
    
    @property
    def is_not_carrying_anything(self) -> bool:
        return self._model is not None and self._blueprint is not None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything
    
    def extract_blueprint(self) -> Optional[DossierNodeBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return DossierNodeBlueprint(dossier=self._model.payload)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DossierNodeCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

