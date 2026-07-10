# src/validator/coord/validator.py

"""
Module: validator.coord.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from model import Coord
from toolkit import MathToolkit
from operation import Validator
from result import ValidationResult
from util import LoggingLevelRouter, NUMBER_OF_ROWS
from err import CoordNullException, CoordValidatorException


class CoordValidator(ModelValidator[Coord]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Coord instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                     toolkit: MathToolkit
            ) -> ValidationResult[Coord]:

    Super Class:
        ModelValidator
    """
    OPERATION_NAME = "coord_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: MathToolkit | None = None
    ) -> ValidationResult[Coord]:
        """
        Check if a Coord is safe to use.

        Action:
            1.  Send an exception in the ValidationResult if either x or y
                    -   Is null
                    -   Not a number
                    -   Out of  bounds.
            2.  Otherwise, send the success result.
        Args:
             candidate: Any
             toolkit: MathToolkit
        Returns:
            ValidationResult[Coord]
        Raises:
            TypeError
            NullCoordException
            CoordValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        if toolkit is None:
            toolkit = MathToolkit()
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=Coord,
            context_null_exception=CoordNullException(),
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidatorException.MSG,
                    err_code=CoordValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate to a Coord for additional tests ---#
        coord = cast(Coord, candidate)
        
        # Handle the case that, either the row or column are not between [0-7] inclusive.
        for attribute in [coord.row, coord.column]:
            number_validation_result = toolkit.number_validator.execute(
                ceiling=NUMBER_OF_ROWS,
                candidate=attribute,
                floor=0,
            )
            if number_validation_result.is_failure:
                # Return the exception on failure.
                return ValidationResult.failure(
                    CoordValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordValidatorException.MSG,
                        err_code=CoordValidatorException.ERR_CODE,
                        ex=number_validation_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(coord)