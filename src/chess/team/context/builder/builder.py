# src/chess/team/context/builder/builder.py

"""
Module: chess.team.context.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.agent import Agent, AgentService
from chess.arena import Arena, ArenaService
from chess.arena import Arena
from chess.arena.service import ArenaService
from chess.system import Builder, BuildResult, ArenaColor, GameColorValidator, IdentityService, LoggingLevelRouter
from chess.team import (
    NoTeamContextFlagsException, TeamContext, TeamContextBuildFailedException, TeamSchema, TeamSchemaValidator,
    TeamValidator,
    TooManyTeamContextFlagsException
)


class TeamContextBuilder(Builder[TeamContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce TeamContext instances whose integrity is always guaranteed.
     2.  Manage construction of TeamContext instances that can be used safely by the client.
     3.  Ensure params for TeamContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
        *   build

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
            arena: Optional[Arena] = None,
            agent: Optional[Agent] = None,
            color: Optional[ArenaColor] = None,
            arena_service: ArenaService = ArenaService(),
            agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[TeamContext]:
        """
        # Action:
            1. Confirm that only one in the tuple (id, name, agent, color, team_schema), is not null.
            2. Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3. If all checks pass build the PieceContext in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   name (Optional[int])
            8   arena (Optional[Arena])
            *   agent (Optional[Agent])
            *   color (Optional[ArenaColor])

        These Parameters must be provided:
            *   arena_service (ArenaService)
            *   agent_certifier (AgentService)
            *   identity_service (IdentityService)
            *   schema_validator (TeamSchemaValidator)

        # Returns:
          BuildResult[TeamContext] containing either:
                - On success: TeamContext in the payload.
                - On failure: Exception.

        # Raises:
            *   TeamContextBuildFailedException
            *   NoTeamContextFlagsException
            *   TooManyTeamContextFlagsException
        """
        method = "PieceSearchContextBuilder.builder"
        
        try:
            # Start the error detection process.
            params = [id, name, arena, agent, color]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoTeamContextFlagsException(f"{method}:  {NoTeamContextFlagsException.DEFAULT_MESSAGE}")
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    TooManyTeamContextFlagsException(f"{method}: {TooManyTeamContextFlagsException}")
                )
            # If no errors are detected pick the flag whose value is not for processing.
            
            if id is not None:
                validation = identity_service.validate_id(candidate=id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # If id is correct create a id.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(id=validation.payload))
            
            if agent is not None:
                validation = agent_service.validator.validate(candidate=agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # If agent is correct create a agent.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(agent=validation.payload))
            
            if arena is not None:
                validation = arena_service.item_validator.validate(candidate=arena)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # If arena is correct create a agent.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(agent=validation.payload))
            
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # If name is correct create a name.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(name=validation.payload))

            if color is not None:
                validation = color_validator.validate(candidate=color)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # If color is correct create a color.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(color=validation.payload))
            
            if arena is not None:
                validation = arena_service.validator.validate(candidate=color)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # If arena is correct create a arena.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(arena=validation.payload))
            
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                TeamContextBuildFailedException(
                    ex=ex, message=f"{method}: {TeamContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )