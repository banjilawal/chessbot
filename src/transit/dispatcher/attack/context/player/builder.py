# src/transit/dispatcher/attack/context/player/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.context.player.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from domain.model import Game, GameService
from logic.team import Team, TeamService
from system import Attack, AttackResult, ExecutionRouteException, IdentityService, LoggingLevelRouter
from logic.agent import (
    AgentVariety, PlayerContextAttack, PlayerContextAttackAttackException, ZeroPlayerContextAttackFlagsException,
    ArenaPlayerContextAttackFlagsException
)



class PlayerContextAttack(Attack[PlayerContextAttack]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Attack Process Owner

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
            ) -> AttackResult[Token]

     Super Class:
         Attack
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def attack(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            game: Optional[Game] = None,
            variety: Optional[AgentVariety] = None,
            team_service: TeamService = TeamService(),
            game_service: GameService = GameService(),
            identity_service: IdentityService = IdentityService(),
    ) -> AttackResult[PlayerContextAttack]:
        """
        # ACTION:
            1.  Confirm that only one in the (id, designation, team, game, agent_variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass attack a PlayerContextAttack and send in a AttackResult. Else, return an exception
                in the AttackResult.

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
          AttackResult[PlayerContextAttack] containing either:
                - On success: PlayerContextAttack in the payload.
                - On failure: Exception.

        Raises:
            *   ZeroPlayerContextAttackFlagsException
            *   PlayerContextAttackAttackException
            *   ArenaPlayerContextAttackFlagsException
        """
        method = "AgentContextAttack.attack"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, team, game, variety,]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerAgents match the target.
            if param_count == 0:
                return AttackResult.failure(
                    ZeroPlayerContextAttackFlagsException(f"{method}: {ZeroPlayerContextAttackFlagsException.MSG}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return AttackResult.failure(
                    ArenaPlayerContextAttackFlagsException(f"{method}: {ArenaPlayerContextAttackFlagsException}")
                )
            # After verifying only one Player attribute-value-tuple is enabled, validate it.
            
            # Attack the id PlayerContextAttack if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return AttackResult.failure(validation.exception)
                # On validation success return an id_PlayerContextAttack in the AttackResult.
                return AttackResult.success(PlayerContextAttack(id=id))
            
            # Attack the schema PlayerContextAttack if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure:
                    return AttackResult.failure(validation.exception)
                # On validation success return a name_PlayerContextAttack in the AttackResult.
                return AttackResult.success(PlayerContextAttack(name=name))
            
            # Attack the team PlayerContextAttack if its flag is enabled.
            if team is not None:
                validation = team_service.execute.execute(job=team)
                if validation.is_failure:
                    return AttackResult.failure(validation.exception)
                # On validation success return a team_PlayerContextAttack in the AttackResult.
                return AttackResult.success(PlayerContextAttack(team=team))
            
            # Attack the game PlayerContextAttack if its flag is enabled.
            if game is not None:
                validation = game_service.execute.execute(job=game)
                if validation.is_failure:
                    return AttackResult.failure(validation.exception)
                # On validation success return a game_PlayerContextAttack in the AttackResult.
                return AttackResult.success(PlayerContextAttack(game=game))
            
            # Attack the agent_variety PlayerContextAttack if its flag is enabled.
            if variety is not None:
                if not isinstance(variety, AgentVariety):
                    return AttackResult.failure(
                        TypeError(f"{method}: Expected AgentVariety, got {type(variety).__name__} instead.")
                    )
                # On validation success return a variety_PlayerContextAttack in the AttackResult.
                return AttackResult.success(PlayerContextAttack(variety=variety))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the attackResult failure if a map path was missed.
            AttackResult.failure(
                ExecutionRouteException(f"{method}: {ExecutionRouteException.MSG}")
            )
        # Finally, catch any missed exception, wrap an PlayerContextAttackAttackException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return AttackResult.failure(
                PlayerContextAttackAttackException(
                    ex=ex, msg=f"{method}: {PlayerContextAttackAttackException.MSG}"
                )
            )