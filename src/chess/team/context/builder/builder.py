# src/chess/team/context/builder/builder.py

"""
Module: chess.team.context.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.agent import Agent, AgentService
from chess.system import Builder, BuildResult, GameColor, IdentityService, LoggingLevelRouter
from chess.team import (
    NoTeamContextFlagsException, TeamContext, TeamContextBuildFailedException, TeamSchema, TeamValidator,
    TooManyTeamContextFlagsException
)


class TeamContextBuilder(Builder[TeamContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor

     # RESPONSIBILITIES:
     Produce TeamContext instances whose integrity is always guaranteed. If any attributes do not pass
     their integrity checks, send an exception instead.

     # PROVIDES:
     BuildResult[TeamContext] containing either:
         - On success: TeamContext in the payload.
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
            agent: Optional[Agent] = None,
            color: Optional[GameColor] = None,
            schema: Optional[TeamSchema] = None,
            agent_service: AgentService = AgentService(),
            team_validator: TeamValidator = TeamValidator(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[TeamContext]:
        """
        # Action:
            1. Confirm that only one in the tuple (id, name, agent, color, schema), is not null.
            2. Certify the not-null attribute is safe using the appropriate service and validator.
            3. If all checks pass build the PieceContext in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   name (Optional[int])
            *   agent (Optional[Agent])
            *   color (Optional[GameColor])
            *   schema (Optional[TeamSchema])

        These Parameters must be provided:
            *   agent_service (AgentService)
            *   team_validator (TeamValidator)
            *   identity_service (IdentityService)

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
            params = [id, name, agent, color, schema]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoTeamContextFlagsException(f"{method}:  {NoTeamContextFlagsException.DEFAULT_MESSAGE}")
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    TooManyTeamContextFlagsException(f"{method}: {TooManyTeamContextFlagsException}")
                )
            
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(payload=TeamContext(id=id))
            
            if agent is not None:
                validation = agent_service.validator.validate(agent)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(payload=TeamContext(agent=agent))
            
            if name is not None:
                validation = team_validator.validate_name(name)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(payload=TeamContext(name=name))

            if color is not None:
                validation = team_validator.validate_color(color)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(payload=TeamContext(color=color))
            
            if schema is not None:
                return BuildResult.success(TeamContext(schema=schema))
            
        except Exception as ex:
            return BuildResult.failure(
                TeamContextBuildFailedException(
                    ex=ex,
                    message=f"{method}: {TeamContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )