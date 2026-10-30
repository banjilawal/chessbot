# src/transit/dispatcher/fabrication/search/stack/board/dispatcher.py

"""
Module: transit.dispatcher.fabrication.search.stack.board.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


class BoardContextBuilder(ContextBuilder[Board]):
    """
     Role:Build, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a BoardContext instance is certified safe, reliable, and consistent before use.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Super Class:
        *   Builder

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService()
    ) -> BuildResult[Board]:
        """
        # ACTION:
            1.  If Candidate fails existence or type checks return the exception chain in the BuildResult. Else,
                test how many optional attributes are not null.
            2.  If only one attribute is one and only one attribute is not null return the exception chain in the
                BuildResult.
            3.  If no route is found for the enabled attribute send an exception chain in the BuildResult.
            4.  If a build route exists return the outcome of the build to the caller.
        # PARAMETERS:
            *   rank (Any)
            *   arena_service (ArenaService)
            *   identity_service (IdentityService):
        # RETURNS:
            *   BuildResult[Board] containing either:
                    - On failure:   Exception.
                    - On success:   BoardContext in the payload.
        Raises:
            *   TypeError
            *   NullBoardContextException
            *   ZeroBoardContextFlagsException
            *   ArenaBoardContextFlagsException
            *   BoardContextBuildRouteException
            *   BoardContextBuilderException
        """
        method = "BoardContextBuilder.execute"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return BuildResult.failure(
                BoardContextBuilderException(
                    msg=f"{method}: {BoardContextBuilderException.MSG}",
                    ex=NullBoardContextException(f"{method}: {NullBoardContextException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, BoardContext):
            # Send the exception chain on failure.
            return BuildResult.failure(
                BoardContextBuilderException(
                    msg=f"{method}: {BoardContextBuilderException.MSG}",
                    ex=TypeError(f"{method}: Was expecting a BoardContext, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate into BoardContext for additional tests. ---#
        context = cast(BoardContext, priming.authorization_applicant)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return BuildResult.failure(
                BoardContextBuilderException(
                    msg=f"{method}: {BoardContextBuilderException.MSG}",
                    ex=ZeroBoardContextFlagsException(f"{method}: {ZeroBoardContextFlagsException.MSG}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return BuildResult.failure(
                BoardContextBuilderException(
                    msg=f"{method}: {BoardContextBuilderException.MSG}",
                    ex=ArenaBoardContextFlagsException(
                        f"{method}: {ArenaBoardContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate build branch. ---#
        
        # Build for the search-by-id target.
        if context.id is not None:
            build = identity_service.validate_id(candidate=context.id)
            if build.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    BoardContextBuilderException(
                        msg=f"{method}: {BoardContextBuilderException.MSG}",
                        ex=builder.exception
                    )
                )
            # On build success return the id_BoardContext in the BuildResult.
            return BuildResult.success(payload=context)
        
        # Build for the search-by-arena target.
        if context.arena is not None:
            build = arena_service.execute.search_service(context.arena)
            if build.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    BoardContextBuilderException(
                        msg=f"{method}: {BoardContextBuilderException.MSG}",
                        ex=builder.exception
                    )
                )
            # On build success return the arena_BoardContext in the BuildResult.
            return BuildResult.success(payload=context)
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            BoardContextBuilderException(
                msg=f"{method}: {BoardContextBuilderException.MSG}",
                ex=BoardContextBuildRouteException(
                    f"{method}: {BoardContextBuildRouteException.MSG}"
                )
            )
        )