# src/chess/square/builder/builder.py

"""
Module: chess.square.builder.builder
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""

from typing import cast

from chess.board import Board, BoardService
from chess.coord import Coord, CoordService
from chess.square import AddingDuplicateSquareException, Square, SquareBuildFailedException, SquareContext
from chess.system import Builder, BuildResult, IdentityService, InvariantBreachException, LoggingLevelRouter, id_emitter


class SquareBuilder(Builder[Square]):
    """
     # ROLE: Builder, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce Square instances whose integrity is guaranteed at creation.
     2.  Manage construction of Square instances that can be used safely by the client.
     3.  Ensure params for Square creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
         *   SquareBuilder

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            board: Board,
            coord: Coord,
            name: str,
            id: int = id_emitter.square_id,
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Square]:
        """
        # ACTION:
            1.  If the id or name are not certified safe send an exception chain in the BuildResult. Else verify
                the coord param's correctness.
            2.  If the coord is not certified safe send an exception chain in the BuildResult. Else verify the board.
            3.  If the board is not certfied safe send an exception chain in the BuildResult. Else  create the
                square instance.
            4.  Register the squre with its board using the board's instance of BoardSquareService. If the
                registration is not successful send an exception chain in the BuildResult. Otherwise, send
                the successfully created sqaure in the BuildResult's payload.
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   cord (Coord)
            *   board (Board)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
            *   SquareBuildFailedException
        """
        method = "SquareBuilder.builder"
        
        # Handle the case that either id or name are not certified safe.
        identity_validation = identity_service.validate_identity(
            id_candidate=id,
            name_candidate=name
        )
        if identity_validation.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                SquareBuildFailedException(
                    message=f"{method}: {SquareBuildFailedException.DEFAULT_MESSAGE}",
                    ex=identity_validation.exception
                )
            )
        # Handle the case that the coord is not certified safe.
        coord_validation = coord_service.item_validator.validate(coord)
        if coord_validation.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                SquareBuildFailedException(
                    message=f"{method}: {SquareBuildFailedException.DEFAULT_MESSAGE}",
                    ex=coord_validation.exception
                )
            )
        # Handle the case that the board is not certified safe.
        board_validation = board_service.item_validator.validate(board)
        if board_validation.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                SquareBuildFailedException(
                    message=f"{method}: {SquareBuildFailedException.DEFAULT_MESSAGE}",
                    ex=board_validation.exception
                )
            )
        # Handle the case that the coord has already been assigned to a square.
        search_result = board.squares.search(context=SquareContext(coord=coord))
        if search_result.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                SquareBuildFailedException(
                    message=f"{method}: {SquareBuildFailedException.DEFAULT_MESSAGE}",
                    ex=search_result.exception
                )
            )
        # --- Create the Square. ---#
        
        square = Square(id=id, name=name, coord=coord, board=board)
        
        # If the square does not have  a fully bidirectional relationship with the board process the registration.
        relation_analysis = board_service.square_relation_analyzer.analyze(
            candidate_primary=board,
            candidate_satellite=square
        )
        # Handle the case that the relation analysis was not completed.
        if relation_analysis.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                SquareBuildFailedException(
                    message=f"{method}: {SquareBuildFailedException.DEFAULT_MESSAGE}",
                    ex=relation_analysis.exception
                )
            )
        # Handle the case that the board and square are not related.
        if relation_analysis.not_related:
            # On failure return the exception.
            return BuildResult.failure(
                SquareBuildFailedException(
                    message=f"{method}: {SquareBuildFailedException.DEFAULT_MESSAGE}",
                    ex=InvariantBreachException(
                        message=f"{method}:{InvariantBreachException.DEFAULT_MESSAGE}",
                    )
                )
            )
        # Handle the case that the board and square are have a fully bidirectional relationship.
        if relation_analysis.is_bidirectional:
            # On failure return the exception.
            return BuildResult.failure(
                SquareBuildFailedException(
                    message=f"{method}: {SquareBuildFailedException.DEFAULT_MESSAGE}",
                    ex=AddingDuplicateSquareException(
                        message=f"{method}:{AddingDuplicateSquareException.DEFAULT_MESSAGE}",
                    )
                )
            )
        # --- Last relationship state is a partial binding. This is the only case for registering the Square ---#
        
        # Handle the case that the insertion fails.
        insertion_result = board.squares.add(square=square)
        if insertion_result.is_failure:
            # On failure return the exception.
            return BuildResult.failure(
                SquareBuildFailedException(
                    message=f"{method}: {SquareBuildFailedException.DEFAULT_MESSAGE}",
                    ex=insertion_result.exception
                )
            )
        # --- On insertion success extract the insertion payload and send in the BuildResult. ---#
        return BuildResult.success(cast(Square, insertion_result.payload))

