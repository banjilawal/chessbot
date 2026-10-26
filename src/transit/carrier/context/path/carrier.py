# src/transit/carrier/context/path/carrier.py

"""
Module: transit.carrier.context.path.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import PathContext, PathContextBlueprint
from transit import ContextCarrier


class PathContextCarrier(ContextCarrier[PathContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated PathContext or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [Path|PathContextBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[PathContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[PathContext]
    _blueprint: Optional[PathContextBlueprint]
    
    def __init__(
            self,
            model: Optional[PathContext] | None = None,
            blueprint: Optional[PathContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[PathContext]
            blueprint: Optional[PathContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[PathContext | PathContextBlueprint]:
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
                isinstance(self._model, PathContext)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None and
                isinstance(self._blueprint, PathContextBlueprint)
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
    
    def extract_blueprint(self) -> Optional[PathContextBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(PathContext, self._model)
        return PathContextBlueprint(
             label=model.label,
             origin=model.origin,
             destination=model.destination,
        )

