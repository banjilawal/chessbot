# chess/board/builder.py

"""
Module: chess.board.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List

from chess.coord import CoordBuilder
from chess.square import Square, SquareBuilder
from chess.board import Board, BoardBuildFailedException
from chess.system import BOARD_DIMENSION, Builder, BuildResult, IdValidator, id_emitter


class BoardBuilder(Builder[Board]):
    """
    # ROLE: Build
  
    # RESPONSIBILITIES:
    Create new Board objects safely.
  
    # PROVIDES:
      BuildResult[Board] containing either:
            - On success: Board in the payload.
            - On failure: Exception.
  
    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    def build(
            cls,
            id: int,
            num_rows: int=BOARD_DIMENSION,
            num_columns: int=BOARD_DIMENSION,
            id_validator: type[IdValidator]=IdValidator,
            coord_builder: type[CoordBuilder]=CoordBuilder,
            square_builder: type[SquareBuilder]=SquareBuilder
    ) -> BuildResult[Board]:
        """
        # Action:
        Construct a new Board object after verifying its inputs will not cause an error.
    
        # Parameters:
          * id (int): unique identifier.
          * num_rows (int): number of rows in the 2D array of Squares
          * num_columns (int): number of columns in the 2D array of Squares
          * id_validator (type[IdValidator]): sanity checks id parameter.
          * coord_builder (type[CoordBuilder]): Responsible for building Coord objects in the board.
          * square_builder (type[SquareBuilder]): Responsible for building Square objects in the board.
    
        # Returns:
          BuildResult[Board] containing either:
                - On success: Square in the payload.
                - On failure: Exception.
    
        # Raises:
            * BoardBuildFailedException:
        """
        method = "BoardBuilder.build"
        
        try:
            id_validation = id_validator.validate(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            squares: List[List[Square]] = []
            for i in range(num_rows):
                row_squares: List[Square] = []
                ascii_value = ord('A')
                
                for j in range(num_columns):
                    name = chr(ascii_value) + str(i + 1)
                    
                    coord_build_result = coord_builder.build(row=i, column=j)
                    if coord_build_result.is_failure():
                        return BuildResult.failure(coord_build_result.exception)
                    
                    square_build_result  = square_builder.build(
                        id=id_emitter.square_id,
                        name=name,
                        coord=coord_build_result.payload
                    )
                    
                    if square_build_result.is_failure():
                        return BuildResult.failure(square_build_result.exception)
                    
                    
                    row_squares.append(square_build_result.payload)
                    ascii_value += 1
                squares.append(row_squares)
            
            return BuildResult.success(payload=Board(id=id))
        
        except Exception as e:
            return BuildResult.failure(
                BoardBuildFailedException(
                    f"{method}: {BoardBuildFailedException.DEFAULT_MESSAGE}", e
                )
            )
