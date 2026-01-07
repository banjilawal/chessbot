# src/chess/board/board.py

"""
Module: chess.board.board
Author: Banji Lawal
Created: 2025-07-31
version: 1.0.0
"""


from chess.arena import Arena
from chess.system import InsertionResult
from chess.team import Team, TeamService
from chess.token import Token, TokenService, UniqueTokenDataService
from chess.square import UniqueSquareDataService
from chess.token.service import UniqueTokenDataServiceException



class Board:
    """
    # ROLE: Data-Holder/Data Owner
  
    # RESPONSIBILITIES:
    The Surface of Squares where Tokens are played.
  
    # PROVIDES:
      Board
  
    # ATTRIBUTES:
        * id (int): Unique identifier.
        * tokens ([Token]): Array tokens in Board object
        * squares ([[Square]]): A 2D array of squares in Board object.
    """
    
    _id: int
    _arena: Arena
    _tokens: UniqueTokenDataService
    _squares: UniqueSquareDataService
    
    def __init__(
            self,
            id: int,
            arena: Arena,
            tokens: UniqueTokenDataService = UniqueTokenDataServiceException(),
            squares: UniqueSquareDataService = UniqueSquareDataService(),
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
        self._arena = arena
        self._tokens = tokens
        self._squares = squares
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @@property
    def tokens(self) -> UniqueTokenDataService:
        return self._tokens
    
    @@property
    def squares(self) -> UniqueSquareDataService:
        return self._squares
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Board):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def accept_token(
            self,
            token: Token,
            token_service: TokenService = TokenService()
    ) -> InsertionResult[Token]:
        token_validation = token_service.validator.validate(token)
        if token_validation.is_failure:
            return InsertionResult.failure(
                Board
            )
        

    
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
