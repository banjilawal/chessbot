# src/recurrence/set/recurrence.py

"""
Module: recurrence.set.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Dict, Generic, Tuple, Type, TypeVar

from recurrence import RecurrenceRegistry

T = TypeVar("T", bound="Rank")


class RecurrenceSet(ABC, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Stores sets of recurrence registries.

    Attributes:
        members: Tuple[RecurrenceTable, ...]
        recurrence_table_type_dict(self) -> Dict[Type[RecurrenceTable], RecurrenceTable]:

    Provides:

    Super Class:
    """
    _registries: Tuple[RecurrenceRegistry, ...]
    
    def __init__(
            self, registries: Tuple[RecurrenceRegistry, ...],
    ):
        """
        Args:
            space: T
            space_mapping_function: SetMappingFunction[T]
        """
        self._registries = registries
        
    @property
    def registries(self) -> Tuple[RecurrenceRegistry, ...]:
        return self._registries
    
    @property
    def recurrence_registry_type_dict(self) -> Dict[Type[RecurrenceRegistry], RecurrenceRegistry]:
        set_dict: Dict[Type[RecurrenceRegistry], RecurrenceRegistry] = {}
        for member in self._registries:
            member_type = Type[member.__class__]
            set_dict[member_type] = member
        return set_dict
