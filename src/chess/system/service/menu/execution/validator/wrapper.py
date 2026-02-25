# src/chess/system/service/menu/execution/validator/wrapper.py

"""
Module: chess.system.service.menu.execution.validator.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from chess.system import ValidationException

__all__ = [
    # ======================# SERVICE_EXECUTION_VALIDATION_FAILURE #======================#
    "ServiceExecutionValidationException",
]

# ======================# SERVICE_EXECUTION_VALIDATION_FAILURE #======================#
class ServiceExecutionValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in ServiceExecutionValidator.validate that, prevented a successful
        validation result from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SERVICE_EXECUTION_VALIDATION_FAILED"
    DEFAULT_MESSAGE = "ServiceExecution validation failed."