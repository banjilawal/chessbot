# src/chess/agent/builder.py

"""
Module: chess.agent.builder
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from typing import Optional

from chess.team import UniqueTeamDataService
from chess.game import UniqueGameDataService
from chess.engine.service import EngineService
from chess.agent import Agent, AgentBuildFailedException, AgentVariety, AgentValidator, HumanAgent, MachineAgent
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter, ValidationResult, id_emitter


class AgentFactory(Builder[Agent]):
        """
        # ROLE: Builder, Data Integrity Guarantor

        # RESPONSIBILITIES:
        Produce Agent instances whose integrity is always guaranteed. If any attributes do not pass
        their integrity checks, send an exception instead of an unsafe Agent.

        # PROVIDES:
        BuildResult[Agent] containing either:
            - On success: Agent in the payload.
            - On failure: Exception.

        # ATTRIBUTES:
        None
        """
        
        @classmethod
        def build(
                cls,
                name: str,
                id: id_emitter.agent_id,
                agent_variety: AgentVariety,
                agent_validator: AgentValidator = AgentValidator(),
                identity_service: IdentityService = IdentityService(),
                engine_service: Optional[EngineService] = None,
        ) -> BuildResult[Agent]:
            """
            # ACTION:
            1.  Call _validate_build_params. to verify inputs are safe.
            2.  If the _validate params returns failure include the failure in a BuildResult.
            3.  If the engine is not validation call build_machine_agent. Otherwise, call build_human_agent.

            # PARAMETERS:
                *   id (int)
                *   name (str)
                *   identity_service (IdentityService)
                *   engine_service (Optional[EngineService])

            # Returns:
            ValidationResult[Agent] containing either:
                - On success: Agent in the payload.
                - On failure: Exception.

            # Raises:
                *   AgentBuildFailedException
            """
            method = "AgentBuilder.build"
            
            try:
                # Ensure the agent_variety is the correct type and not null.
                variety_validation = agent_validator.certify_variety(candidate=agent_variety)
                if variety_validation.failure():
                    return BuildResult.failure(variety_validation.exception)
                # Use agent_variety to decide which factory method to call.
                if isinstance(agent_variety, HumanAgent):
                    return cls.build_human_agent(id=id, name=name,)
                if isinstance(agent_variety, MachineAgent):
                    return cls.build_machine_agent(id=id, name=name, engine_service=engine_service)
                
                if agent_variety == AgentVariety.MACHINE_AGENT and engine_service is None:
                    return BuildResult.failure(
                        AgentBuildFailedException(
                            f"{method}: Cannot build a MachineAgent "
                            f"without an EngineService instance."
                        )
                    )
                
                if agent_variety == AgentVariety.MACHINE_AGENT and engine_service is not None:
                    return cls.build_machine_agent(
                        id=id,
                        name=name,
                        team_stack=team_stack,
                        engine_service=engine_service,
                        identity_service=identity_service,
                    )
                
                return cls.build_human_agent(
                    id=id,
                    name=name,
                    team_stack=team_stack,
                    identity_service=identity_service,
                )
            
            except Exception as ex:
                return BuildResult.failure(
                    AgentBuildFailedException(
                        ex=ex,
                        message=(
                            f"{method}: "
                            f"{AgentBuildFailedException.DEFAULT_MESSAGE}"
                        )
                    )
                )
        
        @classmethod
        @LoggingLevelRouter.monitor
        def build_human_agent(
                cls,
                id: int,
                name: str,
                identity_service: IdentityService = IdentityService(),
        ) -> BuildResult[HumanAgent]:
            """"""
            method = "AgentBuilder.build_human_agent"
            try:
                validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(
                    HumanAgent(
                        id=id,
                        name=name,
                        games=UniqueGameDataService(),
                        team_assignments=UniqueTeamDataService(),
                    )
                )
            # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
            # then return the exceptions inside a ValidationResult.
            except Exception as ex:
                return BuildResult.failure(
                    HumanAgentBuildFailedException(
                        ex=ex, message=f"{method}:{HumanAgentBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
        
        @classmethod
        @LoggingLevelRouter.monitor
        def build_machine_agent(
                cls,
                name: str,
                id: int = id_emitter.service_id,
                engine_service: EngineService = EngineService(),
                identity_service: IdentityService = IdentityService(),
        ) -> BuildResult[HumanAgent]:
            """"""
            method = "AgentBuilder.build_machine_agent"
            try:
                identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
                if identity_validation.is_failure():
                    return BuildResult.failure(validation.exception)
                
                
                
    
                return BuildResult.success(
                    MachineAgent(
                        id=id,
                        name=name,
                        team_stack=team_stack,
                        engine_service=engine_service
                    )
                )
            except Exception as ex:
                return BuildResult.failure(
                    AgentBuildFailedException(
                        ex=ex,
                        message=(
                            f"{method}: "
                            f"{AgentBuildFailedException.DEFAULT_MESSAGE}"
                        )
                    )
                )


@classmethod
@LoggingLevelRouter.monitor
def _verify_build_attributes(
        cls,
        id: int,
        name: str,
        variety: AgentVariety,
        engine_service: Optional[EngineService],
        identity_service: IdentityService = IdentityService(),
) -> ValidationResult[(int, str, AgentVariety, Optional[EngineService])]:
    """
    # ACTION
    validate_build_attributes. This decouples verification logic from build logic so
    each factory method can run independently and build can direct which product
    should be manufactured.
    """
    method = "AgentFactory._verify_build_attributes"
    try:
        # Start the error detection process.
        identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
        if identity_validation.is_failure():
            return BuildResult.failure(identity_validation.exception)
        
        rank_validation = rank_certifier.item_validator.validate(candidate=rank)
        if rank_validation.is_failure():
            return BuildResult.failure(rank_validation.exception)
        
        team_validation = team_certifier.item_validator.validate(candidate=team)
        if team_validation.is_failure():
            return BuildResult.failure(team_validation.exception)
        
        square_validation = square_certifier.item_validator.validate(candidate=opening_square)
        if square_validation.is_failure():
            return BuildResult.failure(square_validation.exception)
        
        roster_number_validation = identity_service.validate_id(candidate=roster_number)
        if roster_number_validation.is_failure():
            return BuildResult.failure(roster_number_validation.exception)
        
        # If no errors are detected return the successfully validated (id, name, rank, team) tuple.
        return ValidationResult.success((id, name, rank, team, roster_number, opening_square))
    
    # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
    # then return the exceptions inside a ValidationResult.
    except Exception as ex:
        return ValidationResult.failure(
            PieceBuildFailedException(ex=ex, message=f"{method}: {PieceBuildFailedException.DEFAULT_MESSAGE}")
        )


class AgentContextBuilder(Builder[AgentContext]):
    """
    # ROLE: Builder

    # RESPONSIBILITIES:
        1.  Produce new AgentContext instances that are guaranteed to be the safe and reliable.
        2.  Ensure the only search value provided in the AgentContext has been verified to be safe.

    # PROVIDES:
      BuildResult[AgentContext] containing either:
            - On success: AgentContext in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
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
            variety: Optional[AgentVariety] = None,
            team_service: TeamService = TeamService(),
            game_service: GameService = GameService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[AgentContext]:
        """
        # Action:
            1.  Confirm that only one in the (id, name, team, game, agent_variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an AgentContext are return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   name (Optional[str])
            *   team (Optional[Team])
            *   game (Optional[Game])
            *   agent_variety (Optional[AgentVariety])

        These Parameters must be provided:
            *   team_service (TeamService)
            *   game_service (GameService)
            *   identity_service (IdentityService)

        # Returns:
          BuildResult[AgentContext] containing either:
                - On success: AgentContext in the payload.
                - On failure: Exception.

        # Raises:
            *   AgentContextBuildFailedException
            *   NoAgentContextFlagException
            *   TooManyAgentContextFlagsException
        """
        method = "AgentSearchContextBuilder.builder"
        try:
            # Get how many optional parameters are not null. One param is expected to have
            # a value.
            params = [id, name, team, game, variety, ]
            param_count = sum(bool(p) for p in params)
            # Cannot search for an Agent object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoAgentContextFlagException(f"{method}: {NoAgentContextFlagException.DEFAULT_MESSAGE}")
                )
            # Only one param can be used for a search. If you need to search by multiple params
            # Filter the previous set of matches in a new AgentSearch with a new context.
            if param_count > 1:
                return BuildResult.failure(
                    TooManyAgentContextFlagsException(f"{method}: {TooManyAgentContextFlagsException}")
                )
            # After verifying the correct number of switches is turned on validate the target value
            # with the appropriate Validator. On pass create an AgentContext.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(AgentContext(id=id))
            
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(AgentContext(name=name))
            
            if team is not None:
                validation = team_service.item_validator.validate(candidate=team)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(AgentContext(team=team))
            
            if game is not None:
                validation = game_service.validate_name(name)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(AgentContext(game=game))
            
            if variety is not None:
                if not isinstance(variety, AgentVariety):
                    return BuildResult.failure(
                        TypeError(f"{method}: Expected AgentVariety, got {type(variety).__name__} instead.")
                    )
                return BuildResult.success(AgentContext(variety=variety))
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an AgentContextBuildFailedException and send the exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
                AgentContextBuildFailedException(
                    ex=ex, message=f"{method}: {AgentContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )