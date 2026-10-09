# src/transit/carrier/model/alert/carrier.py

"""
Module: transit.carrier.model.alert.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Alert
from transit import ModelCarrier


class AlertCarrier(ModelCarrier[Alert]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Alert or its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [Alert | AlterTableBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[AlertBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Alert]
    _blueprint: Optional[AlertBlueprint]
    
    def __init__(
            self,
            model: Optional[Alert] | None = None,
            blueprint: Optional[AlertBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Alert]
            blueprint: Optional[AlertBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Alert | AlterTableBlueprint]:
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
                isinstance(self._model, Alert)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, AlterTableBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[AlertBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(Alert, self._model)
        return AlterTableBlueprint(
            id=model.id,
            game=model.game,
            board=model.board,
        )

