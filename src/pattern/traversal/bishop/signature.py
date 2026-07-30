# src/pattern/traversal/bishop/pattern.py

"""
Module: pattern.traversal.bishop.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import cast

from model import Bishop
from pattern import TraversalSignature
from recurrence import BishopRecurrenceRegistries


class BishopSignature(TraversalSignature[Bishop]):
    
    def __init__(self, recurrence_registries: BishopRecurrenceRegistries):
        """
        Args:
            recurrence_registries: BishopRecurrenceRegistries
        """
        super().__init__(recurrence_registries=recurrence_registries)
        
    @property
    def recurrence_registries(self) -> BishopRecurrenceRegistries:
        return cast(BishopRecurrenceRegistries, super().recurrence_registries)