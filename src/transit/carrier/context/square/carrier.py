# src/transit/carrier/context/square/carrier.py

"""
Module: transit.carrier.context.square.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HomeSquare, Square, SquareBlueprint
from transit import ContextCarrier


class SquareContextCarrier(ContextCarrier[SquareContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated SquareContext or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Square|SquareContextBlueprint]

    Provides:
        - def extract_ContextBlueprint() -> Optional[SquareContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[SquareContext]
    _blueprint: Optional[SquareContextBlueprint]
    
    def __init__(
            self,
            model: Optional[SquareContext] | None = None,
            blueprint: Optional[SquareContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[SquareContext]
            blueprint: Optional[SquareContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Square | SquareContextBlueprint]:
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
    def is_carrying_ContextBlueprint(self) -> bool:
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
    def is_home_square_modelCarrier(self) -> bool:
        return (
                self.is_carrying_model and
                isinstance(self._model, HomeSquare)
        )

    def extract_ContextBlueprint(self) -> Optional[SquareContextBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        if self.is_home_square_carrier:
            home_square = cast(HomeSquareContext, self._model)
            return SquareContextBlueprint(
                id=home_square.id,
                name=home_square.name,
                board=home_square.board,
                coord=home_square.coord,
                occupant=home_square.occupant,
                formation=home_square.formation,
            )
        context = cast(SquareContext, self._model)
        return SquareContextBlueprint(
            id=context.id,
            name=context.name,
            board=context.board,
            coord=context.coord,
            occupant=context.occupant,
        )

