# src/chess/board/searcher/builder

"""
Module: chess.board.searcher.builder
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0
"""

from chess.arena import Arena, ArenaService
from chess.system import BuildResult, Builder, UnhandledRouteException, IdentityService, LoggingLevelRouter
from chess.board import BoardContext, BoardContextBuildFailedException


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
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: int,
            arena: Arena,
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[BoardContext]:
        """
        # ACTION:
            1.  Confirm that only one in the (id, arena) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a BoardContext and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # PARAMETERS:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[str])
                *   target (Optional[Coord])
            These Parameters must be provided:
                *   id_validator (type[IdValidator])
                *   name_validator (type[NameValidator])
                *   builder (type[CoordBuilder])

        # RETURNS:
        BuildResult[TeamSearchContext] containing either:
            - On success:   TeamSearchContext in the payload.
            - On failure:   Exception.

        # RAISES:
            *   ZeroBoardContextFlagsException
            *   BoardContextBuildFailedException
            *   ExcessiveBoardContextFlagsException
        """
        method = "BoardContextBuilder.builder"
        
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, arena]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which Boards match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroBoardFlagsException(f"{method}: {ZeroBoardFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveBoardContextFlagsException(f"{method}: {ExcessiveBoardContextFlagsException}")
                )
            # After verifying only one Player attribute-value-tuple is enabled, validate it.
            
            # Build the id BoardContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_BoardContext in the BuildResult.
                return BuildResult.success(BoardContext(id=id))
            
            # Build the arena BoardContext if its flag is enabled.
            if arena is not None:
                validation = arena_service.validate.validator(candidate=arena)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_BoardContext in the BuildResult.
                return BuildResult.success(BoardContext(arena=arena))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                UnhandledRouteException(f"{method}: {UnhandledRouteException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception, wrap an AgentContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                BoardContextBuildFailedException(f"{method}: {BoardContextBuildFailedException.DEFAULT_MESSAGE}")
            )