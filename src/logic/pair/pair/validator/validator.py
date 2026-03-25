# src/logic/pair/pair/validation/validation.py

"""
Module: logic.pair.pair.validation.validation
Author: Banji Lawal
Created: 2026-03-13
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast

from logic.node import NodeValidationProcess
from logic.edge import HeadCannotBeTailException
from logic.pair import Pair, NullPairException, PairValidationException
from logic.system import LoggingLevelRouter, ValidationResult, ValidationProcess


class PairValidationProcess(ValidationProcess[Pair]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a Pair instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

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
            node_validator: NodeValidationProcess = NodeValidationProcess(),
    ) -> ValidationResult[Pair]:
        """
        Actin:
            1.  If the candidate fails existence or type tests send the exception in the ValidationResult.
                Else, cast to Node instance, node.
            2.  If either the head, tail, distance, heuristic or weight fail verification send an exception chain
                in the ValidationResult. Else, send the node in the ValidationResult.
                
        Args:
            candidate: Any
            node_validator: NodeValidationProcess
            
        Returns:
            ValidationResult[Pair]
            
        Raises:
            TypeError
            NullPairException
            PairValidationException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PairValidationException(
                    mthd=method,
                    op=PairValidationException.OP,
                    msg=PairValidationException.MSG,
                    err_code=PairValidationException.ERR_CODE,
                    rslt_type=PairValidationException.RSLT_TYPE,
                    ex=NullPairException(
                        var="Candidate",
                        val={type(candidate).__name__},
                        msg=NullPairException.MSG,
                        err_code=NullPairException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Pair):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PairValidationException(
                    mthd=method,
                    op=PairValidationException.OP,
                    msg=PairValidationException.MSG,
                    err_code=PairValidationException.ERR_CODE,
                    rslt_type=PairValidationException.RSLT_TYPE,
                    ex=TypeError(f"Expected Pair, got {type(candidate).__name__}. instead")
                )
            )
        # --- Cast the candidate to an Node for additional tests ---#
        pair = cast(Pair, candidate)
        
        # Handle the case that either the head or tail does not pass a validation check.
        for member in pair.members:
            validation_result = node_validator.execute(candidate=member)
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    PairValidationException(
                        mthd=method,
                        op=PairValidationException.OP,
                        msg=PairValidationException.MSG,
                        err_code=PairValidationException.ERR_CODE,
                        rslt_type=PairValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
        # Handle the case that, the head and tail are the same.
        if pair.head == pair.tail:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PairValidationException(
                    mthd=method,
                    op=PairValidationException.OP,
                    msg=PairValidationException.MSG,
                    err_code=PairValidationException.ERR_CODE,
                    rslt_type=PairValidationException.RSLT_TYPE,
                    ex=HeadCannotBeTailException(
                        msg=PairValidationException.MSG,
                        err_code=PairValidationException.ERR_CODE,
                    )
                )
            )
        # --- The validation checks were passed, send the success result. ---#
        return ValidationResult.success(pair)