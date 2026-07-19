# src/selector/orientation/selector.py

"""
Module: selector.orientation.selector
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional, cast

from schema import AxisOrientation, QuadrantOrientation
from selector import Selector


class OrientationSelector(Selector):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Picks selector a
                -   Coord: Geometric quantity
                -   Orientation: Linear Orientation
            as an selector for multiplication, conversion or simple addition.

    Attributes:
        orientation: Optional[Orientation]
        coord: Optional[Coord]
        entity: Optional[Coord|Orientation]
        is_axis_selector: bool
        is_orientation_point: bool

    Provides:
        
        -   _equal_orientation_points(point: Point) -> bool
        -  _equal_axis_selectors(self, point: Point) -> bool
    Super Class:
        Selector
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
    def is_axis_selector(self) -> bool:
        return (
                self._quadrant is None and
                self._axis is not None and
                isinstance(self._axis, AxisOrientation)
        )
    
    @property
    def is_quadrant_point(self) -> bool:
        return (
                self._quadrant is not None and
                self._axis is None and
                isinstance(self._quadrant, QuadrantOrientation)
        )

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, OrientationSelector):
            point = cast(OrientationSelector, other)
            if point.is_orientation_point:
                return self._equal_orientation_points(point)
            return self._equal_axis_selectors(self)
        return False
        
    def _equal_orientation_points(self, point: OrientationSelector) -> bool:
        if self.is_orientation_point and point.is_orientation_point:
            return self.entity == point.entity
        return False
    
    def _equal_axis_selectors(self, point: OrientationSelector) -> bool:
        if self.is_axis_selector and point.is_axis_selector:
            return self.entity == point.entity
        return False
    
    