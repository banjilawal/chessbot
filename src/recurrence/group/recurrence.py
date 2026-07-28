# src/recurrence/group/recurrence.py

"""
Module: recurrence.group.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Dict, Generic, Tuple, Type, TypeVar

from recurrence import RecurrenceTable

T = TypeVar("T", bound="Rank")


class RecurrenceTableGroup(ABC, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Groups recurrence tables which build a rank's movement pattern.

    Attributes:
        members: Tuple[RecurrenceTable, ...]
        recurrence_table_type_dict(self) -> Dict[Type[RecurrenceTable], RecurrenceTable]:

    Provides:

    Super Class:
    """
    _members: Tuple[RecurrenceTable, ...]
    
    def __init__(
            self, members: Tuple[RecurrenceTable, ...],
    ):
        """
        Args:
            space: T
            space_mapping_function: GroupMappingFunction[T]
        """
        self._members = members
        
    @property
    def members(self) -> Tuple[RecurrenceTable, ...]:
        return self._members
    
    @property
    def recurrence_table_type_dict(self) -> Dict[Type[RecurrenceTable], RecurrenceTable]:
        group_dict: Dict[Type[RecurrenceTable], RecurrenceTable] = {}
        for member in self._members:
            member_type = Type[member.__class__]
            group_dict[member_type] = member
        return group_dict
