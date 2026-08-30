# src/domain/metadata/blueprint/model/searchable/walk/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.walk.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import Context, SearchableModelBlueprint, WalkModel
from err import ModelNullException

T = TypeVar("T", bound="WalkModel")


class WalkModelBlueprint(SearchableModelBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a WalkModel object.
 

     Attributes:
         id: Optional[int]
         domain_class: Type[T]
         
     Provides:

     Super Class:
        SearchableModelBlueprint
     """
    _id: Optional[int]
    
    def __init__(
            self,
            domain_class: Type[T],
            search_context_class: Type[Context[T]],
            domain_null_exception: ModelNullException,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Type[T]
            search_context_class: SearchContext[T]
            domain_null_exception: ModelNullException
            id: Optional[int]
        """
        super().__init__(
            domain_class=domain_class,
            search_context_class=search_context_class,
            domain_null_exception=domain_null_exception,
        )
        self._id = id
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[Context[T]]:
        return cast(Type[Context[T]], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> ModelNullException:
        return cast(ModelNullException, super().domain_null_exception)
    
    @property
    def id(self) -> Optional[int]:
        return self._id
