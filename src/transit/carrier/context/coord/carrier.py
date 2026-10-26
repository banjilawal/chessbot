# src/transit/carrier/context/coord/carrier.py

"""
Module: transit.carrier.context.coord.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CoordContext, CoordContextBlueprint
from transit import ContextCarrier


class CoordContextCarrier(ContextCarrier[CoordContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated CoordContext or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [Coord|CoordContextBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[CoordContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[CoordContext]
    _blueprint: Optional[CoordContextBlueprint]
    
    def __init__(
            self,
            model: Optional[CoordContext] | None = None,
            blueprint: Optional[CoordContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[CoordContext]
            blueprint: Optional[CoordContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[CoordContext | CoordContextBlueprint]:
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
                isinstance(self._model, CoordContext)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None and
                isinstance(self._blueprint, CoordContextBlueprint)
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
    
    def extract_blueprint(self) -> Optional[CoordContextBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(CoordContext, self._model)
        return CoordContextBlueprint(
            row=model.row,
            column=model.column,
        )

