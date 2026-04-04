# src/logic/vector/service/operation/validate/validator.py

"""
Module: logic.vector.service.operation.validate.validator
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import Any, cast

from system import (
    LONGEST_KNIGHT_LEG_SIZE, LoggingLevelRouter, NumberValidator, ValidationResult,
    Validator
)
from geometry.vector import NullVectorException, Vector
from geometry.vector import VectorValidationException


class VectorValidator(Validator[Vector]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Vector instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    number_validator: NumberValidator = NumberValidator()
            ) -> ValidationResult[Vector]:

    Super Class:
        Validator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator()
    ) -> ValidationResult[Vector]:
        """
        Check if a Vector is safe to use.
        
        Action:
            1.  Send an exception in the ValidationResult if either x or y
                    -   Is null
                    -   Not a number
                    -   Out of  bounds.
            2.  Otherwise, send the success result.
        Args:
             candidate: Any
             number_validator: NumberValidator
        Returns:
            ValidationResult[Vector]
        Raises:
            TypeError
            NullVectorException
            VectorValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorValidationException.OP,
                    msg=VectorValidationException.MSG,
                    err_code=VectorValidationException.ERR_CODE,
                    rslt_type=VectorValidationException.RSLT_TYPE,
                    ex=NullVectorException(
                        msg=VectorValidationException.MSG,
                        err_code=VectorValidationException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Vector):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorValidationException.OP,
                    msg=VectorValidationException.MSG,
                    err_code=VectorValidationException.ERR_CODE,
                    rslt_type=VectorValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected a Vector, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate to a Vector for additional tests ---#
        vector = cast(Vector, candidate)
        
        # Handle the case that, either component is out of bounds.
        for num in [vector.x, vector.y]:
            validation_result = number_validator.validate(
                floor=0,
                ceiling=LONGEST_KNIGHT_LEG_SIZE,
                candidate=abs(num)
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    VectorValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=VectorValidationException.OP,
                        msg=VectorValidationException.MSG,
                        err_code=VectorValidationException.ERR_CODE,
                        rslt_type=VectorValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(vector)