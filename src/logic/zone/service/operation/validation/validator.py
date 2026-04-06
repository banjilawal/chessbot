# src/logic/zone/validation/validation.py

"""
Module: logic.zone.validation.validation
Author: Banji Lawal
Created: 2026-03-29
version: 1.0.0
"""

from __future__ import annotations
from typing import cast, Any

from logic.zone import Zone, NullZoneException
from logic.zone.service.operation.validation.exception.transaction import ZoneValidationException
from system import (
    NUMBER_OF_ROWS, Validator, ValidationResult, LoggingLevelRouter, NumberValidator
)

class ZoneValidator(Validator[Zone]):
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
                    rank: Any,
                    number_validation: NumberValidator,
            ) -> ValidationResult[Zone]

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            number_validation: NumberValidator = NumberValidator(),
    ) -> ValidationResult[Zone]:
        """
        Verify the rank is a Zone that is safe to use.
        
        Action:
            1.  Send an exception chain in the ValidationResult if
                    -   the rank does not exist.
                    -   the rank is not a Zone.
                    -   the row or column is not between [0-7] inclusive.
            2.  Otherwise, after the rank is cast to a Zone, send the success result.
        Args:
            candidate: Any
            number_validation: NumberValidator
        Returns:
            ValidationResult[Zone]
        Raises:
            TypeError
            NullZoneException
            ZoneValidationException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the rank does not exist.
        if candidate is None:
            # Return the exception on failure.
            return ValidationResult.failure(
                ZoneValidationException(
                    cls_mthd=method,
                    cls_name=method.__name__,
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
        # Handle the case that, the rank is the wrong type.
        if not isinstance(candidate, Zone):
            # Return the exception on failure.
            return ValidationResult.failure(
                ZoneValidationException(
                    cls_mthd=method,
                    cls_name=method.__name__,
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
            validate_result = number_validation.validate(
                ceiling=NUMBER_OF_ROWS,
                candidate=attribute,
                floor=0,
            )
            if validate_result.is_failure:
                # Return the exception on failure.
                return ValidationResult.failure(
                    ZoneValidationException(
                        cls_mthd=method,
                        cls_name=method.__name__,
                        op=ZoneValidationException.OP,
                        msg=ZoneValidationException.MSG,
                        err_code=ZoneValidationException.ERR_CODE,
                        rslt_type=ZoneValidationException.RSLT_TYPE,
                        ex=validate_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(zone)