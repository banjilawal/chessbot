# src/recurrence/collection/rook/recurrence.py

"""
Module: recurrence.collection.rook.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Tuple, Type, cast

from model import Rook
from topology.recurrence import AxisRecurrenceRegistry
from topology.registry.collection import RecurrenceRegistryCollection



class RookRecurrenceRegistries(RecurrenceRegistryCollection[Rook]):
    """
    Role:
        -   Data Holder
        -   Iterator

    Responsibilities:
        1.  Stores collections of recurrence registries VectorTransformers iterate over to derives
            to create RookVectorSpans.

    Attributes:
        registries: Tuple[AxisRecurrenceRegistry, ...]
        recurrence_registry_type_dict: Dict[Type[AxisRecurrenceRegistry], RecurrenceRegistry]

    Provides:

    Super Class:
        RecurrenceRegistryCollection
    """
    _registry: AxisRecurrenceRegistry
    
    def __init__(self, recurrence_registry: AxisRecurrenceRegistry):
        super().__init__(registries=tuple([recurrence_registry]))
        self._registry = recurrence_registry

    @property
    def registries(self) -> Tuple[AxisRecurrenceRegistry, ...]:
        return cast(Tuple[AxisRecurrenceRegistry], super().registries)
    
    @property
    def recurrence_registry_type_dict(self) -> Dict[Type[AxisRecurrenceRegistry], AxisRecurrenceRegistry]:
        registry_model = Type[self._registry]
        return {registry_model: self._registry}
