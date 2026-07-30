# src/pattern/traversal/traversal.py

"""
Module: pattern.traversal.category.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Generic, TypeVar


from pattern import Signature
from recurrence import RecurrenceRegistryCollection


T = TypeVar("T", bound="Rank")


class TraversalSignature(Signature, Generic[T]):
    """
    Role:
        -  Iteration


    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Traversable Ranks, Quuen,

    Attributes:
        recurrence_registry_collection: RecurrenceRegistryCollection[T]

    Provides:

    Super Class:
        Signature
    """
    _recurrence_registries: RecurrenceRegistryCollection
    
    def __init__(self, recurrence_registries: RecurrenceRegistryCollection[T], ):
        """
        Args:
            recurrence_registries: RecurrenceRegistryCollection[T]
        """
        super().__init__()
        self._recurrence_registries = recurrence_registries
    
    @property
    def recurrence_registries(self) -> RecurrenceRegistryCollection[T]:
        return self._recurrence_registries
