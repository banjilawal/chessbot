# chess/vector/validator.py

"""
Module: chess.vector.validator
Author: Banji Lawal
Created: 2025-08-26
version: 1.0.0
"""

from typing import Any, cast

from chess.system import ValidationResult, Validator,  KNIGHT_STEP_SIZE, LoggingLevelRouter
from chess.vector import (
  Vector, NullVectorException, NullXComponentException, NullYComponentException, VectorBelowBoundsException,
  VectorAboveBoundsException, InvalidVectorException
)

class VectorValidator(Validator[Vector]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    Prevents an object that does not meet the system's Vector specifications from being used.

    # PROVIDES:
      ValidationResult[Vector] containing either:
            - On success: Vector in payload.
            - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Vector]:
        """
        ACTION:
        Run checks to ensure the candidate is a Vector that meets safety requirements before its used.

        PARAMETERS:
            * candidate (Any): The object to vaildate.

        # Returns:
          ValidationResult[Scalar] containing either:
                - On success: Scalar in payload.
                - On failure: Exception.

        RAISES:
            * TypeError
            * NullVectorException
            * InvalidVectorException
        """
        method = "VectorValidator.validate"

        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullVectorException(f"{method}: {NullVectorException.DEFAULT_MESSAGE}")
                )


            if not isinstance(candidate, Vector):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an Vector, got {type(candidate).__name__} instead.")
                )

            vector = cast(Vector, candidate)

            x_component_validation = cls.validate_x_component(x=vector.x)
            if x_component_validation.is_failure():
                return ValidationResult.failure(x_component_validation.exception)
            
            y_component_validation = cls._y_component_validator(y=vector.y)
            if y_component_validation.is_failure():
                return ValidationResult.failure(y_component_validation.exception)
            
            return ValidationResult.success(payload=vector)

        except Exception as ex:
            return ValidationResult.failure(
                InvalidVectorException(f"{method}: {InvalidVectorException.DEFAULT_MESSAGE}", ex)
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_x_component(cls, x_candidate: Any) -> ValidationResult[int]:
        """
        ACTION:
        Check if the x component is a number within the bounds of the vector.

        PARAMETERS:
            * x_candidate (Any): The object to validate.

        # Returns:
          ValidationResult[int] containing either:
                - On success: int in payload.
                - On failure: Exception.

        RAISES:
            * TypeError
            * NullXComponentException
            * VectorBelowBoundsException
            * VectorAboveBoundsException
            * InvalidVectorException
        """
        method = "VectorValidator.validate_x_component"
        
        try:
            if x_candidate is None:
                return ValidationResult.failure(
                    NullXComponentException(f"{method}: {NullXComponentException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(x_candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an int, got {type(x_candidate).__name__} instead.")
                )
            x = cast(int, x_candidate)
            
            if x < -KNIGHT_STEP_SIZE:
                return ValidationResult.failure(
                    VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if x >= KNIGHT_STEP_SIZE:
                return ValidationResult.failure(
                    VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(payload=x)

        except Exception as ex:
            return ValidationResult.failure(
                InvalidVectorException(f"{method}: {InvalidVectorException.DEFAULT_MESSAGE}", ex)
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_y_component(cls, y_candidate: Any) -> ValidationResult[int]:
        """
        ACTION:
        Check if the y component is a number within the bounds of the vector.

        PARAMETERS:
            * y_candidate (Any): The object to validate.

        # Returns:
          ValidationResult[int] containing either:
                - On success: int in payload.
                - On failure: Exception.

        RAISES:
            * TypeError
            * NullYComponentException
            * VectorBelowBoundsException
            * VectorAboveBoundsException
            * InvalidVectorException
        """
        method = "VectorValidator._validate_y_component"
        
        try:
            if y_candidate is None:
                return ValidationResult.failure(
                    NullYComponentException(f"{method}: {NullYComponentException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(y_candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an int, got {type(x).__name__} instead.")
                )
            y = cast(int, y_candidate)
            
            if y < -KNIGHT_STEP_SIZE:
                return ValidationResult.failure(
                    VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if y >= KNIGHT_STEP_SIZE:
                return ValidationResult.failure(
                    VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(payload=y)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidVectorException(f"{method}: {InvalidVectorException.DEFAULT_MESSAGE}", ex)
            )