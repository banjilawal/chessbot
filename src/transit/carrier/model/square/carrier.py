# src/transit/carrier/model/square/carrier.py

"""
Module: transit.carrier.model.square.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HomeSquare, Square, SquareBlueprint
from transit import ModelCarrier


class SquareCarrier(ModelCarrier[Square]):
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
        entity: [Square|SquareBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[SquareBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Square]
    _blueprint: Optional[SquareBlueprint]
    
    def __init__(
            self,
            model: Optional[Square] | None = None,
            blueprint: Optional[SquareBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Square]
            blueprint: Optional[SquareBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Square | SquareBlueprint]:
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
    
    @property
    def is_home_square_carrier(self) -> bool:
        return (
                self.is_carrying_model and
                isinstance(self._model, HomeSquare)
        )

    def extract_blueprint(self) -> Optional[SquareBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        if self.is_home_square_carrier:
            home_square = cast(HomeSquare, self._model)
            return SquareBlueprint(
                id=home_square.id,
                name=home_square.name,
                board=home_square.board,
                coord=home_square.coord,
                occupant=home_square.occupant,
                formation=home_square.formation,
            )
        model = cast(Square, self._model)
        return SquareBlueprint(
            id=model.id,
            name=model.name,
            board=model.board,
            coord=model.coord,
            occupant=model.occupant,
        )

