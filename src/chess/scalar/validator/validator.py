# src/chess/scalar/validator/validator.py

"""
Module: chess.scalar.validator.validator
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
     # ROLE: Validation, Data Integrity Guarantor, Security.
  
    # RESPONSIBILITIES:
    Prevents an object that does not meet the system's Scalar specifications from being used.
  
    # PROVIDES:
      ValidationResult[Scalar] containing either:
            - On success: Scalar in the payload.
            - On failure: Exception.
  
    # ATTRIBUTES:
        *   candidate (Any)
    """
    
    def __init__(self, candidate: Any):
        super().__init__(candidate)
    

    @LoggingLevelRouter.monitor
    def validate(self) -> ValidationResult[Scalar]:
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
        """
        method = "ScalarValidator.validate"
        
        try:
            if self.candidate is None:
                return ValidationResult.failure(
                    NullScalarException(
                        f"{method}: {NullScalarException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(self.candidate, Scalar):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected a Scaler got {type(self.candidate)} instead."
                    )
                )
            
            scalar = cast(Scalar, self.candidate)
            value_validation = self.validate_value(scalar.value)
            if value_validation.is_failure():
                return ValidationResult.failure(value_validation.exception)
            
            # if scalar.value is None:
            #     return ValidationResult.failure(
            #         NullNumberException(
            #             f"{method}: {NullNumberException.DEFAULT_MESSAGE}"
            #         )
            #     )
            #
            # if scalar.value < -BOARD_DIMENSION:
            #     return ValidationResult.failure(
            #         ScalarBelowBoundsException(
            #             f"{method}: {ScalarBelowBoundsException.DEFAULT_MESSAGE}"
            #         )
            #     )
            #
            # if scalar.value >= BOARD_DIMENSION:
            #     return ValidationResult.failure(
            #         ScalarAboveBoundsException(
            #             f"{method}: {ScalarAboveBoundsException.DEFAULT_MESSAGE}"
            #         )
            #     )
            
            return ValidationResult.success(payload=scalar)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidScalarException(
                    ex=ex,
                    message=f"{method}: {InvalidScalarException.DEFAULT_MESSAGE}"
                )
            )
    
    @LoggingLevelRouter.monitor
    def validate_value(self, candidate: Any) -> ValidationResult[int]:
        """
        # Action:
        Verifies candidate is a Scalar whose absolute value is within BOARD_DIMENSION.

        # Parameters:
          * candidate (Any): Object to verify is an int within the dimensions of the board.

        # Returns:
          ValidationResult[Scalar] containing either:
                - On success: Scalar in the payload.
                - On failure: Exception.

        # Raises:
            * TypeError
            * NullNumberException
            * InvalidScalarException
            * ScalarBelowBoundsException
            * ScalarAboveBoundsException
        """
        method = "ScalarValidator.validate"
        
        try:
            if self.candidate is None:
                return ValidationResult.failure(
                    NullScalarException(
                        f"{method}: {NullScalarException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(self.candidate, int):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected an int got {type(self.candidate)} instead."
                    )
                )
            
            value = cast(int, candidate)
            
            if value is None:
                return ValidationResult.failure(
                    NullNumberException(
                        f"{method}: {NullNumberException.DEFAULT_MESSAGE}"
                    )
                )
            
            if value < -BOARD_DIMENSION:
                return ValidationResult.failure(
                    ScalarBelowBoundsException(
                        f"{method}: {ScalarBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if value >= BOARD_DIMENSION:
                return ValidationResult.failure(
                    ScalarAboveBoundsException(
                        f"{method}: {ScalarAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=value)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidScalarException(
                    ex=ex,
                    message=f"{method}: {InvalidScalarException.DEFAULT_MESSAGE}"
                )
            )