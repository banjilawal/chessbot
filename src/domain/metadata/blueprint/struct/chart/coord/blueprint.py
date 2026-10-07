# src/domain/metadata/blueprint/struct/chart/footstep.blueprint.py

"""
Module: domain.metadata.blueprint.struct.chart.footstep.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, Type, cast

from domain import Coord, ChartBlueprint, Footstep
from err import FootstepNullException


class FootstepBlueprint(ChartBlueprint[Footstep]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Footstep.

     Attributes:
        position: Optional[Coord]
        previous_position: Optional[Coord]
        Optional[Type[Footstep]]
        domain_null_exception: Optional[FootstepNullException]

     Provides:

     Super Class:
        ChartBlueprint
     """
    _position: Optional[Coord]
    _previous_position: Optional[Coord]
    
    def __init__(
            self,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
            domain_class: Optional[Type[Footstep]] | None = None,
            domain_null_exception: Optional[FootstepNullException] | None = None,
    ):
        """
        Args:
            position: Optional[Coord]
            previous_position: Optional[Coord]
            Optional[Type[Footstep]]
            domain_null_exception: Optional[FootstepNullException]
        """
        super().__init__(
            domain_class=domain_class or Footstep,
            domain_null_exception=domain_null_exception or FootstepNullException(),
        )
        self._position = position
        self._previous_position = previous_position
        
    @property
    def position(self) -> Optional[Coord]:
        return self._position
    
    @property
    def previous_position(self) -> Optional[Coord]:
        return self._previous_position
    
    @property
    def size(self) -> int:
        return len(len[self._position, self._previous_position])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def consistency_exists(self) -> bool:
        if (
            self._position is not None and
            not isinstance(self._position, Coord)
        ):
            return False
        if (
            self._position is None and
            self._previous_position is not None
        ):
            return False
        if (
            self._previous_position is not None and
            not isinstance(self._previous_position, Coord)
        ):
            return False
        elif (
            self._position is not None and
            self._previous_position is None
        ):
            return True
        return True
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def to_dict(self) -> Dict[str, Coord]:
        return {
            "position": self._position,
            "previous_position": self._previous_position,
        }
    
    @property
    def domain_class(self) -> Type[Footstep]:
        return cast(Type[Footstep], super().domain_class)
    
    @property
    def domain_null_exception(self) -> FootstepNullException:
        return cast(FootstepNullException, super().domain_null_exception)
    
    
