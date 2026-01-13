# src/chess/square/builder/builder.py

"""
Module: chess.square.builder.builder
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from typing import Optional

from chess.board import Board, BoardService
from chess.coord import Coord, CoordService
from chess.system import Builder, BuildResult, IdentityService
from chess.square import (
    SquareContextBuildRouteException, ZeroSquareContextFlagsException, SquareContext, SquareContextBuildFailedException,
    ExcessiveSquareContextFlagsException
)


class SquareContextBuilder(Builder[SquareContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce TeamContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of TeamContext instances that can be used safely by the client.
    3.  Ensure params for TeamContext creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
    None

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
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[SquareContext]:
        """
        # ACTION:
            1.  If the candidate fails existence or type tests send the exception in the ValidationResult.
                Else, cast to TeamContext instance context.
            2.  If one-and-only-one context attribute is not null return an exception in the ValidationResult.
            3.  If there is no certification route for the attribute return an exception in the ValidationResult.
            4.  If the certification route exists use the appropriate service or validator to send either an exception
                chain the ValidationResult or the context.
        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   null Optional[(str)]
                *   cord Optional[(Coord)]
                *   board Optional[(Board)]
            These Parameters must be provided:
                *   board_service (BoardService)
                *   coord_service (CoordService)
                *   identity_service (IdentityService)
        # RETURNS:
            *   BuildResult[SquareContext] containing either:
                - On success: SquareContext in the payload.
                - On failure: Exception.

        # RAISES:
            *   ZeroSnapshotContextFlagsException
            *   SnapshotContextBuildFailedException
            *   ExcessiveSnapshotContextFlagsException
            *   SnapshotContextBuildRouteException
        """
        method = "SquareContextBuilder.build"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, name, coord]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareContextBuildFailedException(
                    message=f"{method}: {SquareContextBuildFailedException.DEFAULT_MESSAGE}",
                    ex=ZeroSquareContextFlagsException(
                        f"{method}: {ZeroSquareContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareContextBuildFailedException(
                    message=f"{method}: {SquareContextBuildFailedException.DEFAULT_MESSAGE}",
                    ex=ExcessiveSquareContextFlagsException(
                        f"{method}: {ExcessiveSquareContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the id SquareContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareContextBuildFailedException(
                        message=f"{method}: {SquareContextBuildFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_SquareContext in the BuildResult.
            return BuildResult.success(SquareContext(id=id))
        
        # Build the name SquareContext if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareContextBuildFailedException(
                        message=f"{method}: {SquareContextBuildFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_SquareContext in the BuildResult.
            return BuildResult.success(SquareContext(name=name))
        
        # Build the coord SquareContext if its flag is enabled.
        if coord is not None:
            validation = coord_service.validator.validate(coord)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareContextBuildFailedException(
                        message=f"{method}: {SquareContextBuildFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a coord_SquareContext in the BuildResult.
            return BuildResult.success(SquareContext(coord=coord))
        
        # Build the board SquareContext if its flag is enabled.
        if board is not None:
            validation = board_service.validator.validate(candidate=board)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareContextBuildFailedException(
                        message=f"{method}: {SquareContextBuildFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a board_SquareContext in the BuildResult.
            return BuildResult.success(SquareContext(board=board))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            SquareContextBuildFailedException(
                message=f"{method}: {SquareContextBuildFailedException.DEFAULT_MESSAGE}",
                ex=SquareContextBuildRouteException(f"{method}: {SquareContextBuildRouteException.DEFAULT_MESSAGE}")
            )
        )