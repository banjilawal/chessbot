# src/recurrence/collection/recurrence.py

"""
Module: recurrence.collection.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Dict, Generic, List, Tuple, Type, TypeVar

from topology import RecurrenceRegistry

T = TypeVar("T", bound="TraversalRank")


class RecurrenceRegistryCollection(ABC, Generic[T]):
    """
    Role:
        -   Data Holder
        -   Iterator

    Responsibilities:
        1.  Stores collections of recurrence registries VectorTransformers iterate over.

    Attributes:
        registries: Tuple[RecurrenceRegistry, ...]
        recurrence_registry_type_dict(self) -> Dict[Type[RecurrenceRegistry], RecurrenceRegistry]

    Provides:

    Super Class:
    """
    _registries: Tuple[RecurrenceRegistry, ...]
    
    def __init__(
            self, registries: Tuple[RecurrenceRegistry, ...],
    ):
        """
        Args:
            registries: Tuple[RecurrenceRegistry, ...]
        """
        self._registries = registries
        
    @property
    def origin(self) -> Vector:
        return
        
    @property
    def registries(self) -> Tuple[RecurrenceRegistry, ...]:
        return self._registries
    
    @property
    def recurrence_registry_type_dict(self) -> Dict[Type[RecurrenceRegistry], RecurrenceRegistry]:
        hashtable: Dict[Type[RecurrenceRegistry], RecurrenceRegistry] = {}
        for registry in self._registries:
            registry_model = Type[registry.__class__]
            hashtable[registry_model] = registry
        return hashtable
    
    
    @property
    def number_of_registries(self) -> int:
        return len(self._registries)
    
    @property
    def is_empty(self) -> bool:
        return self.number_of_registries == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def registry_names(self) -> List[str]:
        names: List[str] = []
        for registry_model in self.recurrence_registry_type_dict.keys():
            name = registry_model.__class__.__name__
            if name not in names:
                names.append(name)
        return names
    
    @property
    def has_single_registry_model(self) -> bool:
        return len(self.registry_names) == 1
    
    @property
    def has_multiple_registry_models(self) -> bool:
        return len(self.registry_names) > 1
