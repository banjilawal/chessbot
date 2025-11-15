# src/chess/scalar/scalar.py


"""
Module: chess.scalar.scalar
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""


class Scalar:
    """
    # ROLE: Computation, Transformation
  
    # RESPONSIBILITIES:
    Multiplication of Vector and Coord objects by Scalar.
  
    # PROVIDES:
    Scalar
  
    # ATTRIBUTES:
        *   value (int): range [-BOARD_DIMENSION, BOARD_DIMENSION]
    """
    
    def __init__(self, value: int):
        """
        # Action:
        Construct a Scalar
    
        # Parameters:
            * value (int):
    
        # Returns:
        None
    
        # Raises:
        None
        """
        method = "Scalar.__init__"
        
        self._value = value
    
    @property
    def value(self) -> int:
        return self._value
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Scalar):
            return self._value == other.value
        return False
    
    def __hash__(self):
        return hash(self._value)
    
    def __str__(self):
        return f"Scalar(value={self._value})"
