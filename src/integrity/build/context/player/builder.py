# src/integrity/build/context/player/builder.py

"""
Module: integrity.build.context.player.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model.game import Game, GameService
from logic.team import Team, TeamService
from system import Builder, BuildResult, ExecutionRouteException, IdentityService, LoggingLevelRouter
from logic.agent import (
    AgentVariety, PlayerContextBuilder, PlayerContextBuilderBuildException, ZeroPlayerContextBuilderFlagsException,
    ArenaPlayerContextBuilderFlagsException
)



class PlayerContextBuilder(Builder[PlayerContextBuilder]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

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
            ) -> BuildResult[Token]

     Super Class:
         Builder
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            game: Optional[Game] = None,
            variety: Optional[AgentVariety] = None,
            team_service: TeamService = TeamService(),
            game_service: GameService = GameService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[PlayerContextBuilder]:
        """
        # ACTION:
            1.  Confirm that only one in the (id, designation, team, game, agent_variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a PlayerContextBuilder and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # PARAMETERS:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[str])
                *   team (Optional[Team])
                *   game (Optional[Game])
                *   agent_variety (Optional[AgentVariety])
    
            These Parameters must be provided:
                *   team_service (TeamService)
                *   game_service (GameService)
                *   identity_service (IdentityService)

        # RETURNS:
          BuildResult[PlayerContextBuilder] containing either:
                - On success: PlayerContextBuilder in the payload.
                - On failure: Exception.

        Raises:
            *   ZeroPlayerContextBuilderFlagsException
            *   PlayerContextBuilderBuildException
            *   ArenaPlayerContextBuilderFlagsException
        """
        method = "AgentSearchContextBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, team, game, variety,]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerAgents match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroPlayerContextBuilderFlagsException(f"{method}: {ZeroPlayerContextBuilderFlagsException.MSG}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ArenaPlayerContextBuilderFlagsException(f"{method}: {ArenaPlayerContextBuilderFlagsException}")
                )
            # After verifying only one Player attribute-value-tuple is enabled, validate it.
            
            # Build the id PlayerContextBuilder if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_PlayerContextBuilder in the BuildResult.
                return BuildResult.success(PlayerContextBuilder(id=id))
            
            # Build the schema PlayerContextBuilder if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a name_PlayerContextBuilder in the BuildResult.
                return BuildResult.success(PlayerContextBuilder(name=name))
            
            # Build the team PlayerContextBuilder if its flag is enabled.
            if team is not None:
                validation = team_service.validator.validate(candidate=team)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a team_PlayerContextBuilder in the BuildResult.
                return BuildResult.success(PlayerContextBuilder(team=team))
            
            # Build the game PlayerContextBuilder if its flag is enabled.
            if game is not None:
                validation = game_service.validator.validate(candidate=game)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a game_PlayerContextBuilder in the BuildResult.
                return BuildResult.success(PlayerContextBuilder(game=game))
            
            # Build the agent_variety PlayerContextBuilder if its flag is enabled.
            if variety is not None:
                if not isinstance(variety, AgentVariety):
                    return BuildResult.failure(
                        TypeError(f"{method}: Expected AgentVariety, got {type(variety).__name__} instead.")
                    )
                # On validation success return a variety_PlayerContextBuilder in the BuildResult.
                return BuildResult.success(PlayerContextBuilder(variety=variety))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                ExecutionRouteException(f"{method}: {ExecutionRouteException.MSG}")
            )
        # Finally, catch any missed exception, wrap an PlayerContextBuilderBuildException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                PlayerContextBuilderBuildException(
                    ex=ex, msg=f"{method}: {PlayerContextBuilderBuildException.MSG}"
                )
            )