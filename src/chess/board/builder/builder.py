# src/chess/board/builder/builder

"""
Module: chess.board.builder.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List, cast

from chess.coord import Coord, CoordService
from chess.square import SquareBuilder, SquareService, UniqueSquareDataService
from chess.board import Board, BoardBuildFailedException
from chess.system import BOARD_DIMENSION, Builder, BuildResult, IdentityService


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
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            
            square_data: UniqueSquareDataService = UniqueSquareDataService(),
    ) -> BuildResult[Board]:
        """
        # Action:
        Construct a new Board object after verifying its inputs will not cause an error.
    
        # Parameters:
          * id (int): unique identifier.
          * num_rows (int): number of rows in the 2D array of Squares
          * num_columns (int): number of columns in the 2D array of Squares
          * id_validator (type[IdValidator]): sanity checks id parameter.
          * builder (type[CoordBuilder]): Responsible for building Coord objects in the board.
          * square_builder (type[SquareBuilder]): Responsible for building Square objects in the board.
    
        # Returns:
          BuildResult[Board] containing either:
                - On success: Square in the payload.
                - On failure: Exception.
    
        # Raises:
            * BoardBuildFailedException:
        """
        method = "BoardBuilder.builder"
        
        try:
            id_validation = identity_service.validate_id(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)


            for i in range(num_rows):
                ascii_value = ord('A')
                
                for j in range(num_columns):
                    name = chr(ascii_value) + str(i + 1)
                    
                    coord_build_result = coord_service.builder.build(row=i, column=j)
                    if coord_build_result.is_failure():
                        return BuildResult.failure(coord_build_result.exception)
   
                    square_build_result = square_data.service.builder.build(
                        id=identity_service.id_emitter.square_id,
                        name=name,
                        coord=coord_build_result.payload
                    )
                    if square_build_result.is_failure():
                        return BuildResult.failure(square_build_result.exception)
                    
                    addition_result = square_data.push_unique(square=square_build_result.payload)
                    if addition_result.is_failure():
                        return BuildResult.failure(addition_result.exception)
                    ascii_value += 1
                
            
            return BuildResult.success(payload=Board(id=id, square_service=square_data))
        
        except Exception as e:
            return BuildResult.failure(
                BoardBuildFailedException(
                    f"{method}: {BoardBuildFailedException.DEFAULT_MESSAGE}", e
                )
            )
