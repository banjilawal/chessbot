# src/chess/vector/validator/validator.py

"""
Module: chess.vector.validator.validator
Author: Banji Lawal
Created: 2025-08-26
version: 1.0.0
"""

from typing import Any, cast


from chess.vector import (
  Vector, NullVectorException, NullXComponentException, NullYComponentException,
  VectorBelowBoundsException, VectorAboveBoundsException, InvalidVectorException
)
from chess.system import ValidationResult, Validator, LONGEST_KNIGHT_LEG_SIZE, LoggingLevelRouter


class VectorValidator(Validator[Vector]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Square instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT:
        *   Validator

    # PROVIDES:
        * SquareValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """


    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Vector]:
        """
        # ACTION:
        1.  Check candidate is not validation.
        2.  Check if candidate is a Vector.
        3.  Check candidate.x is:
                *   an INT
                *   between -LONGEST_KNIGHT_LEG_SIZE and -LONGEST_KNIGHT_LEG_SIZE exclusive.
        4.  Check candidate.y is:
                *   an INT
                *   between -LONGEST_KNIGHT_LEG_SIZE and -LONGEST_KNIGHT_LEG_SIZE exclusive.
        5.  If any check fails, return the exception inside a ValidationResult.
        6.  When all checks pass cast candidate to a Vector instance then return inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any): Object to validate.

        # Returns:
        ValidationResult[Vector] containing either:
            - On success: Vector in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullVectorException
            *   InvalidVectorException
        """
        method = "VectorValidator.validate"

        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullVectorException(f"{method}: {NullVectorException.DEFAULT_MESSAGE}")
                )


            if not isinstance(candidate, Vector):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Vector, got {type(candidate).__name__} instead.")
                )

            vector = cast(Vector, candidate)

            x_component_validation = cls.validate_x_component(x=vector.x)
            if x_component_validation.is_failure():
                return ValidationResult.failure(x_component_validation.exception)
            
            y_component_validation = cls.validate_y_component(y=vector.y)
            if y_component_validation.is_failure():
                return ValidationResult.failure(y_component_validation.exception)
            
            return ValidationResult.success(payload=vector)

        except Exception as ex:
            return ValidationResult.failure(
                InvalidVectorException(
                    ex=ex,
                    message=f"{method}: {InvalidVectorException.DEFAULT_MESSAGE}"
                )
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_x_component(cls, x_candidate: Any) -> ValidationResult[int]:
        """
        # ACTION:
        Check if the x component is a number within the bounds of the vector.

        # PARAMETERS:
            *   x_candidate (Any): The object to validate.

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullXComponentException
            *   VectorBelowBoundsException
            *   VectorAboveBoundsException
            *   InvalidVectorException
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
            
            if x < -LONGEST_KNIGHT_LEG_SIZE:
                return ValidationResult.failure(
                    VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if x >= LONGEST_KNIGHT_LEG_SIZE:
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
        # ACTION:
        Check if the y component is a number within the bounds of the vector.

        # PARAMETERS:
            *   y_candidate (Any): The object to validate.

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullYComponentException
            *   VectorBelowBoundsException
            *   VectorAboveBoundsException
            *   InvalidVectorException
        """
        method = "VectorValidator._validate_y_component"
        
        try:
            if y_candidate is None:
                return ValidationResult.failure(
                    NullYComponentException(
                        f"{method}: "
                        f"{NullYComponentException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(y_candidate, int):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected an int, got {type(x).__name__} instead."
                    )
                )
            y = cast(int, y_candidate)
            
            if y < -LONGEST_KNIGHT_LEG_SIZE:
                return ValidationResult.failure(
                    VectorBelowBoundsException(
                        f"{method}: "
                        f"{VectorBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if y >= LONGEST_KNIGHT_LEG_SIZE:
                return ValidationResult.failure(
                    VectorAboveBoundsException(
                        f"{method}:"
                        f" {VectorAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=y)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidVectorException(
                    ex=ex,
                    message=f"{method}: "
                            f"{InvalidVectorException.DEFAULT_MESSAGE}"
                )
            )