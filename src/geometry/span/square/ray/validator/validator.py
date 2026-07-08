# src/geometry/span/square/ray/validation/validation.py

"""
Module: geometry.span.square.ray.validation
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, List, cast

from geometry.square import SquareValidator
from system import LoggingLevelRouter, ValidationResult, Validator
from math.span import SquareRay, SquareRayMembersNullException, SquareRayNullException, SquareRayValidatorException


class SquareRayValidator(Validator[SquareRay]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a rank is not null and the correct type before its used as a Span.Square.Ray.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Provides:


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
            1.  Send an exception chain in the ValidationResult if, the rank is either
                    *   nulI
                    *   is not a SquareRay instance.
            2.  Otherwise, cast the candidate into a SquareRay then, send in the success result.
            
        Args:
            candidate: Any
            square_validator: SquareRayValidator
            
        Returns:
            ValidationResult[SquareRay]
            
        Raises:
            TypeError
            SquareRayNullException
            SquareRayValidatorException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRayValidatorException(
                    cls_mthd=method,
                    op=SquareRayValidatorException.OP,
                    msg=SquareRayValidatorException.MSG,
                    err_code=SquareRayValidatorException.ERR_CODE,
                    mthd_rslt_type=SquareRayValidatorException.MTHD_RSLT,
                    ex=SquareRayNullException(
                        var="rank",
                        val="None",
                        msg=SquareRayNullException.MSG,
                        err_code=SquareRayNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SquareRay):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRayValidatorException(
                    cls_mthd=method,
                    op=SquareRayValidatorException.OP,
                    msg=SquareRayValidatorException.MSG,
                    err_code=SquareRayValidatorException.ERR_CODE,
                    mthd_rslt_type=SquareRayValidatorException.MTHD_RSLT,
                    ex=TypeError(f"{method} Expected SquareRay, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast candidate to a SquareRay for additional tests. ---#
        square_ray = cast(SquareRay, candidate)
        
        # Handle the case that, the origin does not pass square safety checks.
        origin_validation_result = square_validator.build(candidate=square_ray.origin)
        if origin_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRayValidatorException(
                    cls_mthd=method,
                    op=SquareRayValidatorException.OP,
                    msg=SquareRayValidatorException.MSG,
                    err_code=SquareRayValidatorException.ERR_CODE,
                    mthd_rslt_type=SquareRayValidatorException.MTHD_RSLT,
                    ex=origin_validation_result.exception
                )
            )
        # Handle the case that, the members are null
        if square_ray.members is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRayValidatorException(
                    cls_mthd=method,
                    op=SquareRayValidatorException.OP,
                    msg=SquareRayValidatorException.MSG,
                    err_code=SquareRayValidatorException.ERR_CODE,
                    mthd_rslt_type=SquareRayValidatorException.MTHD_RSLT,
                    ex=SquareRayMembersNullException(
                        var="ray.members",
                        val="None",
                        msg=SquareRayValidatorException.MSG,
                        err_code=SquareRayValidatorException.ERR_CODE,
                
                    )
                )
            )
        # Handle the case that, ray.members is null.
        if not isinstance(square_ray.members, List):
            # Send the exception chain on failure.
            wrong_type = type(square_ray.members).__name__
            return ValidationResult.failure(
                SquareRayValidatorException(
                    cls_mthd=method,
                    op=SquareRayValidatorException.OP,
                    msg=SquareRayValidatorException.MSG,
                    err_code=SquareRayValidatorException.ERR_CODE,
                    mthd_rslt_type=SquareRayValidatorException.MTHD_RSLT,
                    ex=SquareRayMembersNullException(
                        var="type(ray.members)",
                        val=wrong_type,
                        msg=SquareRayValidatorException.MSG,
                        err_code=SquareRayValidatorException.ERR_CODE,
                        ex=TypeError(
                            f"{method} Expected List[Square] for ray, got {wrong_type} instead."
                        )
                    )
                )
            )
        # --- Passed safet checks. Send the success result. ---#
        return ValidationResult.success(square_ray)
