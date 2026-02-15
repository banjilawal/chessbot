
from __future__ import annotations
from typing import List

from chess.node.category import OccupantCategory
from chess.node.color import DiscoveryColor
from chess.square import Square


class Node:
    _square: Square
    _discovery_color: DiscoveryColor
    _occupant_category: OccupantCategory
    
    _outgoing: List[Node]
    _incoming: List[Node]
    
    def __init__(self, square: Square):
        self._square: square
        self._discovery_color = DiscoveryColor.WHITE
        self._occupant_category = OccupantCategory.NO_OCCUPANT
        
        self._incoming = []
        self._outgoing = []
        
    @property
    def square(self) -> Square:
        return self._square
    
    @property
    def discovery_color(self) -> DiscoveryColor:
        return self._discovery_color
    
    @discovery_color.setter
    def discovery_color(self, discovery_color: DiscoveryColor):
        self._discovery_color = discovery_color
        
    @property
    def occupant_category(self) -> OccupantCategory:
        return self._occupant_category
    
    @occupant_category.setter
    def occupant_category(self, occupant_category: OccupantCategory):
        self._occupant_category = occupant_category
        
    @property
    def incoming(self) -> List[Node]:
        return self._incoming
    
    @property
    def outgoing(self) -> List[Node]:
        return self._outgoing