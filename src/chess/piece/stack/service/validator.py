# src/chess/agent/stack/service/coord_stack_validator.py

"""
Module: chess.agent.stack.service.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from typing import Any, cast

from chess.piece import (
    CannotRunServiceWithoutCoordStackException, CoordStackService, CoordStackValidator,
    InvalidCoordStackServiceException, NullCoordStackServiceException
)
from chess.system import LoggingLevelRouter, ValidationResult, Validator


class CoordStackServiceValidator(Validator[CoordStackService]):
    """
    # ROLE: Validation, Integrity Guarantor

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of CoordStackService, that meets integrity
    requirements, before the candidate is used.

    # PROVIDES:
    ValidationResult[CoordStackService] containing either:
        - On success: CoordStackService in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            coord_stack_validator: type[CoordStackValidator] = CoordStackValidator,
    ) -> ValidationResult[CoordStackService]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check if candidate is a CoordStackService. If so cast it.
        3.  Verify the CoordStackService.stack is not null.
        4.  Verify the CoordStackService.stack by running CoordStackService.validate_coord_stack.
        4.  If any check fails, return the exception inside a ValidationResult.
        5.  If all pass return the CoordStackStack object in a ValidationResult

        # PARAMETERS:
            *   candidate (Any):                                    Object to validate as a CoordStackService object.
            *   coord_stack_validator (type[CoordStackValidator]):  Validator to use to validate the stack attribute.

        # Returns:
        ValidationResult[CoordStackService] containing either:
            - On success:   CoordStackService in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullCoordStackServiceException
            *   InvalidCoordStackServiceException
            *   CannotRunServiceWithoutCoordStackException
        """
        method = "CoordStackServiceValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullCoordStackServiceException(
                        f"{method}: "
                        f"{NullCoordStackServiceException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, CoordStackService):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected CoordStackService, got {type(candidate).__name__} instead."
                    )
                )
            
            coord_stack_service = cast(CoordStackService, candidate)
            
            if coord_stack_service.stack is None:
                return ValidationResult.failure(
                    CannotRunServiceWithoutCoordStackException(
                        f"{method}: "
                        f"{CannotRunServiceWithoutCoordStackException.DEFAULT_MESSAGE}"
                    )
                )
            
            stack_validation = coord_stack_service.validate_coord_stack()
            if stack_validation.is_failure():
                return ValidationResult.failure(stack_validation.exception)
            
            return ValidationResult.success(coord_stack_service)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordStackServiceException(
                    ex=ex,
                    message=f"{method}: "
                            f"{InvalidCoordStackServiceException.DEFAULT_MESSAGE}"
                )
            )