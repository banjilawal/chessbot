# src/chess/board/context/builder/builder.py

"""
Module: chess.board.context.builder.builder
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import Optional

from chess.arena import Arena, ArenaService
from chess.system import Builder, BuildResult, IdentityService
from chess.board import (
    BoardContextBuildRouteException, ZeroBoardContextFlagsException, BoardContext, BoardContextBuildFailedException,
    ExcessiveBoardContextFlagsException
)

class BoardContextBuilder(Builder[BoardContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce BoardContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of BoardContext instances that can be used safely by the client.
    3.  Ensure params for BoardContext creation have met the application's safety contract.
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
            arena: Optional[Arena] = None,
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[BoardContext]:
        """
        # ACTION:
            1.  If one-and-only-one context attribute is not null send an exception chain in the BuildResult.
            2.  If there is no build route for the not-null context attribute send an exception chain in the BuildResult.
            3.  If the build route exists and the context attribute is not verified send an exception chain in the 
                BuildResult. Else build the context and send it in the BuildResult's payload.
        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   arena Optional[(Arena)]
            These Parameters must be provided:
                *   arena_service (ArenaService)
                *   identity_service (IdentityService)
        # RETURNS:
            *   BuildResult[BoardContext] containing either:
                    - On failure: Exception.
                    - On success: BoardContext in the payload.
        # RAISES:
            *   ZeroBoardContextFlagsException
            *   BoardContextBuildFailedException
            *   ExcessiveBoardContextFlagsException
            *   BoardContextBuildRouteException
        """
        method = "BoardContextBuilder.build"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, arena]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BoardContextBuildFailedException(
                    message=f"{method}: {BoardContextBuildFailedException.DEFAULT_MESSAGE}",
                    ex=ZeroBoardContextFlagsException(
                        f"{method}: {ZeroBoardContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BoardContextBuildFailedException(
                    message=f"{method}: {BoardContextBuildFailedException.DEFAULT_MESSAGE}",
                    ex=ExcessiveBoardContextFlagsException(
                        f"{method}: {ExcessiveBoardContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the id BoardContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    BoardContextBuildFailedException(
                        message=f"{method}: {BoardContextBuildFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_BoardContext in the BuildResult.
            return BuildResult.success(BoardContext(id=id))
        
        # Build the arena BoardContext if its flag is enabled.
        if arena is not None:
            validation = arena_service.validator.validate(arena)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    BoardContextBuildFailedException(
                        message=f"{method}: {BoardContextBuildFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a arena_BoardContext in the BuildResult.
            return BuildResult.success(BoardContext(arena=arena))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            BoardContextBuildFailedException(
                message=f"{method}: {BoardContextBuildFailedException.DEFAULT_MESSAGE}",
                ex=BoardContextBuildRouteException(f"{method}: {BoardContextBuildRouteException.DEFAULT_MESSAGE}")
            )
        )