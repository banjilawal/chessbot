# src/chess/square/context/builder/builder.py

"""
Module: chess.square.context.builder.builder
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from typing import Optional

from chess.board import Board
from chess.coord import Coord, CoordService
from chess.system import Builder, BuildResult, IdentityService
from chess.square import (
    NoSquareContextFlagSetException, SquareContext, SquareContextBuildFailedException,
    ExcessiveSquareContextFlagsSetException
)


class SquareContextBuilder(Builder[SquareContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce SquareContext instances whose integrity is always guaranteed.
     2.  Manage construction of SquareContext instances that can be used safely by the client.
     3.  Ensure params for SquareContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
         *   SquareContextBuilder

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    
    @classmethod
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            coord: Optional[Coord] = None,
            board: Optional[Board] = None,
            coord_service: CoordService = CoordService(),
            idservice: IdentityService = IdentityService(),
    ) -> BuildResult[SquareContext]:
        """
        # ACTION:
        1.  Verify only one param is turned on.
        2.  If either id or designation is turned on verify them with identity_service.
        2.  If the coord is turned on verify with coord_service.
        3.  Run board-integrity checks with board_service.
        4.  If any checks fail, send their exception to the caller in a BuildResult.
        5.  When all checks pass, create a new Square object then send to the caller in a BuildResult.

        # PARAMETERS:
            *   id (int)
            *   designation (str)
            *   cord (Coord)
            *   board (Board)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[Square] containing either:
            - On success: Square in the payload.
            - On failure: Exception.

        # Raises:
            *   SquareBuildFailedException
        """
        method = "SquareContextBuilder.build"
        try:
            # Start err
            params = [id, name, coord]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoSquareContextFlagSetException(f"{method}: {NoSquareContextFlagSetException.DEFAULT_MESSAGE}")
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveSquareContextFlagsSetException(
                        f"{method}: {ExcessiveSquareContextFlagsSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if id is not None:
                id_validation = idservice.validate_id(candidate=id)
                if id_validation.is_failure:
                    return BuildResult.failure(id_validation.exception)
                return BuildResult.success(SquareContext(id=id))
            
            if name is not None:
                name_validation = idservice.validate_name(candidate=name)
                if name_validation.is_failure:
                    return BuildResult.failure(name_validation.exception)
                return BuildResult.success(SquareContext(name=name))
            
            if coord is not None:
                coord_validation = coord_service.item_validator.validate(coord)
                if coord_validation.is_failure:
                    return BuildResult.failure(coord_validation.exception)
                return BuildResult.success(SquareContext(coord=coord))
            
        # Finally, if there is an unhandled exception Wrap an SquareContextBuildFailedException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                SquareContextBuildFailedException(
                    ex=ex, message=f"{method}: {SquareContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )