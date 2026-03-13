# src/logic/span/square/span/validator/validator.py

"""
Module: logic.span.square.span.validator
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, List, cast

from logic.square import SquareValidator
from logic.system import LoggingLevelRouter, ValidationResult, Validator
from logic.span import NullSquareSpanException, SquareSpan, SquareSpanMembersNullException, SquareSpanValidationException


class SquareSpanValidator(Validator[SquareSpan]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a candidate is not null and the correct type before its used as a Span.Square.Span.
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
    ) -> ValidationResult[SquareSpan]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if, the candidate is either
                    *   nulI
                    *   is not a SquareSpan instance.
            2.  Otherwise, cast the candidate to a SquareSpan then, send in the success result.
            
        Args:
            candidate: Any
            square_validator: SquareSpanValidator
            
        Returns:
            ValidationResult[SquareSpan]
            
        Raises:
            TypeError
            NullSquareSpanException
            SquareSpanValidationException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareSpanValidationException(
                    mthd=method,
                    op=SquareSpanValidationException.OP,
                    msg=SquareSpanValidationException.MSG,
                    err_code=SquareSpanValidationException.ERR_CODE,
                    rslt_type=SquareSpanValidationException.RSLT_TYPE,
                    ex=NullSquareSpanException(
                        var="candidate",
                        val="None",
                        msg=NullSquareSpanException.MSG,
                        err_code=NullSquareSpanException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SquareSpan):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareSpanValidationException(
                    mthd=method,
                    op=SquareSpanValidationException.OP,
                    msg=SquareSpanValidationException.MSG,
                    err_code=SquareSpanValidationException.ERR_CODE,
                    rslt_type=SquareSpanValidationException.RSLT_TYPE,
                    ex=TypeError(f"{method} Expected SquareSpan, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast candidate to a SquareSpan for additional tests. ---#
        square_span = cast(SquareSpan, candidate)
        
        # Handle the case that, the origin does not pass square safety checks.
        origin_validation_result = square_validator.validate(candidate=square_span.origin)
        if origin_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareSpanValidationException(
                    mthd=method,
                    op=SquareSpanValidationException.OP,
                    msg=SquareSpanValidationException.MSG,
                    err_code=SquareSpanValidationException.ERR_CODE,
                    rslt_type=SquareSpanValidationException.RSLT_TYPE,
                    ex=origin_validation_result.exception
                )
            )
        # Handle the case that, the members are null
        if square_span.members is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareSpanValidationException(
                    mthd=method,
                    op=SquareSpanValidationException.OP,
                    msg=SquareSpanValidationException.MSG,
                    err_code=SquareSpanValidationException.ERR_CODE,
                    rslt_type=SquareSpanValidationException.RSLT_TYPE,
                    ex=SquareSpanMembersNullException(
                        var="square_span.members",
                        val="None",
                        msg=SquareSpanValidationException.MSG,
                        err_code=SquareSpanValidationException.ERR_CODE,
                
                    )
                )
            )
        # Handle the case that, square_span.members is null.
        if not isinstance(square_span.members, List):
            # Return the exception chain on failure.
            wrong_type = type(square_span.members).__name__
            return ValidationResult.failure(
                SquareSpanValidationException(
                    mthd=method,
                    op=SquareSpanValidationException.OP,
                    msg=SquareSpanValidationException.MSG,
                    err_code=SquareSpanValidationException.ERR_CODE,
                    rslt_type=SquareSpanValidationException.RSLT_TYPE,
                    ex=SquareSpanMembersNullException(
                        var="type(square_span.members)",
                        val=wrong_type,
                        msg=SquareSpanValidationException.MSG,
                        err_code=SquareSpanValidationException.ERR_CODE,
                        ex=TypeError(
                            f"{method} Expected List[Square] for square_span, got {wrong_type} instead."
                        )
                    )
                )
            )
        # --- Passed safet checks. Send the success result. ---#
        return ValidationResult.success(square_span)
