# src/chess/arena/context/builder/builder.py

"""
Module: chess.arena.context.builder.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional

from chess.game import Game, GameService
from chess.team import Team, TeamService
from chess.system import Builder, BuildResult, FailsafeBranchExitPointException, IdentityService, LoggingLevelRouter
from chess.arena import (
    ArenaContext, ArenaContextBuildFailedException, ExcessiveArenaContextFlagsException, ZeroArenaContextFlagsException,
)


class ArenaContextBuilder(Builder[ArenaContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce ArenaContext instances whose integrity is always guaranteed.
    2.  Manage construction of ArenaContext instances that can be used safely by the client.
    3.  Ensure params for ArenaContext creation have met the application's safety contract.
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
            id: Optional[int] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            game: Optional[Game] = None,
            variety: Optional[ArenaVariety] = None,
            team_service: TeamService = TeamService(),
            game_service: GameService = GameService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[ArenaContext]:
        """
        # Action:
            1.  Confirm that only one in the (id, designation, team, game, arena_variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a ArenaContext and send in a BuildResult. Else, send an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[str])
                *   team (Optional[Team])
                *   game (Optional[Game])
                *   arena_variety (Optional[ArenaVariety])

            These Parameters must be provided:
                *   team_service (TeamService)
                *   game_service (GameService)
                *   identity_service (IdentityService)

        # Returns:
          BuildResult[ArenaContext] containing either:
                - On success: ArenaContext in the payload.
                - On failure: Exception.

        # Raises:
            *   ZeroArenaContextFlagsException
            *   ArenaContextBuildFailedException
            *   ExcessiveArenaContextFlagsException
        """
        method = "ArenaSearchContextBuilder.builder"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, team, game, variety, ]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerArenas match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroArenaContextFlagsException(f"{method}: {ZeroArenaContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveArenaContextFlagsException(f"{method}: {ExcessiveArenaContextFlagsException}")
                )
            # After verifying only one PlayerArena attribute-value-tuple is enabled, validate it.
            
            # Build the id ArenaContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_ArenaContext in the BuildResult.
                return BuildResult.success(ArenaContext(id=id))
            
            # Build the name ArenaContext if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a name_ArenaContext in the BuildResult.
                return BuildResult.success(ArenaContext(name=name))
            
            # Build the team ArenaContext if its flag is enabled.
            if team is not None:
                validation = team_service.validator.validate(candidate=team)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a team_ArenaContext in the BuildResult.
                return BuildResult.success(ArenaContext(team=team))
            
            # Build the game ArenaContext if its flag is enabled.
            if game is not None:
                validation = game_service.validator.validate(candidate=game)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a game_ArenaContext in the BuildResult.
                return BuildResult.success(ArenaContext(game=game))
            
            # Build the arena_variety ArenaContext if its flag is enabled.
            if variety is not None:
                if not isinstance(variety, ArenaVariety):
                    return BuildResult.failure(
                        TypeError(f"{method}: Expected ArenaVariety, got {type(variety).__name__} instead.")
                    )
                # On validation success return a variety_ArenaContext in the BuildResult.
                return BuildResult.success(ArenaContext(variety=variety))
            
            # As a failsafe send a buildResult failure if a context path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        # Finally, if there is an unhandled exception Wrap an ArenaContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                ArenaContextBuildFailedException(
                    ex=ex, message=f"{method}: {ArenaContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )