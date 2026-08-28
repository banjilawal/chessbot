# src/domain/metadata/blueprint/model/searchable/cartesian/vector/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.cartesian.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import CartesianBlueprint, Vector, VectorSearchContext
from err import VectorNullException



class VectorBlueprint(CartesianBlueprint[Vector]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Vector object.
        2.  DTO

    Attributes:
        domain_class: Type[Vector]
        search_context_class: Type[VectorSearchContext]
        domain_null_exception: VectorModelNullException
        x: int
        y: int
            
    Provides:

     Super Class:
        CartesianBlueprint
     """
    _x: int
    _y: int
    
    def __init__(
            self,
            x: int,
            y: int,
            domain_class: Optional[Type[Vector]] | None = None,
            domain_null_exception: Optional[VectorNullException] | None = None,
            search_context_class: Optional[Type[VectorSearchContext]] | None = None,
    ):
        """
        Args:
            x: int
            y: int
            domain_class: Optional[Type[Vector]]
            domain_null_exception: Optional[VectorModelNullException]
            search_context_class: Optional[Type[VectorSearchContext]]
        """
        super().__init__(
            domain_class=domain_class or Vector,
            search_context_class=search_context_class or VectorSearchContext,
            domain_null_exception=domain_null_exception or VectorNullException(),
        )
        self._x = x
        self._y = y
        
    @property
    def domain_class(self) -> Type[Vector]:
        return cast(type[Vector], super()._domain_class)
    
    @property
    def search_context_class(self) -> Type[VectorSearchContext]:
        return cast(Type[VectorSearchContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> VectorNullException:
        return cast(VectorNullException, super().domain_null_exception)
    
    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y