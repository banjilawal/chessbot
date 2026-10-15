# src/domain/metadata/blueprint/struct/binder/blueprint.py

"""
Module: domain.metadata.blueprint.struct.binder.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, cast

from domain import Archetype, ArchetypeBinder, Archetyped
from domain import StructBlueprint
from err import ArchetypeBinderNullException

T = TypeVar("T", bound="ArchetypeBinder")
M = TypeVar("M", bound="Archetyped")


class BinderBlueprint(StructBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Binder.

     Attributes:
        white_entry: Any
        black_entry: Any
        domain_class: Type[T]
        domain_null_exception: ArchetypeBinderNullException

     ProvideT:

     Super class:
        StructBlueprint
     """
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: Optional[ArchetypeBinderNullException] | None = None,
    ):
        """
        ArgT:
            white_entry: Any
            black_entry: Any
            domain_class: Type[T]
            Optional[ArchetypeBinderNullException]
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or ArchetypeBinderNullException()
        )
        
    @property
    def size(self) -> int:
        return len(self.bindings)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    @abstractmethod
    def archetypes_are_the_same(self) -> bool:
        pass
    
    @property
    def archetypes_differ(self) -> bool:
        return not self.archetypes_are_the_same
    
    @property
    def is_balanced(self) -> bool:
        return (
                self is not None and
                self.entries_are_unique and
                self.archetypes_differ
        )
    
    @property
    def is_not_balanced(self) -> bool:
        return not self.is_balanced

    @property
    @abstractmethod
    def consistency_exists(self) -> bool:
        pass
    
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
    @abstractmethod
    def bindings(self) -> Dict[Archetype, Any]:
        pass
    
    @property
    @abstractmethod
    def to_list(self) -> List[Any]:
        pass
        
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ArchetypeBinderNullException:
        return cast(ArchetypeBinderNullException, super().domain_null_exception)
        
    