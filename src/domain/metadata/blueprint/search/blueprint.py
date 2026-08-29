# src/domain/metadata/blueprint/search/blueprint.py

"""
Module: domain.metadata.blueprint.search.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import Blueprint, SearchContext
from err import SearchContextNullException

T = TypeVar("T", bound="SearchContext")


class SearchContextBlueprint(Blueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a SearchContext.
         
     Attributes:
        domain_class: Type[T]
        domain_null_exception: SearchContextNullException

     Provides:

     Super Class:
        Blueprint
     """
    _id: Optional[int]
    _name: Optional[str]
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: SearchContextNullException,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: SearchContextNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
        )
        self._id = id
        self._name = name
        
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SearchContextNullException:
        return  cast(SearchContextNullException, super()._domain_null_exception)
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name


