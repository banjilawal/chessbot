# src/chess/piece/stack/coord_stack_validator.py

"""
Module: chess.piece.stack.coord_stack_validator
Author: Banji Lawal
Created: 2025-09-30
version: 1.0.0
"""

from typing import Any, cast

from chess.system import LoggingLevelRouter, Validator, ValidationResult
from chess.piece import (
    CoordStack, CoordStackSizeConflictException, CorruptedCoordStackException,
    InconsistentCurrentCoordException, InvalidCoordStackException, NullCoordStackException
)


class CoordStackValidator(Validator[CoordStack]):
    """
    # ROLE: Validation, Integrity Guarantor
  
    # RESPONSIBILITIES:
    Verifies a candidate is an instance of CoordStack, that meets integrity
    requirements, before the candidate is used.
  
    # PROVIDES:
    ValidationResult[CoordStack] containing either:
        - On success: CoordStack in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    No attributes
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[CoordStack]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check if candidate is a CoordStack. If so cast it.
        3.  Verify the CoordStack.items is not null.
        4.  Verify Coordstack.size and CoordStack.is_empty() do not conflict.
        5.  Verify CoordStack.current_coord is null if CoordStack.is_empty()
            do not conflict.
        6.  If any check fails, return the exception inside a ValidationResult.
        7.  If all pass return the CoordStack object in a ValidationResult
    
        # PARAMETERS:
            *   candidate (Any):  Object to validate as a CoordStack object.
    
        # Returns:
        ValidationResult[CoordStack] containing either:
            - On success:   CoordStack in the payload.
            - On failure:   Exception.
    
        # RAISES:
            *   TypeError
            *   NullCoordStackException
            *   CorruptedCoordStackException
            *   InconsistentCurrentCoordException
            *   CoordStackNotRegisteredWithAgentException
            *   InvalidCoordStackException
        """
        method = "CoordinateStackValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullCoordStackException(
                        f"{method}: {NullCoordStackException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, CoordStack):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}:"
                        f" Expected CoordStack, got {type(candidate).__name__} instead."
                    )
                )
            
            coord_stack = cast(CoordStack, candidate)
            
            if coord_stack.items is None:
                return ValidationResult.failure(
                    CorruptedCoordStackException(
                        f"{method} {CorruptedCoordStackException.DEFAULT_MESSAGE}"
                    )
                )
            
            if (
                    coord_stack.size > 0 and coord_stack.is_empty() or
                    coord_stack.size == 0 and not coord_stack.is_empty()
            ):
                return ValidationResult.failure(
                    CoordStackSizeConflictException(
                        f"{method}: {CoordStackSizeConflictException.DEFAULT_MESSAGE}"
                    )
                )
            
            if (
                    coord_stack.is_empty() and coord_stack.current_coord is not None or
                    not coord_stack.is_empty() and coord_stack.current_coordStack is None
            ):
                return ValidationResult.failure(
                    InconsistentCurrentCoordException(
                        f"{method}: {InconsistentCurrentCoordException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=coord_stack)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordStackException(
                    f"{method}: {InvalidCoordStackException.DEFAULT_MESSAGE}",
                    ex
                )
            )
