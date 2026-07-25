# src/recurrence/series/bishop/recurrence.py

"""
Module: recurrence.series.bishop.recurrence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Tuple

from model import Bishop
from recurrence import NortheastQuadrantRecurrence, Recurrence, RecurrenceSeries


class QuadrantSeries(RecurrenceSeries[Bishop]):
    
    def __init__(
            self,
            recurrence_set: Tuple[Recurrence, ...] = (
                NortheastQuadrantRecurrence(),
            )
    ):

