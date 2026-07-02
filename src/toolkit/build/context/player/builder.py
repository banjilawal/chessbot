# src/toolkit/context/player/toolkit.py

"""
Module: toolkit.context.player.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model.game import Game, GameService
from logic.team import Team, TeamService
from system import Toolkit, ToolkitResult, ExecutionRouteException, IdentityService, LoggingLevelRouter
from logic.agent import (
    AgentVariety, PlayerContextToolkit, PlayerContextToolkitToolkitException, ZeroPlayerContextToolkitFlagsException,
    ArenaPlayerContextToolkitFlagsException
)



class PlayerContextToolkit(Toolkit[PlayerContextToolkit]):
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
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            game: Optional[Game] = None,
            variety: Optional[AgentVariety] = None,
            team_service: TeamService = TeamService(),
            game_service: GameService = GameService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ToolkitResult[PlayerContextToolkit]:
        """
        # ACTION:
            1.  Confirm that only one in the (id, designation, team, game, agent_variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass toolkit a PlayerContextToolkit and send in a ToolkitResult. Else, return an exception
                in the ToolkitResult.

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
          ToolkitResult[PlayerContextToolkit] containing either:
                - On success: PlayerContextToolkit in the payload.
                - On failure: Exception.

        Raises:
            *   ZeroPlayerContextToolkitFlagsException
            *   PlayerContextToolkitToolkitException
            *   ArenaPlayerContextToolkitFlagsException
        """
        method = "AgentSearchContextToolkit.toolkit"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, team, game, variety,]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerAgents match the target.
            if param_count == 0:
                return ToolkitResult.failure(
                    ZeroPlayerContextToolkitFlagsException(f"{method}: {ZeroPlayerContextToolkitFlagsException.MSG}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return ToolkitResult.failure(
                    ArenaPlayerContextToolkitFlagsException(f"{method}: {ArenaPlayerContextToolkitFlagsException}")
                )
            # After verifying only one Player attribute-value-tuple is enabled, validate it.
            
            # Toolkit the id PlayerContextToolkit if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return ToolkitResult.failure(validation.exception)
                # On validation success return an id_PlayerContextToolkit in the ToolkitResult.
                return ToolkitResult.success(PlayerContextToolkit(id=id))
            
            # Toolkit the schema PlayerContextToolkit if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure:
                    return ToolkitResult.failure(validation.exception)
                # On validation success return a name_PlayerContextToolkit in the ToolkitResult.
                return ToolkitResult.success(PlayerContextToolkit(name=name))
            
            # Toolkit the team PlayerContextToolkit if its flag is enabled.
            if team is not None:
                validation = team_service.validator.execute(candidate=team)
                if validation.is_failure:
                    return ToolkitResult.failure(validation.exception)
                # On validation success return a team_PlayerContextToolkit in the ToolkitResult.
                return ToolkitResult.success(PlayerContextToolkit(team=team))
            
            # Toolkit the game PlayerContextToolkit if its flag is enabled.
            if game is not None:
                validation = game_service.validator.execute(candidate=game)
                if validation.is_failure:
                    return ToolkitResult.failure(validation.exception)
                # On validation success return a game_PlayerContextToolkit in the ToolkitResult.
                return ToolkitResult.success(PlayerContextToolkit(game=game))
            
            # Toolkit the agent_variety PlayerContextToolkit if its flag is enabled.
            if variety is not None:
                if not isinstance(variety, AgentVariety):
                    return ToolkitResult.failure(
                        TypeError(f"{method}: Expected AgentVariety, got {type(variety).__name__} instead.")
                    )
                # On validation success return a variety_PlayerContextToolkit in the ToolkitResult.
                return ToolkitResult.success(PlayerContextToolkit(variety=variety))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the toolkitResult failure if a map path was missed.
            ToolkitResult.failure(
                ExecutionRouteException(f"{method}: {ExecutionRouteException.MSG}")
            )
        # Finally, catch any missed exception, wrap an PlayerContextToolkitToolkitException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return ToolkitResult.failure(
                PlayerContextToolkitToolkitException(
                    ex=ex, msg=f"{method}: {PlayerContextToolkitToolkitException.MSG}"
                )
            )