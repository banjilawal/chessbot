# src/recurrence/series/recurrence.py

"""
Module: recurrence.series.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Tuple, TypeVar

from recurrence import Recurrence

T = TypeVar("T", bound="Rank")


class RecurrenceSeries(ABC, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Store a set of recurrence relations to run as a job.

    Attributes:
        recurrence_set: Tuple[Recurrence, ...]
        
    Provides:

    Super Class:
    """
    
    _recurrence_set: Tuple[Recurrence, ...]
    
    def __init__(self, recurrence_set: Tuple[Recurrence, ...]):
        self._recurrence_set = recurrence_set
        
    @property
    def recurrence_set(self) -> Tuple[Recurrence, ...]:
        return self._recurrence_set
