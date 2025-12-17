# src/chess/formation/lookup/context/context.py

"""
Module: chess.formation.lookup.context.context
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.formation import BattleOrder
from chess.system import Context, GameColor


class OrderContext(Context[BattleOrder]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provide an BattleOrderFinder with an attribute value to find BattleOrders with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   square (Optional[str])
        *   color (Optional[ColorColor])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _square: Optional[str]
    _color: Optional[GameColor]
    
    def __init__(
            self,
            name: Optional[str] = None,
            square: Optional[str] = None,
            color: Optional[GameColor] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (Optional[str])
            *   square (Optional[str])
            *   color (Optional[Color])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=None, name=name)
        self._color = color
        self._square = square
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def square(self) -> Optional[str]:
        return self._square
    
    def to_dict(self) -> dict:
        """
        # Convert the OrderContext object to a dictionary.

        # PARAMETERS:
        None

        # Returns:
        dict

        # Raises:
        None
        """
        return {
            "name": self.name,
            "color": self._color,
            "square": self._square,
        }