# src/topology/basis/traversal/basis.py

"""
Module: topology.basis.traversal.basis
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Generic, TypeVar

from geometry import RecurrenceRegistryCollection
from topology import TopologyBasis

T = TypeVar("T", bound="TraversalRank")


class TraversalTopologyBasis(TopologyBasis, Generic[T]):
    """
    Role:
        -  Data Holder


    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Traversable Ranks, Quuen,

    Attributes:
        recurrence_registries: RecurrenceRegistryCollection[T]

    Provides:

    Super Class:
        Basis
    """
    _recurrence_registries: RecurrenceRegistryCollection[T]
    
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
