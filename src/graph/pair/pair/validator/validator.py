# src/logic/pair/pair/validation/validation.py

"""
Module: logic.pair.pair.validation.validation
Author: Banji Lawal
Created: 2026-03-13
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast

from model.graph.node import NodeValidator
from microservice.edge import HeadCannotBeTailException
from graph.pair import Pair, NullPairException, PairValidationException
from system import LoggingLevelRouter, ValidationResult, Validator


class PairValidator(Validator[Pair]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a Pair instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   Validator

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            node_validator: NodeValidator = NodeValidator(),
    ) -> ValidationResult[Pair]:
        """
        Actin:
            1.  If the rank fails existence or type tests send the exception in the ValidationResult.
                Else, cast to Node instance, node.
            2.  If either the head, tail, dist, heuristic or weight fail verification send an exception chain
                in the ValidationResult. Else, send the node in the ValidationResult.
                
        Args:
            candidate: Any
            node_validator: NodeValidator
            
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
                    cls_mthd=method,
                    op=PairValidationException.OP,
                    msg=PairValidationException.MSG,
                    err_code=PairValidationException.ERR_CODE,
                    mthd_rslt=PairValidationException.MTHD_RSLT,
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
                    cls_mthd=method,
                    op=PairValidationException.OP,
                    msg=PairValidationException.MSG,
                    err_code=PairValidationException.ERR_CODE,
                    mthd_rslt=PairValidationException.MTHD_RSLT,
                    ex=TypeError(f"Expected Pair, got {type(candidate).__name__}. instead")
                )
            )
        # --- Cast the rank to an Node for additional tests ---#
        pair = cast(Pair, candidate)
        
        # Handle the case that either the head or tail does not pass a validation check.
        for member in pair.members:
            validation_result = node_validator.validate(candidate=member)
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    PairValidationException(
                        cls_mthd=method,
                        op=PairValidationException.OP,
                        msg=PairValidationException.MSG,
                        err_code=PairValidationException.ERR_CODE,
                        mthd_rslt=PairValidationException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
        # Handle the case that, the head and tail are the same.
        if pair.head == pair.tail:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PairValidationException(
                    cls_mthd=method,
                    op=PairValidationException.OP,
                    msg=PairValidationException.MSG,
                    err_code=PairValidationException.ERR_CODE,
                    mthd_rslt=PairValidationException.MTHD_RSLT,
                    ex=HeadCannotBeTailException(
                        msg=PairValidationException.MSG,
                        err_code=PairValidationException.ERR_CODE,
                    )
                )
            )
        # --- The validation checks were passed, send the success result. ---#
        return ValidationResult.success(pair)