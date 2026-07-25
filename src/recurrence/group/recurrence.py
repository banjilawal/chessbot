# src/recurrence/group/recurrence.py

"""
Module: recurrence.group.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from model import Vector
from space import SpaceReservoir

R = TypeVar("R", bound="Rank")
S = TypeVar("S", bound="Space")


class RankRecurrenceSet(ABC, Generic[R, S]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Store a set of recurrence relations to run as a job.

    Attributes:
        origin: Vector
        
    Provides:

    Super Class:
    """
    _space_reservoir: S
    
    
    def __init__(self, space_reservoir: S):
        self._space_reservoir = space_reservoir
        
    @property
    def space_reservoir(self) -> S:
        return self._space_reservoir
