# src/transit/carrier/model/square/home/carrier.py

"""
Module: transit.carrier.model.square.home.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HomeSquare, HomeSquareBlueprint, Square, SquareBlueprint
from transit import SquareCarrier


class HomeSquareCarrier(SquareCarrier):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Square or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [HomeSquare|SquareBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[HomeSquareBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[HomeSquare]
    _blueprint: Optional[HomeSquareBlueprint]
    
    def __init__(
            self,
            model: Optional[HomeSquare] | None = None,
            blueprint: Optional[HomeSquareBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[HomeSquare]
            blueprint: Optional[HomeSquareBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[HomeSquare|HomeSquareBlueprint]:
        if self.is_empty:
            return None
        if self.is_carrying_model:
            return self._model
        return self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Square)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, SquareBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_over_capacity(self) -> bool:
        return self.size > 1

    def extract_blueprint(self) -> Optional[HomeSquareBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint

        model = cast(HomeSquare, self._model)
        return HomeSquareBlueprint(
            id=model.id,
            name=model.name,
            board=model.board,
            coord=model.coord,
            occupant=model.occupant,
            formation=model.formation,
        )

