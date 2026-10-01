# src/assurance/reference/chart/position/chart.py

"""
Module: assurance.reference.chart.position.chart
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional

from assurance.reference import ValidatorChart
from domain import Coord


class TokenPositionChart(ValidatorChart[Coord]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores TokenPositionValidator success data.

    Attributes:
        position: Optional[Coord]
        previous_position: Optional[Coord]

    Provides:

    Super
    """
    _position: Optional[Coord]
    _previous_position: Optional[Coord]
    
    def __init__(
            self,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
    ):
        """
        Args:
            position: Optional[Coord]
            previous_position: Optional[Coord]
        """
        super().__init__()
        self._position = position
        self._previous_position = previous_position
    
    @property
    def position(self) -> Optional[Coord]:
        return self._position
    
    @property
    def previous_position(self) -> Optional[Coord]:
        return self._previous_position
    
    @property
    def is_full(self) -> bool:
        return self.size == 2
    
    @property
    def to_dict(self) -> Dict[str, Coord]:
        table: Dict[str, Coord] = {}
        if self._position is not None:
            table["position"] = self._position
        if self._previous_position is not None:
            table["previous_position"] = self._previous_position
        return table