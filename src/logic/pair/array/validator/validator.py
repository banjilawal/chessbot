# src/logic/pair/array/validator/validator.py

"""
Module: logic.pair.array.validator
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from typing import Any, cast

from logic.node import NodePairList, NodePairListNullException, NodePairListValidationException
from logic.system import LoggingLevelRouter, ValidationResult, Validator


class NodePairListValidator(Validator[NodePairList]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a candidate is not null and the correct type before its used as a Pair.Array.
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
    def validate(cls, candidate: Any) -> ValidationResult[NodePairList]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if, the candidate is either
                    *   nulI
                    *   is not a NodePairList instance.
            2.  Otherwise, cast the candidate to a NodePairList then, send in the success result.
            
        Args:
            candidate: Any
            
        Returns:
            ValidationResult[NodePairList]
            
        Raises:
            TypeError
            NodePairListNullException
            NodePairListValidationException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodePairListValidationException(
                    mthd=method,
                    op=NodePairListValidationException.OP,
                    msg=NodePairListValidationException.MSG,
                    err_code=NodePairListValidationException.ERR_CODE,
                    rslt_type=NodePairListValidationException.RSLT_TYPE,
                    ex=NodePairListNullException(
                        var="candidate",
                        val="None",
                        msg=NodePairListNullException.MSG,
                        err_code=NodePairListNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, NodePairList):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodePairListValidationException(
                    mthd=method,
                    op=NodePairListValidationException.OP,
                    msg=NodePairListValidationException.MSG,
                    err_code=NodePairListValidationException.ERR_CODE,
                    rslt_type=NodePairListValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"{method} Expected NodePairList, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Safety checks are passed. Send the success result. ---#
        return ValidationResult.success(cast(NodePairList, candidate))
