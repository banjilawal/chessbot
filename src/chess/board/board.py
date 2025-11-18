# src/chess/board/board.py

"""
Module: chess.board.board
Author: Banji Lawal
Created: 2025-07-31
version: 1.0.0
"""


from typing import List
from chess.piece import Piece
from chess.square import Square


class Board:
    """
    # ROLE: Data-Holder/Data Owner
  
    # RESPONSIBILITIES:
    The Surface of Squares where Pieces are played.
  
    # PROVIDES:
      Board
  
    # ATTRIBUTES:
        * id (int): Unique identifier.
        * pieces ([Piece]): Array pieces in Board object
        * squares ([[Square]]): A 2D array of squares in Board object.
    """
    
    _id: int
    _pieces: List[Piece]
    _squares: List[List[Square]]
    
    def __init__(self, id: int):
        """
        # Action:
        Constructs Board object
    
        # Parameters:
          * id (int):
    
        # Returns:
        None
    
        # Raises:
        None
        """
        method = "Board.__init__"
        
        self._id = id
        self._pieces = [Piece]
        self._squares = [[Square]]
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def squares(self) -> List[Square]:
        """Flatten the 2D board_validator into team_name 1D list of squares for efficient searching."""
        return [square for row in self._squares for square in row]
    
    @property
    def pieces(self) -> List[Piece]:
        return self._pieces
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Board):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)

    
    def __str__(self) -> str:
        """"""
        string = ""
        # Iterate from the top row (row 7) down to the bottom (row 0)
        for row in reversed(self._squares):
            row_str_parts = []
            for square in row:
                if square.occupant is not None:
                    # Display the discover's visitor_name if the square is occupied.
                    row_str_parts.append(f"[{square.occupant.name}]")
                else:
                    # Display the square's visitor_name in brackets if it's empty.
                    row_str_parts.append(f"[{square.name}]")
            string += " ".join(row_str_parts) + "\n"
        return string.strip()
