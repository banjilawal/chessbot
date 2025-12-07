# src/chess/agent/context/service/validator_.py

"""
Module: chess.agent.context.service.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import Any, cast

from chess.agent import (
    AgentContextBuilder, AgentContextService, AgentContextValidator, AgentSearch,
    InvalidAgentContextException, MissingAgentContextBuilderException, MissingAgentContextValidatorException,
    MissingAgentSearcherException, NullAgentContextServiceException
)
from chess.system import LoggingLevelRouter, ValidationResult, Validator


class AgentContextServiceValidator(Validator[AgentContextService]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1. Verify a candidate is an AgentContextService whose Builder, Validator and Searcher exist.

    # PROVIDES:
      ValidationResult[AgentContextService] containing either:
            - On success: AgentContextService in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[AgentContextService]:
        """
        # Action:
            1.  Confirm the candidate is not null and an AgentContextService instance.
            2.  Certify it has a not null AgentContextBuilder
            3.  Certify it has a not null AgentContextValidator
            4.  Certify it has a not null AgentSearcher

        # Parameters:
            *   candidate (Any)

        # Returns:
          BuildResult[AgentContextService] containing either:
                - On success: AgentContextService in the payload.
                - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullAgentContextServiceException
            *   MissingAgentContextBuilderException
            *   MissingAgentContextValidatorException
            *   MissingAgentSearcherException
            *   InvalidAgentContextServiceException
        """
        method = "AgentContextServiceValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullAgentContextServiceException(
                        f"{method}: {NullAgentContextServiceException.DEFAULT_MESSAGE}"
                    )
                )
            # If the candidate is not an AgentContext validation has failed.
            if not isinstance(candidate, AgentContextService):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected AgentContextService, got {type(candidate).__name__} instead.")
                )
            # Once the two existence checks are passed cast candidate to an AgentContextService
            # For additional processing.
            service = cast(AgentContextService, candidate)
            
            # Only need to make sure builder is a not-null AgentContextBuilder instance.
            if service.builder is None or not isinstance(service.builder, AgentContextBuilder):
                return ValidationResult.failure(
                    MissingAgentContextBuilderException(
                        f"{method}: {MissingAgentContextBuilderException.DEFAULT_MESSAGE}"
                    )
                )
            # Make sure validator is a not-null AgentContextValidator instance.
            if service.validator is None or not isinstance(service.validator, AgentContextValidator):
                return ValidationResult.failure(
                    MissingAgentContextValidatorException(
                        f"{method}: {MissingAgentContextValidatorException.DEFAULT_MESSAGE}"
                    )
                )
            # Make sure searcher is a not-null AgentSearcher instance.
            if service.search is None or not isinstance(service.search, AgentSearch):
                return ValidationResult.failure(
                    MissingAgentSearcherException(
                        f"{method}: {MissingAgentSearcherException.DEFAULT_MESSAGE}"
                    )
                )
            # If all checks pass return the AgentContextService.
            return ValidationResult.success(service)
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidAgentContextServiceException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            ValidationResult.failure(
                InvalidAgentContextException(
                    ex=ex, message=f"{method}: {InvalidAgentContextException.DEFAULT_MESSAGE}"
                )
            )