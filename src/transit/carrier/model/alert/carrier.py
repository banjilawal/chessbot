# src/transit/carrier/model/alert/carrier.py

"""
Module: transit.carrier.model.alert.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AlertTable
from transit import ModelCarrier


class AlertTableCarrier(ModelCarrier[AlertTable]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Alert or its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [AlertTable | AlterTableBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[AlertTableBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[AlertTable]
    _blueprint: Optional[AlertTableBlueprint]
    
    def __init__(
            self,
            model: Optional[AlertTable] | None = None,
            blueprint: Optional[AlertTableBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[AlertTable]
            blueprint: Optional[AlertTableBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[AlertTable | AlterTableBlueprint]:
        if self.is_empty:
            return None
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, AlertTable)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, AlterTableBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[AlertTableBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(AlertTable, self._model)
        return AlterTableBlueprint(
            id=model.id,
            game=model.game,
            board=model.board,
        )

