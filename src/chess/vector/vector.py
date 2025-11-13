# chess/vector/vector.py

"""
Module: chess.vector.vector
Author: Banji Lawal
Created: 2025-08-26
version: 1.0.0
"""

from chess.coord import Coord, CoordValidator
from chess.scalar import Scalar, ScalarService
from chess.system import BuildResult, Result, LoggingLevelRouter


class Vector:
    """
    # ROLE: Transformer
  
    # RESPONSIBILITY:
    Transforms Coord by addition or multiplication.
  
    # PROVIDES:
    Vector
  
    # ATTRIBUTES:
      * x (int):  component in the x-plane (column)
      * y (int):  component in the y-plane (row)
      * scalar_service (type[ScalarService]):  provides scalar product functionality
    """
    
    _x: int
    _y: int
    _scalar_service: type[ScalarService]
    
    def __init__(self, x: int, y: int, scalar_service: type[ScalarService] = ScalarService):
        """
        ACTION:
        Construct a Vector object.
    
        PARAMETERS:
            * x (int)
            * y (int)
    
        # Returns:
        None
    
        RAISES:
        None
        """
        self._x = x
        self._y = y
        self._scalar_service = scalar_service
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def scalar_service(self):
        return self._scalar_service
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Vector):
            return self._x == other.x and self._y == other.y
        return False
    
    def __hash__(self):
        return hash((self._x, self._y))
    
    @LoggingLevelRouter.monitor()
    def scalar_product(self, scalar: Scalar) -> BuildResult[Vector]:
        """
        Action:
        Parameters:
          * scalar (Scalar): A scalar
    
        Returns:
          Result[Vector]
    
        Raises:
          InvalidScalarException
        """
        method = "Vector.scalar_product"
        
        try:
            scalar_validation = self._scalar_service.validate_as_scalar(scalar)
            if not scalar_validation.is_success():
                return BuildResult.failure(scalar_validation.exception)
            
            x_component = self._x * scalar.value
            y_component = self._y * scalar.value
            
            return Result(payload=Vector(x=self._x * scalar.value, y=self._y * scalar.value))
        except Exception as e:
            return Result(exception=e)
    
    @LoggingLevelRouter.monitor()
    def add_to_coord(self, coord: Coord) -> Result[Coord]:
        """
        Action:
          Transform a Coord by offsetting Coord.row and Coord.column.
    
        Parameters:
          * point (Coord): A Coord object
    
        Returns:
          Result[Coord]
    
        Raises:
          InvalidCoordException
        """
        method = "Vector.add_to_coord"
        
        validation = CoordValidator.validate(coord)
        try:
            if not validation.is_success():
                return Result(exception=validation.exception)
            
            return Result(Coord(row=coord.row + self._y, column=coord.column + self._x))
        
        except Exception as e:
            return Result(exception=e)
    
    def __str__(self):
        return f"Vector(x={self._x}, y={self._y})"
