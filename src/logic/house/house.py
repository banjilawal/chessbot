# src/logic/house/house.py

"""
Module: logic.house.house
Author: Banji Lawal
Created: 2025-11-10
version: 1.0.0
"""


from logic.piece import Piece
from logic.square import Square
from logic.house.category import HouseCategory


class House:
    _square: Square
    
    def __init__(self, square: Square):
        self._square = square
        
        
    @property
    def square(self) -> Square:
        return self._square

    @property
    def resident(self) -> Piece:
        return self._square.occupant
    
    @property
    def house_cost(self) -> int:
        return self._square.occupant.rank.ransom
    
    def house_category(self, piece) -> HouseCategory:
        if piece.is_enemy(self._square.occupant):
            return HouseCategory.ENEMY_HOUSE
        return HouseCategory.FRIENDLY_HOUSE
    
    
    
