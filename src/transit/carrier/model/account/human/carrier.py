# src/transit/carrier/model/account/human/carrier.py

"""
Module: transit.carrier.model.account.human.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HumanAccount, HumanAccountBlueprint
from transit import AccountCarrier


class HumanAccountCarrier(AccountCarrier):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated HumanAccount or its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [HumanAccount|HumanAccountBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[HumanAccountBlueprint]

    Super Class:
        HumanAccountCarrier
    """
    
    _model: Optional[HumanAccount]
    _blueprint: Optional[HumanAccountBlueprint]
    
    def __init__(
            self,
            model: Optional[HumanAccount] | None = None,
            blueprint: Optional[HumanAccountBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[HumanAccount]
            blueprint: Optional[HumanAccountBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[HumanAccount | HumanAccountBlueprint]:
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
                isinstance(self._model, HumanAccount)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, HumanAccountBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[HumanAccountBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(HumanAccount, self._model)
        return HumanAccountBlueprint(
            subscriber=model.subscriber,
        )
    
    



