# src/validation/scalar/validator.py

"""
Module: validation.scalar.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from model import Scalar
from setting import BoardProperty
from setting.board.dimension.config import BoardDimensionPropertyTable
from toolkit import MathToolkit
from operation import Validator
from result import ValidationResult
from util import LoggingLevelRouter
from err import ScalarNullException, ScalarValidationException


class ScalarValidator(Validator[Scalar]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Scalar instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(candidate: Any, toolkit: MathToolkit) -> ValidationResult[Scalar]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "scalar_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: MathToolkit | None = None,
    ) -> ValidationResult[Scalar]:
        """
        Verify the object is a Scalar that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate either null or not a Scalar.
                    _   Its absolute value is > BOARD_DIMENSION.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: ScalarToolkit
        Returns:
            ValidationResult[Scalar]
        Raises:
             ScalarValidationException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = MathToolkit()
        
        # Handle the case that, the candidate does not exist.
        validation_priming_result = toolkit.validation_primer.validate(
            candidate=candidate,
            target_model=Scalar,
            context_null_exception=ScalarNullException(),
        )
        if validation_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ScalarValidationException.MSG,
                    err_code=ScalarValidationException.ERR_CODE,
                    ex=validation_priming_result.exception,
                )
            )
        # --- Cast candidate to a Scalar for additional tests. ---#
        scalar = cast(Scalar, candidate)
        
        scalar_magnitude_validation_result = toolkit.number_validator.validate(
            candidate=scalar.magnitude,
            floor=0,
            ceiling=BoardDimensionPropertyTable.entry[BoardProperty.MAX_ROW_INDEX],
        )
        if scalar_magnitude_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ScalarValidationException.MSG,
                    err_code=ScalarValidationException.ERR_CODE,
                    ex=validation_priming_result.exception,
                )
            )
        return ValidationResult.success(scalar)