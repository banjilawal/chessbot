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
from logic.coord.service.operation.validation.exception.work import CoordValidationException
from logic.system import NUMBER_OF_ROWS, ValidationProcess, ValidationResult, LoggingLevelRouter, NumberValidationProcess

class CoordValidationProcess(ValidationProcess[Coord]):
    """
     Role:
        -   Worker
        -   Integrity management

    Responsibilities:
        1.  Ensure a Coord instance is certified safe, reliable and consistent before use.
        
    Attributes:
    
    Provides:
       -    execute(
                    candidate: Any,
                    number_validation: NumberValidationProcess,
            ) -> ValidationResult[Coord]

    Super Class:
        ValidationProcess
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            number_validation: NumberValidationProcess = NumberValidationProcess(),
    ) -> ValidationResult[Coord]:
        """
        Verify the candidate is a Coord that is safe to use.
        
        Action:
            1.  Send an exception chain in the ValdationResult if
                    -   the candidate does not exist.
                    -   the candidate is not a Coord.
                    -   the row or column is not between [0-7] inclusive.
            2.  Otherwise, after the candidate is cast to a Coord, send the success result.
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
        
        # Handle the case that, either the row or column are not between [0-7] inclusive.
        for attribute in [coord.row, coord.column]:
            validate_result = number_validation.execute(
                ceiling=NUMBER_OF_ROWS,
                candidate=attribute,
                floor=0,
            )
            if validate_result.is_failure:
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
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(coord)