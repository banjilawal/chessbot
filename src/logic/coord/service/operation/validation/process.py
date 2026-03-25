# src/logic/coord/validation/validation.py

"""
Module: logic.coord.validation.validation
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast, Any

from logic.coord import Coord, NullCoordException
from logic.coord.service.operation.validation.exception.wrapper import CoordValidationException
from logic.system import NUMBER_OF_ROWS, ValidationProcess, ValidationResult, LoggingLevelRouter, NumberValidationProcess

class CoordValidationProcess(ValidationProcess[Coord]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a Coord instance is certified safe, reliable and consistent before use.
    2.  Return useful debugging information if a candidate does not satisfy Coord integrity constraints.

    Super Class:
        *   ValidationProcess

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            number_validation: NumberValidationProcess = NumberValidationProcess(),
    ) -> ValidationResult[Coord]:
        """
        Action:
            1.  If the candidate fails existence or type checks send an exception chain in the ValidationResult.
                Else, cast to Coord instance coord.
            2.  If either coord.row or coord.column are not ints bound in the range [0, BOARD_DIMENSION] send an
                exception chain in the ValidationResult. Else, send coord in the ValidationResult.
        Args:
            candidate: Any
            number_validation: NumberValidationProcess
        Returns:
            ValidationResult[Coord]
        Raises:
            TypeError
            NullCoordException
            CoordValidationException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the candidate does not exist.
        if candidate is None:
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordValidationException.OP,
                    msg=CoordValidationException.MSG,
                    err_code=CoordValidationException.ERR_CODE,
                    rslt_type=CoordValidationException.RSLT_TYPE,
                    ex=NullCoordException(
                        msg=NullCoordException.MSG,
                        err_code=NullCoordException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the candidate is the wrong type.
        if not isinstance(candidate, Coord):
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordValidationException.OP,
                    msg=CoordValidationException.MSG,
                    err_code=CoordValidationException.ERR_CODE,
                    rslt_type=CoordValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected a Coord, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast candidate to a Coord for additional tests ---#
        coord = cast(Coord, candidate)
        
        # Handle the either the row or column are not between [0-7] inclusive.
        for attribute in [coord.row, coord.column]:
            validate_result = number_validation.execute(
                ceiling=NUMBER_OF_ROWS,
                candidate=attribute,
                floor=0,
            )
            # Return the exception on failure.
            return ValidationResult.failure(
                CoordValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordValidationException.OP,
                    msg=CoordValidationException.MSG,
                    err_code=CoordValidationException.ERR_CODE,
                    rslt_type=CoordValidationException.RSLT_TYPE,
                    ex=validate_result.exception
                )
            )
        # --- Cast candidate to a Coord for additional tests ---#
        return ValidationResult.success(oord)