# src/toolkit/context/board/toolkit.py

"""
Module: toolkit.context.board.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Optional

from logic.arena import Arena, ArenaService
from system import Toolkit, ToolkitResult, IdentityService
from logic.board import (
    BoardContextToolkitRouteException, ZeroBoardContextFlagsException, BoardContext, BoardContextToolkitException,
    ArenaBoardContextFlagsException
)

class BoardContextToolkit(Toolkit[BoardContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Toolkit Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> ToolkitResult[Token]

     Super Class:
         Toolkit
     """
    @classmethod
    def __init__(
            self,
            id: Optional[int] = None,
            arena: Optional[Arena] = None,
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ToolkitResult[BoardContext]:
        """
        # ACTION:
            1.  If one-and-only-one context attribute is not null send an exception chain in the ToolkitResult.
            2.  If there is no toolkit route for the not-null context attribute send an exception chain in the ToolkitResult.
            3.  If the toolkit route exists and the context attribute is not verified send an exception chain in the
                ToolkitResult. Else toolkit the context and send it in the ToolkitResult's payload.
        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   arena Optional[(Arena)]
            These Parameters must be provided:
                *   arena_service (ArenaService)
                *   identity_service (IdentityService)
        # RETURNS:
            *   ToolkitResult[BoardContext] containing either:
                    - On failure: Exception.
                    - On success: BoardContext in the payload.
        Raises:
            *   ZeroBoardContextFlagsException
            *   BoardContextToolkitException
            *   ArenaBoardContextFlagsException
            *   BoardContextToolkitRouteException
        """
        method = "BoardContextToolkit.toolkit"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, arena]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return ToolkitResult.failure(
                BoardContextToolkitException(
                    msg=f"{method}: {BoardContextToolkitException.MSG}",
                    ex=ZeroBoardContextFlagsException(
                        f"{method}: {ZeroBoardContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return ToolkitResult.failure(
                BoardContextToolkitException(
                    msg=f"{method}: {BoardContextToolkitException.MSG}",
                    ex=ArenaBoardContextFlagsException(
                        f"{method}: {ArenaBoardContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/toolkit branch. ---#
        
        # Toolkit the id BoardContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ToolkitResult.failure(
                    BoardContextToolkitException(
                        msg=f"{method}: {BoardContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_BoardContext in the ToolkitResult.
            return ToolkitResult.success(BoardContext(id=id))
        
        # Toolkit the arena BoardContext if its flag is enabled.
        if arena is not None:
            validation = arena_service.validator.search_service(arena)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ToolkitResult.failure(
                    BoardContextToolkitException(
                        msg=f"{method}: {BoardContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a arena_BoardContext in the ToolkitResult.
            return ToolkitResult.success(BoardContext(arena=arena))
        
        # Return the exception chain if there is no toolkit route for the context.
        return ToolkitResult.failure(
            BoardContextToolkitException(
                msg=f"{method}: {BoardContextToolkitException.MSG}",
                ex=BoardContextToolkitRouteException(f"{method}: {BoardContextToolkitRouteException.MSG}")
            )
        )