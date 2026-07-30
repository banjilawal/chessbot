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
    _members: Tuple[RecurrenceRegistry, ...]
    
    def __init__(
            self, members: Tuple[RecurrenceRegistry, ...],
    ):
        """
        Args:
            space: T
            space_mapping_function: SetMappingFunction[T]
        """
        self._members = members
        
    @property
    def members(self) -> Tuple[RecurrenceRegistry, ...]:
        return self._members
    
    @property
    def recurrence_table_type_dict(self) -> Dict[Type[RecurrenceRegistry], RecurrenceRegistry]:
        set_dict: Dict[Type[RecurrenceRegistry], RecurrenceRegistry] = {}
        for member in self._members:
            member_type = Type[member.__class__]
            set_dict[member_type] = member
        return set_dict
