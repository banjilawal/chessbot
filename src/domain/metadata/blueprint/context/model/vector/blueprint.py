# src/domain/metadata/blueprint/context/model/vector/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from config import XColor
from domain import VectorContext, Y, X, ContextBlueprint, Player
from err import VectorContextNullException


class VectorContextBlueprint(ContextBlueprint[VectorContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an VectorContext.
         
     Attributes:
        domain_class: Type[VectorContext]
        domain_null_exception: VectorContextNullException
        x: Optional[int]
        y: Optional[int]
        player: Optional[Player]
        color: Optional[XColor]

     Provides:

     Super Class:
        ContextBlueprint
     """

    _x: Optional[int]
    _y: Optional[int]
    
    def __init__(
            self,
            domain_class: Optional[Type[VectorContext]] | None = None,
            domain_null_exception: Optional[VectorContextNullException] | None = None,
            x: Optional[int] | None = None,
            y: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Type[VectorContext]
            domain_null_exception: VectorContextNullException
            x: Optional[int]
            y: Optional[int]
        """
        super().__init__(
            domain_class=domain_class or Type[VectorContext],
            domain_null_exception=domain_null_exception or VectorContextNullException(),
        )
        self._x = x
        self._y = y
    
    @property
    def domain_class(self) -> Type[VectorContext]:
        return cast(Type[VectorContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> VectorContextNullException:
        return  cast(VectorContextNullException, super().domain_null_exception)
    
    @property
    def x(self) -> Optional[int]:
        return self._x
    
    @property
    def y(self) -> Optional[int]:
        return self._y
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "x": self._x,
            "y": self._y,
        }
    
    
    
    
    


