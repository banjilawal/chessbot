# src/model/state/math/vector/model/state.py

"""
Module: model.state.math.vector.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class Vector:
    """
    Role:
        -   Model
        -   Stateless Data-Holder
    
    About:
        Consider,
            1.  A Token travels on the X,Y plane.
                    -   abs(delta_x - delta_y) > 0
            2.  Let the series of be
                    -   Coords = C(x0, y0), C(x1, y1), ., C(x_n-1, y_n-1), C(xn, yn)
            3.  Let
                    -   x_i = x_(i-1) + delta_x,
                    -   y_j = y_(j-1) - delta_y
            4.  Therefore,
                    -   x_n = x_0 + delta_x * (n-1),
                    -   y_n = y_0 - delta_y * (n-1)
            5.  delta_x = N and delta_y = M.
            6.  We see iterating through a series of Coords requires the vector;
                    V(delta_x, delta_y).
            7.  Therefore, a Vector provides the interval for stepping through
                a series of Coords.
    
    Responsibilities:
        1.  Represents a delta_x, delta_y which for traveling to coord.
    
    Attributes:
        x: int
        y: int
    
    Provides:
    
    Super Class:
    """
    _x: int
    _y: int
    
    def __init__(self, x: int, y: int):
        """
        Args:
            x: int
            y: int
        """
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Vector):
            return self._x == other.x and self._y == other.y
        return False
    
    def __hash__(self):
        return hash((self._x, self._y))
    
    def __str__(self):
        return f"Vector:{{x:{self._x}, y:{self._y}}}"
