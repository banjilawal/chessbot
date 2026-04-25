# src/operation/validation/scalar/operation.py

"""
Module: operation.validation.scalar.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class ScalarValidator(Validator[Scalar]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a Scalar instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   Validator

    # PROVIDES:
        * ScalarValidator


    # INHERITED ATTRIBUTES:
    None
    """
    
    def __init__(self, candidate: Any):
        super().__init__(candidate)
    

    @LoggingLevelRouter.monitor
    def validate(self) -> ValidationResult[Scalar]:
        """
        # ACTION:
        Verifies rank is a Scalar whose absolute value is within BOARD_DIMENSION.
    
        # PARAMETERS:
          * rank (Any): Object to verify is a Scalar.
    
        # RETURNS:
          ValidationResult[Scalar] containing either:
                - On success: Scalar in the payload.
                - On failure: Exception.
    
        Raises:
            * TypeError
            * NullScalarException
        """
        method = "ScalarValidator.validate"
        
        try:
            if self.candidate is None:
                return ValidationResult.failure(
                    NullScalarException(
                        f"{method}: {NullScalarException.MSG}"
                    )
                )
            
            if not isinstance(self.candidate, Scalar):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected a Scaler, got {type(self.candidate)} instead."
                    )
                )
            
            scalar = cast(Scalar, self.candidate)
            value_validation = self.validate_value(scalar.value)
            if value_validation.is_failure():
                return ValidationResult.failure(value_validation.exception)
            
            # if scalar.value is None:
            #     return ValidationResult.failure(
            #         NullNumberException(
            #             f"{method}: {NullNumberException.MSG}"
            #         )
            #     )
            #
            # if scalar.value < -BOARD_DIMENSION:
            #     return ValidationResult.failure(
            #         ScalarBelowBoundsException(
            #             f"{method}: {ScalarBelowBoundsException.MSG}"
            #         )
            #     )
            #
            # if scalar.value >= BOARD_DIMENSION:
            #     return ValidationResult.failure(
            #         ScalarAboveBoundsException(
            #             f"{method}: {ScalarAboveBoundsException.MSG}"
            #         )
            #     )
            
            return ValidationResult.success(payload=scalar)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidScalarException(
                    ex=ex,
                    msg=f"{method}: {InvalidScalarException.MSG}"
                )
            )
    
    @LoggingLevelRouter.monitor
    def validate_value(self, candidate: Any) -> ValidationResult[int]:
        """
        # ACTION:
        Verifies rank is a Scalar whose absolute value is within BOARD_DIMENSION.

        # PARAMETERS:
          * rank (Any): Object to verify is an int within the dimensions of the board.

        # RETURNS:
          ValidationResult[Scalar] containing either:
                - On success: Scalar in the payload.
                - On failure: Exception.

        Raises:
            * TypeError
            * NullNumberException
            * ScalarValidationException
            * ScalarBelowBoundsException
            * ScalarAboveBoundsException
        """
        method = "ScalarValidator.validate"
        
        try:
            if self.candidate is None:
                return ValidationResult.failure(
                    NullScalarException(
                        f"{method}: {NullScalarException.MSG}"
                    )
                )
            
            if not isinstance(self.candidate, int):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected an int, got {type(self.candidate)} instead."
                    )
                )
            
            value = cast(int, candidate)
            
            if value is None:
                return ValidationResult.failure(
                    NullNumberException(
                        f"{method}: {NullNumberException.MSG}"
                    )
                )
            
            if value < -BOARD_DIMENSION:
                return ValidationResult.failure(
                    ScalarBelowBoundsException(
                        f"{method}: {ScalarBelowBoundsException.MSG}"
                    )
                )
            
            if value >= BOARD_DIMENSION:
                return ValidationResult.failure(
                    ScalarAboveBoundsException(
                        f"{method}: {ScalarAboveBoundsException.MSG}"
                    )
                )
            
            return ValidationResult.success(payload=value)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidScalarException(
                    ex=ex,
                    msg=f"{method}: {InvalidScalarException.MSG}"
                )
            )