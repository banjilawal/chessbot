# chess/board_validator/old_occupation_validator.py

"""
Module: `chess.board_validator.validator`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

 Provides: Create `Board` instances

Contains:
  * `BoardBuilder`
"""

from typing import List, Type

from chess.coord import CoordBuilder
from chess.square import Square, SquareBuilder
from chess.board import Board, BoardBuildFailedException
from chess.system import BOARD_DIMENSION, Builder, BuildResult, IdValidator


class BoardBuilder(Builder[Board]):
    """
    # ROLE: Build
  
    # RESPONSIBILITIES:
    Create new Board objects safely.
  
    # PROVIDES:
      BuildResult[Board] containing either:
            - On success: Board in payload.
            - On failure: Exception.
  
    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    def build(
            cls,
            id: int,
            id_validator: Type[IdValidator]=IdValidator,
            coord_builder: Type[CoordBuilder]=CoordBuilder,
            square_builder: Type[SquareBuilder]=SquareBuilder
    ) -> BuildResult[Board]:
        """
        # Action:
        Construct a new Board object after verifying its inputs will not cause an error.
    
        # Parameters:
          * piece (Piece): The board owner
          * board (Board): Provides the Square of the Board owner.
          * board_origin_builder (BoardOriginBuilder): Creates the BoardOwner object.
    
        # Returns:
          BuildResult[Board] containing either:
                - On success: Square in payload.
                - On failure: Exception.
    
        # Raises:
            * TypeError
            * NullBoardException
            * BoardNullSquaresListException
            * BoardNullEnemiesDictException
            * BoardNullFriendsDictException
            * InvalidBoardException
        """
        method = "BoardBuilder.build"
        
        try:
            id_validation = id_validator.validate(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            squares: List[List[Square]] = []
            for i in range(BOARD_DIMENSION):
                row_squares: List[Square] = []
                ascii_value = ord('A')
                
                for j in range(BOARD_DIMENSION):
                    name = chr(ascii_value) + str(i + 1)
                    board = Board(row=i, column=j)
                    square = Square(name, board)
                    
                    row_squares.append(square)
                    ascii_value += 1
                squares.append(row_squares)
            
            return BuildResult.success(payload=Board(squares=squares))
        
        except Exception as e:
            return BuildResult.failure(
                BoardBuildFailedException(
                    f"{method}: {BoardBuildFailedException.DEFAULT_MESSAGE}",
                    e
                )
            )
