# src/recurrence/set/queen/recurrence.py

"""
Module: recurrence.set.queen.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Tuple, Type, cast

from model import Queen
from recurrence import AxisRecurrenceRegistry, QuadrantRecurrenceRegistry, RecurrenceRegistry
from recurrence.set import RecurrenceRegistryCollection



class QueenRecurrenceSets(RecurrenceRegistryCollection[Queen]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Sets recurrence tables which build a Queen movement pattern.

    Attributes:
        members: Tuple[RecurrenceTable, ...]
        recurrence_table_type_dict(self) -> Dict[Type[RecurrenceTable], RecurrenceTable]:

    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            axis_recurrence_table: AxisRecurrenceRegistry,
            quadrant_recurrence_table: QuadrantRecurrenceRegistry,
    ):
        super().__init__(registries=tuple([axis_recurrence_table, quadrant_recurrence_table]))

