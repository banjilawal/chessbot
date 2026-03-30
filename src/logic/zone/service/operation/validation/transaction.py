# src/logic/zone/validation/validation.py

"""
Module: logic.zone.validation.validation
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast, Any

from logic.zone import Zone, NullZoneException
from logic.zone.service.operation.validation.exception.work import ZoneValidationException
from logic.system import (
    NUMBER_OF_ROWS, ValidationTransaction, ValidationResult, LoggingLevelRouter, NumberValidationTransaction
)

class ZoneValidationTransaction(ValidationTransaction[Zone]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Zone instance is certified safe, reliable and consistent before use.
        
    Attributes:
    
    Provides:
       -    execute(
                    candidate: Any,
                    number_validation: NumberValidationTransaction,
            ) -> ValidationResult[Zone]

    Super Class:
        ValidationTransaction
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            number_validation: NumberValidationTransaction = NumberValidationTransaction(),
    ) -> ValidationResult[Zone]:
        """
        Verify the candidate is a Zone that is safe to use.
        
        Action:
            1.  Send an exception chain in the ValdationResult if
                    -   the candidate does not exist.
                    -   the candidate is not a Zone.
                    -   the row or column is not between [0-7] inclusive.
            2.  Otherwise, after the candidate is cast to a Zone, send the success result.
        Args:
            candidate: Any
            number_validation: NumberValidationTransaction
        Returns:
            ValidationResult[Zone]
        Raises:
            TypeError
            NullZoneException
            ZoneValidationException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the candidate does not exist.
        if candidate is None:
            # Return the exception on failure.
            return ValidationResult.failure(
                ZoneValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=ZoneValidationException.OP,
                    msg=ZoneValidationException.MSG,
                    err_code=ZoneValidationException.ERR_CODE,
                    rslt_type=ZoneValidationException.RSLT_TYPE,
                    ex=NullZoneException(
                        msg=NullZoneException.MSG,
                        err_code=NullZoneException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the candidate is the wrong type.
        if not isinstance(candidate, Zone):
            # Return the exception on failure.
            return ValidationResult.failure(
                ZoneValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=ZoneValidationException.OP,
                    msg=ZoneValidationException.MSG,
                    err_code=ZoneValidationException.ERR_CODE,
                    rslt_type=ZoneValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected a Zone, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast candidate to a Zone for additional tests ---#
        zone = cast(Zone, candidate)
        
        # Handle the case that, either the row or column are not between [0-7] inclusive.
        for attribute in [zone.row, zone.column]:
            validate_result = number_validation.execute(
                ceiling=NUMBER_OF_ROWS,
                candidate=attribute,
                floor=0,
            )
            if validate_result.is_failure:
                # Return the exception on failure.
                return ValidationResult.failure(
                    ZoneValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=ZoneValidationException.OP,
                        msg=ZoneValidationException.MSG,
                        err_code=ZoneValidationException.ERR_CODE,
                        rslt_type=ZoneValidationException.RSLT_TYPE,
                        ex=validate_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(zone)