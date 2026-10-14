# src/domain/metadata/blueprint/struct/binder/blueprint.py

"""
Module: domain.metadata.blueprint.struct.binder.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, Type, TypeVar, cast

from domain import Archetype, ArchetypeBinder, Archetyped
from domain import StructBlueprint
from err import ArchetypeBinderNullException

S = TypeVar("S", bound="ArchetypeBinder")
M = TypeVar("M", bound="Archetyped")


class BinderBlueprint(StructBlueprint[S, M], ABC, Generic[S, M]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Binder.

     Attributes:
        white_entry: M
        black_entry: M
        domain_class: Type[S]
        domain_null_exception: ArchetypeBinderNullException

     Provides:

     Super Class:
        StructBlueprint
     """
    _white_entry: M
    _black_entry: M
    
    def __init__(
            self,
            white_entry: M, 
            black_entry: M,
            domain_class: Type[S],
            domain_null_exception: Optional[ArchetypeBinderNullException] | None = None,
    ):
        """
        Args:
            white_entry: M
            black_entry: M
            domain_class: Type[S]
            Optional[ArchetypeBinderNullException]
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or ArchetypeBinderNullException()
        )
        self._white_entry = white_entry
        self._black_entry = black_entry
        
    @property
    def white_entry(self) -> S:
        return self._white_entry
    
    @property
    def black_entry(self) -> S:
        return self._black_entry
    
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
    def archetypes_are_the_same(self) -> bool:
        return self._white_entry.archetype == self._black_entry.archetype
    
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
    def consistency_exists(self) -> bool:
        return (
                self.is_balanced and
                self._white_entry.archetype == Archetype.WHITE and
                self._black_entry.archetype == Archetype.BLACK
        )
    
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
    def bindings(self) -> Dict[Archetype, M]:
        pass
        
    @property
    def to_dict(self) -> Dict[str, M]:
        return {
            "white": self._white_entry,
            "black": self._black_entry
        }
    
    @property
    def domain_class(self) -> Type[S]:
        return cast(Type[S], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ArchetypeBinderNullException:
        return cast(ArchetypeBinderNullException, super().domain_null_exception)
        
    