# src/recurrence/group/rook/recurrence.py

"""
Module: recurrence.group.rook.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Tuple, Type, cast

from model import Rook
from recurrence import AxisRecurrenceTable, RecurrenceTable
from recurrence.group import RecurrenceTableGroup



class RookRecurrenceSets(RecurrenceTableGroup[Rook]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Groups recurrence tables which build a Rook movement pattern.

    Attributes:
        members: Tuple[RecurrenceTable, ...]
        recurrence_table_type_dict(self) -> Dict[Type[RecurrenceTable], RecurrenceTable]:

    Provides:

    Super Class:
    """
    _table: AxisRecurrenceTable
    
    def __init__(self, recurrence_table: AxisRecurrenceTable):
        super().__init__(members=tuple([recurrence_table]))
        self._table = recurrence_table

    @property
    def members(self) -> Tuple[AxisRecurrenceTable, ...]:
        return cast(Tuple[AxisRecurrenceTable], super().members)
    
    @property
    def recurrence_table_type_dict(self) -> Dict[Type[AxisRecurrenceTable], RecurrenceTable]:
        table_type = Type[self._table]
        return {table_type: self._table}
