# src/toggle/orientation/toggle.py

"""
Module: toggle.orientation.toggle
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional, cast

from schema import AxisOrientation, QuadrantOrientation
from toggle import Toggle


class OrientationToggle(Toggle):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Picks toggle a
                -   Coord: Geometric quantity
                -   Orientation: Linear Orientation
            as an toggle for multiplication, conversion or simple addition.

    Attributes:
        orientation: Optional[Orientation]
        coord: Optional[Coord]
        entity: Optional[Coord|Orientation]
        is_axis_toggle: bool
        is_orientation_point: bool

    Provides:
        
        -   _equal_orientation_points(point: Point) -> bool
        -  _equal_axis_toggles(self, point: Point) -> bool
    Super Class:
        Toggle
    """
    _axis: Optional[AxisOrientation]
    _quadrant: Optional[QuadrantOrientation]

    
    def __init__(
            self,
            axis: Optional[AxisOrientation] | None = None,
            quadrant: Optional[QuadrantOrientation] | None = None,
    ):
        """
        Args:
            axis:  Optional[AxisOrientation]
            quadrant: Optional[QuadrantOrientation]
        """
        super().__init__()
        self._axis = axis
        self._quadrant = quadrant
        
    @property
    def entity(self) -> Optional[AxisOrientation| QuadrantOrientation]:
        return self._axis or self._quadrant
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "axis": self._axis,
            "quadrant": self._quadrant,
        }
    
    @property
    def is_axis_toggle(self) -> bool:
        return (
                self._quadrant is None and
                self._axis is not None and
                isinstance(self._axis, AxisOrientation)
        )
    
    @property
    def is_quadrant_toggle(self) -> bool:
        return (
                self._quadrant is not None and
                self._axis is None and
                isinstance(self._quadrant, QuadrantOrientation)
        )

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, OrientationToggle):
            point = cast(OrientationToggle, other)
            if point.is_orientation_point:
                return self._equal_orientation_points(point)
            return self._equal_axis_toggles(self)
        return False
        
    def _equal_orientation_points(self, point: OrientationToggle) -> bool:
        if self.is_orientation_point and point.is_orientation_point:
            return self.entity == point.entity
        return False
    
    def _equal_axis_toggles(self, point: OrientationToggle) -> bool:
        if self.is_axis_toggle and point.is_axis_toggle:
            return self.entity == point.entity
        return False
    
    