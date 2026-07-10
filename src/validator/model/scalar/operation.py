# src/validator/scalar/validator.py

"""
Module: validator.scalar.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from model import Scalar
from setting import BoardProperty
from setting.board.dimension.config import BoardDimensionProperty
from toolkit import MathToolkit
from operation import Validator
from result import ValidationResult
from util import LoggingLevelRouter
from err import ScalarNullException, ScalarValidatorException


class ScalarValidator(ModelValidator[Scalar]):
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
             ScalarValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        if toolkit is None:
            toolkit = MathToolkit()
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=Scalar,
            context_null_exception=ScalarNullException(),
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast candidate to a Scalar for additional tests. ---#
        scalar = cast(Scalar, candidate)
        
        scalar_magnitude_validation_result = toolkit.number_validator.execute(
            candidate=scalar.magnitude,
            floor=0,
            ceiling=BoardDimensionProperty.entry[BoardProperty.MAX_ROW_INDEX],
        )
        if scalar_magnitude_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        return ValidationResult.success(scalar)