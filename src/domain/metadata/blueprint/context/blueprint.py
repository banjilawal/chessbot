# src/domain/metadata/blueprint/context/blueprint.py

"""
Module: domain.metadata.blueprint.context.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional, Type, TypeVar, cast

from domain import Blueprint, Context
from err import ContextNullException

T = TypeVar("T", bound="Context")


class ContextBlueprint(Blueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a SearchContext.
         
     Attributes:
        domain_class: Type[T]
        domain_null_exception: ContextNullException

     Provides:

     Super Class:
        Blueprint
     """
    _id: Optional[int]
    _name: Optional[str]
    _max_size: Optional[int]
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: ContextNullException,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            max_size: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: ContextNullException
            id: Optional[int]
            name: Optional[str]
            max_size: Optional[int]
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
        )
        self._id = id
        self._name = name
        self._max_size = max_size or 1
        
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ContextNullException:
        return  cast(ContextNullException, super()._domain_null_exception)
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def max_size(self) -> int:
        return self._max_size
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass


