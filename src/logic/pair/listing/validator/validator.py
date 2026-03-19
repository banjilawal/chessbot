# src/logic/pair/listing/validator/validator.py

"""
Module: logic.pair.listing.validator
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast

from logic.pair import PairList, PairListNullException, PairListValidationException
from logic.system import LoggingLevelRouter, ValidationResult, ValidationProcess


class PairListValidationProcess(ValidationProcess[PairList]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a candidate is not null and the correct type before its used as a Pair.Listing.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[PairList]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if, the candidate is either
                    *   nulI
                    *   is not a PairList instance.
            2.  Otherwise, cast the candidate to a PairList then, send in the success result.
            
        Args:
            candidate: Any
            
        Returns:
            ValidationResult[PairList]
            
        Raises:
            TypeError
            PairListNullException
            PairListValidationException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PairListValidationException(
                    mthd=method,
                    op=PairListValidationException.OP,
                    msg=PairListValidationException.MSG,
                    err_code=PairListValidationException.ERR_CODE,
                    rslt_type=PairListValidationException.RSLT_TYPE,
                    ex=PairListNullException(
                        var="candidate",
                        val="None",
                        msg=PairListNullException.MSG,
                        err_code=PairListNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, PairList):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PairListValidationException(
                    mthd=method,
                    op=PairListValidationException.OP,
                    msg=PairListValidationException.MSG,
                    err_code=PairListValidationException.ERR_CODE,
                    rslt_type=PairListValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"{method} Expected PairList, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Safety checks are passed. Send the success result. ---#
        return ValidationResult.success(cast(PairList, candidate))
