# src/recurrence/collection/bishop/recurrence.py

"""
Module: recurrence.collection.bishop.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Tuple, Type, cast

from model import Bishop
from topology.recurrence import QuadrantRecurrenceRegistry
from topology.registry.collection import RecurrenceRegistryCollection



class BishopRecurrenceRegistries(RecurrenceRegistryCollection[Bishop]):
    """
    Role:
        -   Data Holder
        -   Iterator

    Responsibilities:
        1.  Stores collections of recurrence registries VectorTransformers iterate over to derives
            to create RookVectorSpans.

    Attributes:
        registries: Tuple[QuadrantRecurrenceRegistry, ...]
        recurrence_registry_type_dict: Dict[Type[QuadrantRecurrenceRegistry], RecurrenceRegistry]

    Provides:

    Super Class:
        RecurrenceRegistryCollection
    """
    _registry: QuadrantRecurrenceRegistry
    
    def __init__(self, recurrence_table: QuadrantRecurrenceRegistry):
        super().__init__(registries=tuple([recurrence_table]))
        self._registry = recurrence_table

    @property
    def registries(self) -> Tuple[QuadrantRecurrenceRegistry, ...]:
        return cast(Tuple[QuadrantRecurrenceRegistry], super().registries)
    
    @property
    def recurrence_registry_type_dict(self) -> Dict[Type[QuadrantRecurrenceRegistry], QuadrantRecurrenceRegistry]:
        registry_model = Type[self._registry]
        return {registry_model: self._registry}
