# src/chess/agent/search/context/builder

"""
Module: chess.agent.search.context.builder
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from typing import Any, Optional, cast

from chess.agent import AgentTeamSearchContext
from chess.system import (
    BuildResult, Builder, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter
)
from chess.agent import (
    AgentTeamSearchContext, NullAgentTeamSearchContext, AgentTeamSearchContextBuildFailedException,
    NoAgentTeamSearchOptionSelectedException, MoreThanOneAgentTeamSearchOptionPickedException,
)


class AgentTeamSearchContextBuilder(Builder[AgentTeamSearchContext]):
    """
    # ROLE: Builder

    # RESPONSIBILITIES:
    1.  Manage construction of AgentTeamSearchContext instances that can be used safely by the client.
    2.  Ensure params for AgentTeamSearchContext creation have met the application's safety contract.
    3.  Provide pluggable factories for creating different AgentTeamSearchContext products.


    # PROVIDES:
    ValidationResult[AgentTeamSearchContext] containing either:
        - On success:   AgentTeamSearchContext in the payload.
        - On failure:   Exception.

    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int],
            name: Optional[str],
            color: Optional[GameColor],
            color_validator: type[GameColorValidator] = GameColorValidator,
            identity_service: IdentityService=IdentityService(),
    ) -> BuildResult[AgentTeamSearchContext]:
        """
        # Action:
            1.  Use dependency injected validators to verify correctness of parameters required to
                build a AgentTeamSearchContext instance.
            2.  If the parameters are safe the AgentTeamSearchContext is built and returned.

        # Parameters:
            *   id (Optional[int]):                             Selected if search target is an id.
            
            *   name (Optional[str]):                           Selected if search target is a name.
            
            *   color (Optional[GameColor]):                    Selected if search target is a GameColor.
            
            *   identity_service (type[IdentityService]):       Validates name or ID safety
            
            *   color_validator (type[GameColorValidator]):     Validates a name-search-target

        # Returns:
        BuildResult[AgentTeamSearchContext] containing either:
            - On success:   AgentTeamSearchContext in the payload.
            - On failure:   Exception.

        # Raises:
            *   AgentTeamSearchContextBuildFailedException
            *   NoAgentTeamSearchOptionSelectedException
            *   MoreThanOneAgentTeamSearchOptionPickedException
        """
        method = "AgentTeamSearchContextBuilder.build"
        
        try:
            params = [id, name, color]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoAgentTeamSearchOptionSelectedException(
                        f"{method}: {NoAgentTeamSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    MoreThanOneAgentTeamSearchOptionPickedException(
                        f"{method}: {MoreThanOneAgentTeamSearchOptionPickedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if id is not None:
                return cls.build_id_search_context(id=id, identity_service=identity_service)
            
            if name is not None:
                return cls.build_name_search_context(name=name, identity_service=identity_service)
            
            if color is not None:
                return cls.build_color_search_context(color=color, color_validator=color_validator)
        
        except Exception as ex:
            return BuildResult.failure(
                AgentTeamSearchContextBuildFailedException(
                    f"{method}: {AgentTeamSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_id_search_context(
            cls,
            candidate: Any,
            identity_service: IdentityService=IdentityService(),
    ) -> BuildResult[AgentTeamSearchContext]:
        """
        # Action:
        Build an id-AgentTeamSearchContext if IdentityService verifies search target is safe.

        # Parameters:
          *     candidate (int):                            search_value to validate
          
          *     identity_service (type[IdentityService]):   validates target.

        # Returns:
          ValidationResult[AgentTeamSearchContext] containing either:
                - On success:   AgentTeamSearchContext in the payload.
                - On failure:   Exception.

        # Raises:
            *   InvalidAgentTeamSearchContextException
        """
        method = "AgentTeamSearchContextBuilder.build_id_search_context"
        try:
            id_validation = identity_service.validate_id(candidate=id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            id = cast(int, id_validation.payload)
            
            return BuildResult.success(payload=AgentTeamSearchContext(id=id))
        
        except Exception as ex:
            return BuildResult.failure(
                AgentTeamSearchContextBuildFailedException(
                    f"{method}: {AgentTeamSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_name_search_context(
            cls,
            candidate: Any,
            identity_service: IdentityService=IdentityService(),
    ) -> BuildResult[AgentTeamSearchContext]:
        """
        # Action:
        Build a name-AgentTeamSearchContext if NameValidator verifies search target is safe.

        # Parameters:
          *     candidate (Any):                            search_value to validate
          
          *     identity_service (type[IdentityService]):   validates is a valida name.

        # Returns:
          ValidationResult[AgentTeamSearchContext] containing either:
                - On success:   AgentTeamSearchContext in the payload.
                - On failure:   Exception.

        # Raises:
            *   InvalidAgentTeamSearchContextException
        """
        method = "AgentTeamSearchContextBuilder.build_name_search_context"
        
        try:
            name_validation = identity_service.validate_name(candidate=candidate)
            if name_validation.is_failure():
                return BuildResult.failure(name_validation.exception)
            
            name = cast(str, name_validation.payload)
            
            return BuildResult.success(payload=AgentTeamSearchContext(name=name))
        
        except Exception as ex:
            return BuildResult.failure(
                AgentTeamSearchContextBuildFailedException(
                    f"{method}: {AgentTeamSearchContextBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_color_search_context(
            cls,
            candidate: Any,
            color_validator: type[GameColorValidator]=GameColorValidator
    ) -> BuildResult[AgentTeamSearchContext]:
        """
        # Action:
        Build a color-AgentTeamSearchContext if ColorValidator verifies search target is safe.

        # Parameters:
          *     candidate (Any):                            search_value to validate
          
          *     color_validator (type[ColorValidator]):   validates is a valida name.

        # Returns:
        ValidationResult[AgentTeamSearchContext] containing either:
            - On success:   AgentTeamSearchContext in the payload.
            - On failure:   Exception.

        # Raises:
            *   InvalidAgentTeamSearchContextException
        """
        method = "AgentTeamSearchContextBuilder.build_color_search_context"
        
        try:
            color_validation = color_validator.validate(candidate)
            if color_validation.is_failure():
                return BuildResult.failure(color_validation.exception)
            
            color = cast(GameColor, color_validation.payload)
            
            return BuildResult.success(payload=AgentTeamSearchContext(color=color))
        
        except Exception as e:
            return BuildResult.failure(
                AgentTeamSearchContextBuildFailedException(
                    f"{method}: {AgentTeamSearchContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
