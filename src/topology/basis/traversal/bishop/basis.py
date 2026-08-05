# src/topology/basis/traversal/bishop/basis.py

"""
Module: topology.basis.traversal.bishop.basis
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import cast

from model import Bishop
from basis import TraversalTopologyBasis
from geometry.recurrence import BishopRecurrenceRegistries


class BishopTopologyBasis(TraversalTopologyBasis[Bishop]):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints that generate a BishopVectorSpan.

    Attributes:
        recurrence_registries: RecurrenceRegistryCollection[T]

    Provides:

    Super Class:
        TraversalTopologyBasis
    """
    def __init__(self, recurrence_registries: BishopRecurrenceRegistries):
        """
        Args:
            recurrence_registries: BishopRecurrenceRegistries
        """
        super().__init__(recurrence_registries=recurrence_registries)
        
    @property
    def recurrence_registries(self) -> BishopRecurrenceRegistries:
        return cast(BishopRecurrenceRegistries, super().recurrence_registries)
    
    