# src/agent/search/context/validator.py

"""
Module: chess.agent.search.context.validator
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from typing import Any, cast

from chess.system import GameColor, Validator, IdentityService, GameColorValidator, ValidationResult, LoggingLevelRouter
from chess.agent import (
    AgentTeamSearchContext, InvalidAgentTeamSearchContextException, NullAgentTeamSearchContextException,
    MoreThanOneAgentTeamSearchOptionPickedException, NoAgentTeamSearchOptionSelectedException
)


class AgentTeamSearchContextValidator(Validator):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1.  Verify a candidate is a AgentTeamSearchContext that meets the application's safety contract before the client
        is allowed to use the AgentTeamSearchContext object.
    2.  Provide pluggable factories for validating different search options separately.
    
    # PROVIDES:
    ValidationResult[AgentTeamSearchContext] containing either:
        - On success:   AgentTeam in the payload.
        - On failure:   Exception.

    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            identity_service: IdentityService=IdentityService,
            color_validator: type[GameColorValidator]=GameColorValidator
    ) -> ValidationResult[AgentTeamSearchContext]:
        """
        # Action:
        Verifies candidate is a AgentTeamSearchContext in two steps.
            1.  Test the candidate is a valid SearchAgentTeamContext with a single search option switched on.
            2.  Test the value passed to AgentTeamSearchContext passes its validation contract..

        # Parameters:
          * candidate (Any):                                Object to verify is a AgentTeam.

          * identity_service (type[IdentityService]):       Enforces safety requirements on name-search targets.
          
          * color_validator (type[GameColorValidator]):     Enforces safety requirements on name-search targets.
          
        # Returns:
          ValidationResult[AgentTeamSearchContext] containing either:
                - On success:   AgentTeamSearchContext in the payload.
                - On failure:   Exception.

        # Raises:
            *   TypeError
            *   NullAgentTeamSearchContextException
            *   NoAgentTeamSearchOptionSelectedException
            *   InvalidAgentTeamSearchContextException
            *   MoreThanOneAgentTeamSearchOptionPickedException
        """
        method = "AgentTeamSearchContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullAgentTeamSearchContextException(
                        f"{method} {NullAgentTeamSearchContextException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, AgentTeamSearchContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected AgentTeamSearchContext, got {type(candidate).__name__} instead."
                    )
                )
            
            agentTeam_search_context = cast(AgentTeamSearchContext, candidate)
            if len(agentTeam_search_context.to_dict() == 0):
                return ValidationResult.failure(
                    NoAgentTeamSearchOptionSelectedException(
                        f"{method}: {NoAgentTeamSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if len(agentTeam_search_context.to_dict()) > 1:
                return ValidationResult.failure(
                    MoreThanOneAgentTeamSearchOptionPickedException(
                        f"{method}: {MoreThanOneAgentTeamSearchOptionPickedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if agentTeam_search_context.id is not None:
                return cls.validate_id_search_option(
                    candidate=agentTeam_search_context.id,
                    identity_service=identity_service
                )
            
            if agentTeam_search_context.name is not None:
                return cls.validate_name_search_option(
                    name=agentTeam_search_context.name,
                    identity_service=identity_service
                )
            
            if agentTeam_search_context.color is not None:
                return cls.validate_color_search_option(
                    color=agentTeam_search_context.color,
                    color_validator=color_validator
                )
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentTeamSearchContextException(
                    f"{method}: {InvalidAgentTeamSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_id_search_option(
            cls,
            candidate: Any,
            identity_service: type[IdentityService] = IdentityService
    ) -> ValidationResult[AgentTeamSearchContext]:
        """
        # Action:
        Verify an id_candidate meets application AgentTeamSearchContext safety requirements.

        # Parameters:
            *   candidate (Any):                            Object to verify is an id.
            
            *   identity_service (type[IdentityService]):   Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[AgentTeamSearchContext] containing either:
                - On success:   AgentTeamSearchContext in the payload.
                - On failure:   Exception.

        # Raises:
            *   InvalidAgentTeamSearchContextException
        """
        method = "AgentTeamSearchContextValidator.validate_id_search_option"
        
        try:
            id_validation = identity_service.validate(candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            id = cast(int, id_validation.payload)
            
            return ValidationResult.success(payload=AgentTeamSearchContext(id=id))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentTeamSearchContextException(
                    f"{method}: {InvalidAgentTeamSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_name_search_option(
            cls,
            candidate: Any,
            identity_service: type[IdentityService] = IdentityService
    ) -> ValidationResult[AgentTeamSearchContext]:
        """
        # Action:
        Verify a name_candidate meets application AgentTeamSearchContext safety requirements.

        # Parameters:
          * candidate (Any):                            Object to verify is a name.
          
          * identity_service (type[IdentityService]):   Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[AgentTeamSearchContext] containing either:
                - On success: AgentTeamSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidAgentTeamSearchContextException
        """
        method = "AgentTeamSearchContextValidator.validate_name_search_option"
        
        try:
            name_validation = identity_service.validate(candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            name = cast(str, name_validation.payload)
            
            return ValidationResult.success(payload=AgentTeamSearchContext(name=name))
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentTeamSearchContextException(
                    f"{method}: {InvalidAgentTeamSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_color_search_option(
            cls,
            candidate: Any,
            color_validator: type[GameColorValidator] = GameColorValidator
    ) -> ValidationResult[AgentTeamSearchContext]:
        """
        # Action:
        Verify a color_candidate meets application AgentTeamSearchContext safety requirements.

        # Parameters:
            *   candidate (Any):                                Object to verify is a color.
            
            *   identity_service (type[GameColorValidator]):    Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[AgentTeamSearchContext] containing either:
                - On success:   AgentTeamSearchContext in the payload.
                - On failure:    Exception.

        # Raises:
            *   InvalidAgentTeamSearchContextException
        """
        method = "AgentTeamSearchContextValidator.validate_color_search_option"
        
        try:
            color_validation = color_validator.validate(candidate)
            if color_validation.is_failure():
                return ValidationResult.failure(color_validation.exception)
            
            color = cast(GameColor, color_validation.payload)
            
            return ValidationResult.success(payload=AgentTeamSearchContext(color=color))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentTeamSearchContextException(
                    f"{method}: {InvalidAgentTeamSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
