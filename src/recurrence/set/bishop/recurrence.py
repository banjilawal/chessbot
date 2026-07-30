# src/recurrence/set/bishop/recurrence.py

"""
Module: recurrence.set.bishop.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Tuple, Type, cast

from model import Bishop
from recurrence import QuadrantRecurrenceRegistry, RecurrenceRegistry
from recurrence.set import RecurrenceRegistryCollection



class BishopRecurrenceRegistries(RecurrenceRegistryCollection[Bishop]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Sets recurrence tables which build a Bishop movement pattern.

    Attributes:
        members: Tuple[RecurrenceTable, ...]
        recurrence_table_type_dict(self) -> Dict[Type[RecurrenceTable], RecurrenceTable]:

    Provides:

    Super Class:
    """
    _table: QuadrantRecurrenceRegistry
    
    def __init__(self, recurrence_table: QuadrantRecurrenceRegistry):
        super().__init__(registries=tuple([recurrence_table]))
        self._table = recurrence_table

    @property
    def registries(self) -> Tuple[QuadrantRecurrenceRegistry, ...]:
        return cast(Tuple[QuadrantRecurrenceRegistry], super().registries)
    
    @property
    def recurrence_registry_type_dict(self) -> Dict[Type[QuadrantRecurrenceRegistry], RecurrenceRegistry]:
        table_type = Type[self._table]
        return {table_type: self._table}
