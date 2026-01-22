# src/chess/board/builder/builder.py

"""
Module: chess.board.builder.builder
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""

from chess.arena import Arena, ArenaService
from chess.board import ArenaAlreadyContainsBoardException, Board, BoardBuildFailedException
from chess.system import Builder, BuildResult, BOARD_DIMENSION, IdentityService, LoggingLevelRouter, id_emitter


class BoardBuilder(Builder[Board]):
    """
     # ROLE: Builder, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce Board instances whose integrity is guaranteed at creation.
     2.  Manage construction of Board instances that can be used safely by the client.
     3.  Ensure params for Board creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
         *   BoardBuilder

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            arena: Arena,
            id: int = id_emitter.board_id,
            NUMBER_OF_ROWS: int = BOARD_DIMENSION,
            column_size: int = BOARD_DIMENSION,
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Board]:
        """
        # ACTION:
            1.  If the id or name are not certified safe send an exception chain in the BuildResult.
            2.  If the arena fails its integrity checks send an exception chain in the BuildResult.
            3.  Create a Board instance board then register it with the arena using ArenaBoardService.
            4.  If the registration is not successful send an exception chain in the BuildResult. Otherwise, send
                the successfully created board in the BuildResult's payload.
        # PARAMETERS:
            *   id (int)
            *   arena (Arena)
            *   NUMBER_OF_ROWS (int)
            *   column_size (int)
            *   arena_service (ArenaService)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[Board] containing either:
                    - On failure: Exception.
                    - On success: Board in the payload.
        # RAISES:
            *   BoardBuildFailedException
            *   ArenaAlreadyContainsBoardException
        """
        method = "BoardBuilder.builder"
        
        # Handle the case that the id is not certified safe.
        id_validation = identity_service.validate_id(candidate=id)
        if id_validation.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                BoardBuildFailedException(
                    message=f"{method}: {BoardBuildFailedException.ERROR_CODE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that the arena is not certified safe.
        arena_validation = arena_service.validator.validate(candidate=arena)
        if arena_validation.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                BoardBuildFailedException(
                    message=f"{method}: {BoardBuildFailedException.ERROR_CODE}",
                    ex=arena_validation.exception
                )
            )
        # Handle the case that the arena already contains a board.
        if arena.board is not None:
            # On failure return the exception.
            return BuildResult.failure(
                BoardBuildFailedException(
                    message=f"{method}: {BoardBuildFailedException.ERROR_CODE}",
                    ex=ArenaAlreadyContainsBoardException(f"{method}: {ArenaAlreadyContainsBoardException.DEFAULT_MESSAGE}")
                )
            )
        # Create the board.
        board = Board(id=id, arena=arena, NUMBER_OF_ROWS=NUMBER_OF_ROWS, column_size=column_size)
        
        # --- Can directly bind the board to the arena in a new build without arena_service.insert_board here. ---#
        arena.board = board
        # Send the new board in the BuildResult's payload.
        return BuildResult.success(payload=board)

