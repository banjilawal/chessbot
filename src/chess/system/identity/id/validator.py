# src/chess/system/identity/id/coord_stack_validator.py

"""
Module: chess.system.identity.id.coord_stack_validator
Author: Banji Lawal
Created: 2025-08-12
"""

from typing import cast

from chess.system import (
    Validator, ValidationResult, IdNullException, NegativeIdException, InvalidIdException, LoggingLevelRouter,
)


class IdValidator(Validator[int]):
    """
    # ROLE: Validation, Integrity
  
    # RESPONSIBILITIES:
    Verifies a candidate is an INT greater than zero before its used an ID.
  
    # PROVIDES:
    ValidationResult[int] containing either:
        - On success: int in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: int) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Test if the candidate is:
                *   Not validation.
                *   A positive integer.
        2.  If either text fails send their exception in a ValidationResult.
        3.  When all checks pass cast the candidate to an INT then send inside a ValidationResult.
    
        # PARAMETERS:
            *   candidate (Any): object to certify is a legal ID.
    
        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.
    
        # Raises:
          *     TypeError
          *     IdNULLException
          *     NegativeIdException
        """
        method = "IdValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    IdNullException(f"{method}: {IdNullException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected an integer, got {type(candidate).__id__} instead."
                    )
                )
            
            id = cast(int, candidate)
            
            if id < 0:
                return ValidationResult.failure(
                    NegativeIdException(
                        f"{method}: {NegativeIdException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=id)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidIdException(
                    f"{method}: {InvalidIdException.DEFAULT_MESSAGE}",
                    ex
                )
            )
