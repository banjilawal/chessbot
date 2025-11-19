# src/chess/scalar/coord_stack_validator.py

"""
Module: chess.scalar.coord_stack_validator
Author: Banji Lawal
Created: 2025-08-26
version: 1.0.0
"""


from typing import Any, cast

from chess.system import ValidationResult, Validator, BOARD_DIMENSION, LoggingLevelRouter, NullNumberException
from chess.scalar import (
    Scalar, NullScalarException, ScalarBelowBoundsException, ScalarAboveBoundsException, InvalidScalarException
)


class ScalarValidator(Validator[Scalar]):
    """
    # ROLE: Validation
  
    # RESPONSIBILITIES:
    Prevents an object that does not meet the system's Scalar specifications from being used.
  
    # PROVIDES:
      ValidationResult[Scalar] containing either:
            - On success: Scalar in the payload.
            - On failure: Exception.
  
    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Scalar]:
        """
        # Action:
        Verifies candidate is a Scalar whose absolute value is within BOARD_DIMENSION.
    
        # Parameters:
          * candidate (Any): Object to verify is a Scalar.
    
        # Returns:
          ValidationResult[Scalar] containing either:
                - On success: Scalar in the payload.
                - On failure: Exception.
    
        # Raises:
            * TypeError
            * NullScalarException
            * NullNumberException
            * InvalidScalarException
            * ScalarBelowBoundsException
            * ScalarAboveBoundsException
        """
        method = "ScalarValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullScalarException(f"{method}: {NullScalarException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Scalar):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Scaler got {type(candidate)} instead.")
                )
            
            scalar = cast(Scalar, candidate)
            
            if scalar.value is None:
                return ValidationResult.failure(
                    NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")
                )
            
            if scalar.value < -BOARD_DIMENSION:
                return ValidationResult.failure(
                    ScalarBelowBoundsException(f"{method}: {ScalarBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if scalar.value >= BOARD_DIMENSION:
                return ValidationResult.failure(
                    ScalarAboveBoundsException(
                        f"{method}: {ScalarAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=scalar)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidScalarException(f"{method}: {InvalidScalarException.DEFAULT_MESSAGE}", ex)
            )
