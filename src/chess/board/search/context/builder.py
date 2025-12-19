# src/chess/board/searcher/context/builder

"""
Module: chess.board.searcher.context.builder
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0
"""

from chess.arena import Arena, ArenaService
from chess.system import BuildResult, Builder, FailsafeBranchExitPointException, IdentityService, LoggingLevelRouter
from chess.board import BoardContext, BoardContextBuildFailedException


class BoardContextBuilder(Builder[BoardContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Manage construction of BoardSearch instances that can be used safely by the client.
    2.  Ensure params for BoardSearch creation have met the application's safety contract.
    3.  Provide pluggable factories for creating different TeamSearchContext products.


    # PROVIDES:
    ValidationResult[TeamSearchContext] containing either:
        - On success:   TeamSearchContext in the payload.
        - On failure:   Exception.

    # ATTRIBUTES:
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
        # Action:
            1.  Use dependency injected validators to verify correctness of parameters required to
                builder a TeamSearchContext instance.
            2.  If the parameters are safe the TeamSearchContext is built and returned.

        # Parameters:
            *   id (Optional[int]):                     Selected if searcher target is an id.
            *   designation (Optional[str]):                   Selected if searcher target is a designation.
            *   target (Optional[Coord]):                Selected if searcher target is a target.
            *   id_validator (type[IdValidator]):       Validates an id-searcher-target
            *   name_validator (type[NameValidator]):   Validates a designation-searcher-target
            *   builder (type[CoordBuilder]):     Validates a target-searcher-target

        # Returns:
        BuildResult[TeamSearchContext] containing either:
            - On success:   TeamSearchContext in the payload.
            - On failure:   Exception.

        # Raises:
            *   BoardContextBuildFailedException
            *   NoBoardSearchOptionSelectedException
            *   MoreThanOneBoardSearchOptionPickedException
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
            # After verifying only one PlayerAgent attribute-value-tuple is enabled, validate it.
            
            # Build the id BoardContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_BoardContext in the BuildResult.
                return BuildResult.success(BoardContext(id=id))
            
            # Build the arena BoardContext if its flag is enabled.
            if arena is not None:
                validation = arena_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_BoardContext in the BuildResult.
                return BuildResult.success(BoardContext(arena=arena))
            
            # As a failsafe send a buildResult failure if a context path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        # Finally, if there is an unhandled exception Wrap an AgentContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                BoardContextBuildFailedException(f"{method}: {BoardContextBuildFailedException.DEFAULT_MESSAGE}")
            )