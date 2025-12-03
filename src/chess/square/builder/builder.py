# src/chess/square/builder/builder.py

"""
Module: chess.square.builder.builder
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""
from chess.board import Board, BoardIntegrityService
from chess.coord import Coord, CoordIntegrityService
from chess.square import Square, SquareBuildFailedException, SquareValidator
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter, id_emitter


class SquareBuilder(Builder[Square]):
    """
    # ROLE: Builder, Data Integrity Guarantor

    # RESPONSIBILITIES:
    Produce Square instances whose integrity is always guaranteed. If any
    attributes do not pass their integrity checks, send an exception instead.

    # PROVIDES:
    BuildResult[Square] containing either:
        - On success: Coord in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            name: str,
            board: Board,
            coord: Coord,
            id: int = id_emitter.square_id,
            board_service: BoardIntegrityService = BoardIntegrityService(),
            coord_service: CoordIntegrityService = CoordIntegrityService(),
            square_validator: SquareValidator = SquareValidator(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Square]:
        """
        # ACTION:
        1.  Run identity-integrity checks with identity_service.
        2.  Run coord-integrity checks with coord_service.
        3.  Run board-integrity checks with board_service.
        4.  If any checks fail, send their exception to the caller in a BuildResult.
        5.  When all checks pass, create a new Square object then send to the caller in a BuildResult.
    
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   cord (Coord)
            *   board (Board)
            *   board_service (BoardIntegrityService)
            *   coord_service (CoordIntegrityService)
            *   identity_service (IdentityService)
    
        # Returns:
        ValidationResult[Square] containing either:
            - On success: Square in the payload.
            - On failure: Exception.
    
        # Raises:
            *   SquareBuildFailedException
        """
        method = "SquareBuilder.builder"
        
        try:
            identity_validation = identity_service.validate_identity(
                id_candidate=id,
                name_candidate=name
            )
            if identity_validation.is_failure():
                return BuildResult.failure(identity_validation.exception)
            
            coord_validation = coord_service.item_validator.validate(coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            board_validation = board_service.item_validator.validate(board)
            if board_validation.is_failure():
                return BuildResult.failure(board_validation.exception)
            
            return BuildResult.success(
                payload=Square(
                    id=id,
                    name=name,
                    coord=coord,
                    board=board)
            )
        
        except Exception as ex:
            return BuildResult(
                SquareBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{SquareBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )