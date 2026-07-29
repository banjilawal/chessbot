# src/recurrence/group/queen/recurrence.py

"""
Module: recurrence.group.queen.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Tuple, Type, cast

from model import Queen
from recurrence import AxisRecurrenceTable, QuadrantRecurrenceTable, RecurrenceTable
from recurrence.group import RecurrenceTableGroup



class QueenRecurrenceSets(RecurrenceTableGroup[Queen]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Groups recurrence tables which build a Queen movement pattern.

    Attributes:
        members: Tuple[RecurrenceTable, ...]
        recurrence_table_type_dict(self) -> Dict[Type[RecurrenceTable], RecurrenceTable]:

    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            axis_recurrence_table: AxisRecurrenceTable,
            quadrant_recurrence_table: QuadrantRecurrenceTable,
    ):
        super().__init__(members=tuple([axis_recurrence_table, quadrant_recurrence_table]))

