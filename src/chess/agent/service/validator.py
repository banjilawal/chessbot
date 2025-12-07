# src/chess/agent/service/validator.py

"""
Module: chess.agent.service.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import Any, cast

from chess.agent import (
    AgentFactory, AgentService, AgentValidator, InvalidAgentServiceException, MissingAgentBuilderException,
    MissingAgentValidatorException, NullAgentServiceException
)
from chess.system import LoggingLevelRouter, ValidationResult, Validator


class AgentServiceValidator(Validator[AgentService]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1. Verify a candidate is an AgentService whose Builder, Validator and Searcher exist.

    # PROVIDES:
      ValidationResult[AgentService] containing either:
            - On success: AgentService in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[AgentService]:
        """
        # Action:
            1.  Confirm the candidate is not null and an AgentService instance.
            2.  Certify it has a not null AgentBuilder
            3.  Certify it has a not null AgentValidator
            4.  Certify it has a not null AgentFinder

        # Parameters:
            *   candidate (Any)

        # Returns:
          BuildResult[AgentService] containing either:
                - On success: AgentService in the payload.
                - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullAgentServiceException
            *   MissingAgentFactoryException
            *   MissingAgentValidatorException
            *   InvalidAgentServiceException
        """
        method = "AgentServiceValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullAgentServiceException(
                        f"{method}: {NullAgentServiceException.DEFAULT_MESSAGE}"
                    )
                )
            # If the candidate is not an Agent validation has failed.
            if not isinstance(candidate, AgentService):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected AgentService, got {type(candidate).__name__} instead.")
                )
            # Once the two existence checks are passed cast candidate to an AgentService
            # For additional processing.
            service = cast(AgentService, candidate)
            
            # Only need to make sure builder is a not-null AgentBuilder instance.
            if service.builder is None or not isinstance(service.builder, AgentFactory):
                return ValidationResult.failure(
                    MissingAgentBuilderException(
                        f"{method}: {MissingAgentBuilderException.DEFAULT_MESSAGE}"
                    )
                )
            # Make sure validator is a not-null AgentValidator instance.
            if service.validator is None or not isinstance(service.validator, AgentValidator):
                return ValidationResult.failure(
                    MissingAgentValidatorException(
                        f"{method}: {MissingAgentValidatorException.DEFAULT_MESSAGE}"
                    )
                )

            # If all checks pass return the AgentService.
            return ValidationResult.success(service)
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidAgentServiceException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            ValidationResult.failure(
                InvalidAgentServiceException(
                    ex=ex, message=f"{method}: {InvalidAgentServiceException.DEFAULT_MESSAGE}"
                )
            )