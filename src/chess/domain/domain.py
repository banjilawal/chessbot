# src/chess/owner/owner.py

"""
Module: chess.graph.owner
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from typing import List, Optional

from chess.coord import Coord
from chess.house import House
from chess.pawn import ActorPlacementRequiredException
from chess.piece import Piece


class Domain:
    """
    
    """
    _owner: Piece
    _tree: List[Coord]
    _residents: List[Piece]
    _tree_root: Optional[Coord]
    _previous_tree_root: Coord
    
    _enemy_houses: List[House]
    _friendly_houses: List[House]

    
    def __init__(self, piece: Piece):
        self._owner = piece
        self._id = self._owner.id
        self._tree = List[Coord]
        self._residents = List[Piece]
        self._previous_tree_root = None
        self._tree_root = piece.current_position

    
    @property
    def owner(self) -> Piece:
        return self._owner
    
    @property
    def tree_root(self) -> Coord:
        return self._tree_root
    
    @property
    def previous_tree_root(self) -> Optional[Coord]:
        return self._previous_tree_root
    
    @property
    def tree(self) -> List[Coord]:
        return self._tree
    
    @property
    def residents(self) -> List[Piece]:
        return self._residents
    
    def update(self):
        """"""
        method = "Domain.update"
        
        if self._tree_root is None and self._previous_tree_root == self._tree_root:
            raise ActorPlacementRequiredException(f"{method}: {ActorPlacementRequiredException.DEFAULT_MESSAGE}")
        if self.previous_tree_root is not None and self.previous_tree_root in self._tree:
            self._tree.remove(self.previous_tree_root)
            
        if self._tree_root is not None and self._tree_root not in self._tree:
            
            self._previous_tree_root = self._tree_root
            
            self._tree_root = self._owner.current_position
    
    def __eq__(self, other) -> bool:
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Domain):
            return self._id == other._id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return f"{self._owner} at {self._tree}"
