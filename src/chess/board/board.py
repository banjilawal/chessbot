# src/chess/board/board.py

"""
Module: chess.board.board
Author: Banji Lawal
Created: 2025-07-31
version: 1.0.0
"""


from chess.game import Game
from chess.piece import UniquePieceDataService
from chess.square import UniqueSquareDataService
from chess.token.service import UniquePieceDataServiceException



class Board:
    """
    # ROLE: Data-Holder/Data Owner
  
    # RESPONSIBILITIES:
    The Surface of Squares where Pieces are played.
  
    # PROVIDES:
      Board
  
    # ATTRIBUTES:
        * id (int): Unique identifier.
        * pieces ([Token]): Array pieces in Board object
        * squares ([[Square]]): A 2D array of squares in Board object.
    """
    
    _id: int
    _game: Game
    _piece_service: UniquePieceDataService
    _square_service: UniqueSquareDataService
    
    def __init__(
            self,
            id: int,
            game: Game,
            piece_service: UniquePieceDataService = UniquePieceDataServiceException(),
            square_service: UniqueSquareDataService = UniqueSquareDataService(),
    ):
        """
        # ACTION:
        Constructs Board object
    
        # PARAMETERS:
          * id (int):
    
        # RETURNS:
        None
    
        # RAISES:
        None
        """
        method = "Board.__init__"
        
        self._id = id
        self._game = game
        self._piece_service = piece_service
        self._square_service = square_service
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def game(self) -> Game:
        return self._game
    
    @@property
    def piece_service(self) -> UniquePieceDataService:
        return self._piece_service
    
    @@property
    def square_service(self) -> UniqueSquareDataService:
        return self._square_service
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Board):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)

    
    # def __str__(self) -> str:
    #     """"""
    #     string = ""
    #     # Iterate from the top row (row 7) down to the bottom (row 0)
    #     for row in reversed(self._squares):
    #         row_str_parts = []
    #         for square_name in row:
    #             if square_name.occupant is not None:
    #                 # Display the discover's visitor_name if the square_name is occupied.
    #                 row_str_parts.append(f"[{square_name.occupant.designation}]")
    #             else:
    #                 # Display the square_name's visitor_name in brackets if it's empty.
    #                 row_str_parts.append(f"[{square_name.designation}]")
    #         string += " ".join(row_str_parts) + "\n"
    #     return string.strip()
