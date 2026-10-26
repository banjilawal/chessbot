# src/transit/carrier/context/account/carrier.py

"""
Module: transit.carrier.context.account.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AccountContext, AccountContextBlueprint
from transit import ContextCarrier


class AccountContextCarrier(ContextCarrier[AccountContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated AccountContext or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [Account|AccountContextBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[AccountContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[AccountContext]
    _blueprint: Optional[AccountContextBlueprint]
    
    def __init__(
            self,
            model: Optional[AccountContext] | None = None,
            blueprint: Optional[AccountContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[AccountContext]
            blueprint: Optional[AccountContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[AccountContext | AccountContextBlueprint]:
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
                isinstance(self._model, AccountContext)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None and
                isinstance(self._blueprint, AccountContextBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_consistent(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[AccountContextBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(AccountContext, self._model)
        return AccountContextBlueprint(
            id=model.id,
            firstname=model.firstname,
            lastname=model.lastname,
            email=model.email,
        )

