# src/domain/structure/chart/coord/structure.py

"""
Module: domain.structure.chart.coord.structure
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import  annotations

from typing import Dict, Optional

from domain import Coord
from domain.structure.chart import ParticipantChart


class CoordChart(ParticipantChart[Coord]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores CoordPositionValidator success data.

    Attributes:
        position: Optional[Coord]
        previous_position: Optional[Coord]

    Provides:

    Super
        ParticipantChart
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
    def is_not_consistent(self) -> bool:
        return (
            self._position is None and
            self._previous_position is not None
        )
    
    @property
    def position_exists(self) -> bool:
        return self._position is not None
    
    @property
    def position_does_not_exist(self) -> bool:
        return not self.position_exists
    
    
    @property
    def has_previous_position(self) -> bool:
        return self._previous_position is not None
    
    @property
    def does_not_have_previous_position(self) -> bool:
        return not self.has_previous_position
        
    @property
    def consistency_exists(self) -> bool:
        return not self.is_not_consistent
    
    @property
    def to_dict(self) -> Dict[str, Coord]:
        table: Dict[str, Coord] = {}
        if self._position is not None:
            table["position"] = self._position
        if self._previous_position is not None:
            table["previous_position"] = self._previous_position
        return table