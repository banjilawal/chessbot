# src/err/recurrence/group/bishop/recurrence.py

"""
Module: err.recurrence.group.bishop.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Tuple, Type, cast

from model import Bishop
from recurrence import QuadrantRecurrenceTable, RecurrenceTable
from err.recurrence.group import RecurrenceTableGroup



class BishopRecurrenceSets(RecurrenceTableGroup[Bishop]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Groups recurrence tables which build a Bishop movement pattern.

    Attributes:
        members: Tuple[RecurrenceTable, ...]
        recurrence_table_type_dict(self) -> Dict[Type[RecurrenceTable], RecurrenceTable]:

    Provides:

    Super Class:
    """
    _table: QuadrantRecurrenceTable
    
    def __init__(self, recurrence_table: QuadrantRecurrenceTable):
        super().__init__(members=tuple([recurrence_table]))
        self._table = recurrence_table

    @property
    def members(self) -> Tuple[QuadrantRecurrenceTable, ...]:
        return cast(Tuple[QuadrantRecurrenceTable], super().members)
    
    @property
    def recurrence_table_type_dict(self) -> Dict[Type[QuadrantRecurrenceTable], RecurrenceTable]:
        table_type = Type[self._table]
        return {table_type: self._table}
