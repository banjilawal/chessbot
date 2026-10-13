# src/domain/metadata/blueprint/struct/binder/blueprint.py

"""
Module: domain.metadata.blueprint.struct.binder.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Type, TypeVar, cast

from domain import ArchetypeBinder
from domain import StructBlueprint
from err import ArchetypeBinderNullException

T = TypeVar("T", bound="ArchetypeBinder")

class BinderBlueprint(StructBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Binder.

     Attributes:
         domain_class: Type[T]
         domain_null_exception: ArchetypeBinderNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: ArchetypeBinderNullException,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: ArchetypeBinderNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def consistency_exists(self) -> bool:
        if self is None:
            return False
        if self.is_half_full:
            return False
        if self.entries_are_not_unique:
            return False
        if self.is_full and self.entries_are_unique:
            return True
        return False
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    @abstractmethod
    def entries_are_unique(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def entries_are_not_unique(self) -> bool:
        pass
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_full(self) -> bool:
        return self.size == 2
    
    @property
    def is_half_full(self) -> bool:
        return self.size == 1
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, T]:
        pass
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ArchetypeBinderNullException:
        return cast(ArchetypeBinderNullException, super().domain_null_exception)
    
    
