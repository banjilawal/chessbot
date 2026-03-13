# src/logic/span/square/ray/validator/validator.py

"""
Module: logic.span.square.ray.validator
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, List, cast

from logic.square import SquareValidator
from logic.system import LoggingLevelRouter, ValidationResult, Validator
from logic.span import NullSquareRayException, SquareRay, SquareRayMembersNullException, SquareRayValidationException


class SquareRayValidator(Validator[SquareRay]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a candidate is not null and the correct type before its used as a Span.Square.Ray.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            square_validator: SquareValidator = SquareValidator(),
    ) -> ValidationResult[SquareRay]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if, the candidate is either
                    *   nulI
                    *   is not a SquareRay instance.
            2.  Otherwise, cast the candidate to a SquareRay then, send in the success result.
            
        Args:
            candidate: Any
            square_validator: SquareRayValidator
            
        Returns:
            ValidationResult[SquareRay]
            
        Raises:
            TypeError
            NullSquareRayException
            SquareRayValidationException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareRayValidationException(
                    mthd=method,
                    op=SquareRayValidationException.OP,
                    msg=SquareRayValidationException.MSG,
                    err_code=SquareRayValidationException.ERR_CODE,
                    rslt_type=SquareRayValidationException.RSLT_TYPE,
                    ex=NullSquareRayException(
                        var="candidate",
                        val="None",
                        msg=NullSquareRayException.MSG,
                        err_code=NullSquareRayException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SquareRay):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareRayValidationException(
                    mthd=method,
                    op=SquareRayValidationException.OP,
                    msg=SquareRayValidationException.MSG,
                    err_code=SquareRayValidationException.ERR_CODE,
                    rslt_type=SquareRayValidationException.RSLT_TYPE,
                    ex=TypeError(f"{method} Expected SquareRay, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast candidate to a SquareRay for additional tests. ---#
        square_ray = cast(SquareRay, candidate)
        
        # Handle the case that, the origin does not pass square safety checks.
        origin_validation_result = square_validator.validate(candidate=square_ray.origin)
        if origin_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareRayValidationException(
                    mthd=method,
                    op=SquareRayValidationException.OP,
                    msg=SquareRayValidationException.MSG,
                    err_code=SquareRayValidationException.ERR_CODE,
                    rslt_type=SquareRayValidationException.RSLT_TYPE,
                    ex=origin_validation_result.exception
                )
            )
        # Handle the case that, the members are null
        if square_ray.members is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareRayValidationException(
                    mthd=method,
                    op=SquareRayValidationException.OP,
                    msg=SquareRayValidationException.MSG,
                    err_code=SquareRayValidationException.ERR_CODE,
                    rslt_type=SquareRayValidationException.RSLT_TYPE,
                    ex=SquareRayMembersNullException(
                        var="square_ray.members",
                        val="None",
                        msg=SquareRayValidationException.MSG,
                        err_code=SquareRayValidationException.ERR_CODE,
                
                    )
                )
            )
        # Handle the case that, square_ray.members is null.
        if not isinstance(square_ray.members, List):
            # Return the exception chain on failure.
            wrong_type = type(square_ray.members).__name__
            return ValidationResult.failure(
                SquareRayValidationException(
                    mthd=method,
                    op=SquareRayValidationException.OP,
                    msg=SquareRayValidationException.MSG,
                    err_code=SquareRayValidationException.ERR_CODE,
                    rslt_type=SquareRayValidationException.RSLT_TYPE,
                    ex=SquareRayMembersNullException(
                        var="type(square_ray.members)",
                        val=wrong_type,
                        msg=SquareRayValidationException.MSG,
                        err_code=SquareRayValidationException.ERR_CODE,
                        ex=TypeError(
                            f"{method} Expected List[Square] for square_ray, got {wrong_type} instead."
                        )
                    )
                )
            )
        # --- Passed safet checks. Send the success result. ---#
        return ValidationResult.success(square_ray)
