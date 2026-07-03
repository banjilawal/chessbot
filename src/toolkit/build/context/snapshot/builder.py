# src/toolkit/context/snapshot/toolkit.py

"""
Module: toolkit.context.snapshot.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations



class SnapshotContextToolkit(Toolkit[SnapshotContext]):
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
            game: Optional[Game],
            team: Optional[Team],
            arena: Optional[Arena],
            timestamp: Optional[int],
            player: Optional[PlayerAgent],
            exception: Optional[Exception],
            team_service: TeamService = TeamService(),
            agent_service: AgentService = AgentService(),
            number_validator: NumberValidator = NumberValidator()
    ) -> ToolkitResult[SnapshotContext]:
        """
        # ACTION:
            1.  Confirm that only one in the (team, owner, timestamp) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass toolkit a SnapshotContext and send in a ToolkitResult. Else, return an exception
                in the ToolkitResult.

        # PARAMETERS:
            Only one these must be provided:
                *   game (Optional[Game])
                *   team (Optional[Team])
                *   arena (Optional[Arena])
                *   timestamp (Optional[int])
                *   exception (Optional[Exception])
                *   owner (Optional[Player])
                
            These Parameters must be provided:
                *   game_service (GameService)
                *   team_service (TeamService)
                *   arena_service (ArenaService)
                *   player_service (AgentService)
                *   identity_service (IdentityService)

        # RETURNS:
        ToolkitResult[SnapshotContext] containing either:
            - On success: SnapshotContext in the payload.
            - On failure: Exception.

        Raises:
            *   ZeroSnapshotContextFlagsException
            *   SnapshotContextToolkitException
            *   ArenaSnapshotContextFlagsException
        """
        method = "SnapshotContextToolkit.toolkit"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [team, agent, timestamp]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerAgents match the target.
            if param_count == 0:
                return ToolkitResult.failure(
                    ZeroSnapshotContextFlagsException(f"{method}: {ZeroSnapshotContextFlagsException.MSG}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return ToolkitResult.failure(
                    ArenaSnapshotContextFlagsException(f"{method}: {ArenaSnapshotContextFlagsException}")
                )
            # After verifying only one Snapshot attribute-value-tuple is enabled, validate it.

            # Toolkit the timestamp SnapshotContext if its flag is enabled.
            if timestamp is not None:
                validation = number_validator.build(candidate=timestamp)
                if validation.is_failure:
                    return ToolkitResult.failure(validation.exception)
                # On validation success return an timestamp_SnapshotContext in the ToolkitResult.
                return ToolkitResult.success(payload=SnapshotContext(timestamp=timestamp))
            
            # Toolkit the agent SnapshotContext if its flag is enabled.
            if agent is not None:
                validation = agent_service.validator.search_service(candidate=agent)
                if validation.is_failure:
                    return ToolkitResult.failure(validation.exception)
                # On validation success return an agent_SnapshotContext in the ToolkitResult.
                return ToolkitResult.success(payload=SnapshotContext(agent=agent))
            
            # Toolkit the team SnapshotContext if its flag is enabled.
            if team is not None:
                validation = team_service.validator.build(candidate=team)
                if validation.is_failure:
                    return ToolkitResult.failure(validation.exception)
                # On validation success return a team_SnapshotContext in the ToolkitResult.
                return ToolkitResult.success(payload=SnapshotContext(team=team))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the toolkitResult failure if a map path was missed.
            ToolkitResult.failure(
                ExecutionRouteException(f"{method}: {ExecutionRouteException.MSG}")
            )
        # Finally, catch any missed exception and wrap A SnapshotContextToolkitException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return ToolkitResult.failure(
               SnapshotContextToolkitException(
                    ex=ex, msg=f"{method}: {SnapshotContextToolkitException.MSG}"
                )
            )
