# src/recurrence/set/rook/recurrence.py

"""
Module: recurrence.set.rook.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Tuple, Type, cast

from model import Rook
from recurrence import AxisRecurrenceRegistry, RecurrenceRegistry
from recurrence.set import RecurrenceRegistryCollection



class RookRecurrenceSets(RecurrenceRegistryCollection[Rook]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Sets recurrence tables which build a Rook movement pattern.

    Attributes:
        members: Tuple[RecurrenceTable, ...]
        recurrence_table_type_dict(self) -> Dict[Type[RecurrenceTable], RecurrenceTable]:

    Provides:

    Super Class:
    """
    _table: AxisRecurrenceRegistry
    
    def __init__(self, recurrence_table: AxisRecurrenceRegistry):
        super().__init__(registries=tuple([recurrence_table]))
        self._table = recurrence_table

    @property
    def registries(self) -> Tuple[AxisRecurrenceRegistry, ...]:
        return cast(Tuple[AxisRecurrenceRegistry], super().registries)
    
    @property
    def recurrence_registry_type_dict(self) -> Dict[Type[AxisRecurrenceRegistry], RecurrenceRegistry]:
        table_type = Type[self._table]
        return {table_type: self._table}
