# src/chess/vector/vector.py

"""
Module: chess.vector.vector
Author: Banji Lawal
Created: 2025-08-26
version: 1.0.0
"""


class Vector:
    """
    # ROLE: Transformer, Computation, Iteration.
  
    # RESPONSIBILITY:
    Consider,
        1.  A Piece travels on the X,Y plane. delta_x and delta_y might be different. Iterating through Coords
            to the next Coord.
        2.  Let the series of Coords = C(x0, y0), C(x1, y1), .., C(x_n-1, y_n-1), C(xn, yn)
        3.  Let
                x_i = x_(i-1) + delta_x,
                y_j = y_(j-1) - delta_y
        4.  Therefore,
                x_n = x_0 + delta_x * (n-1),
                y_n = y_0 - delta_y * (n-1)
        5.  delta_x = N and delta_y = M.
        6.  We see iterating through a series of Coords requires the vector; V(delta_x, delta_y).
    Therefore, a Vector provides the interval for stepping  through a series of Coords.
  
    # PROVIDES:
    Vector
  
    # ATTRIBUTES:
        *   x (int):  component in the x-plane (column)
        *   y (int):  component in the y-plane (row)
    """
    
    _x: int
    _y: int
    
    def __init__(self, x: int, y: int):
        """
        # ACTION:
        Construct a Vector object.
    
        # PARAMETERS:
            *   x (int)
            *   y (int)
    
        # Returns:
        None
    
        # RAISES:
        None
        """
        method = "Vector.__init__"
      
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
        return f"Vector(x={self._x}, y={self._y})"
