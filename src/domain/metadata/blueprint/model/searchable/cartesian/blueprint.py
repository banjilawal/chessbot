# src/domain/metadata/blueprint/model/searchable/cartesian/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.cartesian.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import CartesianPoint, SearchContext, SearchableModelBlueprint
from err import ModelNullException

T = TypeVar("T", bound="CartesianPoint")


class CartesianBlueprint(SearchableModelBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a StateModel object.
 
     Attributes:
         search_context_class: Type[SearchContext[T]]

     Provides:

     Super Class:
        ModelBlueprint
     """
    
    def __init__(
            self,
            domain_class: Type[T],
            search_context_class: Type[SearchContext[T]],
            domain_null_exception: ModelNullException,
    ):
        """
        Args:
            domain_class: Type[Model[T]]
            search_context_class: Type[SearchContext[T]]
            domain_null_exception:ModelNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
        )
        self._search_context_class = search_context_class
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[SearchContext[T]]:
        return self._search_context_class