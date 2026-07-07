# src/builder/board/builder.py

"""
Module: builder.board.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from logic.arena import Arena, ArenaService
from logic.board import ArenaAlreadyContainsBoardException, Board, BoardBuilderException
from system import Builder, BuildResult, BOARD_DIMENSION, IdentityService, LoggingLevelRouter, id_emitter


class BoardBuilder(Builder[Board]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Board instance is born safe and reliable.

    Attributes:

    Provides:
        def build(
                cls,
                arena: Arena,
                id: int = id_emitter.board_id,
                NUMBER_OF_ROWS: int = BOARD_DIMENSION,
                column_size: int = BOARD_DIMENSION,
                arena_service: ArenaService = ArenaService(),
                identity_service: IdentityService = IdentityService(),
        ) -> BuildResult[Board]:

     Super Class:
         Builder
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
            1.  If the id or schema are not certified safe send an exception chain in the BuildResult.
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
        Raises:
            *   BoardBuilderException
            *   ArenaAlreadyContainsBoardException
        """
        method = "BoardBuilder.build"
        
        # Handle the case that, the idis not safe.
        id_validation = identity_service.validate_id(candidate=id)
        if id_validation.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                BoardBuilderException(
                    msg=f"{method}: {BoardBuilderException.ERR_CODE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that, the arenais not safe.
        arena_validation = arena_service.run.search_service(candidate=arena)
        if arena_validation.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                BoardBuilderException(
                    msg=f"{method}: {BoardBuilderException.ERR_CODE}",
                    ex=arena_validation.exception
                )
            )
        # Handle the case that, the arena already contains a board.
        if arena.board is not None:
            # On failure return the exception.
            return BuildResult.failure(
                BoardBuilderException(
                    msg=f"{method}: {BoardBuilderException.ERR_CODE}",
                    ex=ArenaAlreadyContainsBoardException(f"{method}: {ArenaAlreadyContainsBoardException.MSG}")
                )
            )
        # Create the board.
        board = Board(id=id, arena=arena, NUMBER_OF_ROWS=NUMBER_OF_ROWS, column_size=column_size)
        
        # --- Can directly bind the board to the arena in a new build without arena_service.insert_board here. ---#
        arena.board = board
        # Send the new board in the BuildResult's payload.
        return BuildResult.success(payload=board)

