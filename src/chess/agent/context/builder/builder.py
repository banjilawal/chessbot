# src/chess/agent/context/builder/builder.py

"""
Module: chess.agent.context.builder.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional


from chess.team import Team, TeamIntegrityService
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter
from chess.agent import (
    AgentVariety, AgentContext, AgentContextBuildFailedException, NoAgentContextFlagSetException,
    TooManyAgentContextFlagsSetException
)



class AgentContextBuilder(Builder[AgentContext]):
    """
    # ROLE: Builder

    # RESPONSIBILITIES:
        1. Produce only AgentContext instances that are safe and reliable.
        2. Ensure params for AgentContext have correctness.

    # PROVIDES:
      BuildResult[AgentContext] containing either:
            - On success: AgentContext in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            variety: Optional[AgentVariety] = None,
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[AgentContext]:
        """
        # Action:
            1. Confirm that only one in the tuple (id, name, agent), is not null.
            2. Certify the not-null attribute is safe using the appropriate service and validator.
            3. If all checks pass build the AgentContext in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   name (Optional[str])
            *   team (Optional[Team])

        These Parameters must be provided:
            *   team_service (TeamIntegrityService)
            *   identity_service (IdentityService)

        # Returns:
          BuildResult[AgentContext] containing either:
                - On success: AgentContext in the payload.
                - On failure: Exception.

        # Raises:
            *   AgentContextBuildFailedException
            *   NoAgentContextFlagSetException
            *   TooManyAgentContextFlagsSetException
        """
        method = "AgentSearchContextBuilder.builder"
        
        try:
            params = [id, name, variety, ]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoAgentContextFlagSetException(
                        f"{method}: "
                        f"{NoAgentContextFlagSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    TooManyAgentContextFlagsSetException(
                        f"{method}: "
                        f"{TooManyAgentContextFlagsSetException}"
                    )
                )
            
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
            

                return BuildResult.success(AgentContext(variety=variety))
        
        except Exception as ex:
            return BuildResult.failure(
                AgentContextBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{AgentContextBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )