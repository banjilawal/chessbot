# src/recurrence/collection/queen/recurrence.py

"""
Module: recurrence.collection.queen.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Queen
from recurrence import AxisRecurrenceRegistry, QuadrantRecurrenceRegistry
from recurrence.collection import RecurrenceRegistryCollection



class QueenRecurrenceRegistries(RecurrenceRegistryCollection[Queen]):
    """
    Role:
        -   Data Holder
        -   Iterator

    Responsibilities:
        1.  Stores collections of recurrence registries VectorTransformers iterate over to derives
            to create QueenVectorSpans.

    Attributes:

    Provides:

    Super Class:
        RecurrenceRegistryCollection
    """
    
    def __init__(
            self,
            axis_recurrence_registry: AxisRecurrenceRegistry,
            quadrant_recurrence_registry: QuadrantRecurrenceRegistry,
    ):
        super().__init__(registries=tuple([axis_recurrence_registry, quadrant_recurrence_registry]))

