# src/logic/pair/pair/validator/validator.py

"""
Module: logic.pair.pair.validator.validator
Author: Banji Lawal
Created: 2026-03-13
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast

from logic.node import NodeValidator
from logic.edge import HeadCannotBeTailException
from logic.pair import NodePair, NodePairNullException, NodePairValidationException
from logic.system import LoggingLevelRouter, ValidationResult, Validator


class NodePairValidator(Validator[NodePair]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a NodePair instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

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
            node_validator: NodeValidator = NodeValidator(),
    ) -> ValidationResult[NodePair]:
        """
        Actin:
            1.  If the candidate fails existence or type tests send the exception in the ValidationResult.
                Else, cast to Node instance, node.
            2.  If either the head, tail, distance, heuristic or weight fail verification send an exception chain
                in the ValidationResult. Else, send the node in the ValidationResult.
                
        Args:
            candidate: Any
            node_validator: NodeValidator
            
        Returns:
            ValidationResult[NodePair]
            
        Raises:
            TypeError
            NodePairNullException
            NodePairValidationException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodePairValidationException(
                    mthd=method,
                    op=NodePairValidationException.OP,
                    msg=NodePairValidationException.MSG,
                    err_code=NodePairValidationException.ERR_CODE,
                    rslt_type=NodePairValidationException.RSLT_TYPE,
                    ex=NodePairNullException(
                        var="Candidate",
                        val={type(candidate).__name__},
                        msg=NodePairNullException.MSG,
                        err_code=NodePairNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, NodePair):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodePairValidationException(
                    mthd=method,
                    op=NodePairValidationException.OP,
                    msg=NodePairValidationException.MSG,
                    err_code=NodePairValidationException.ERR_CODE,
                    rslt_type=NodePairValidationException.RSLT_TYPE,
                    ex=TypeError(f"Expected NodePair, got {type(candidate).__name__}. instead")
                )
            )
        # --- Cast the candidate to an Node for additional tests ---#
        node_pair = cast(NodePair, candidate)
        
        # Handle the case that either the head or tail is not certified as safe.
        for member in node_pair.members:
            validation_result = node_validator.validate(candidate=member)
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodePairValidationException(
                        mthd=method,
                        op=NodePairValidationException.OP,
                        msg=NodePairValidationException.MSG,
                        err_code=NodePairValidationException.ERR_CODE,
                        rslt_type=NodePairValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
        # Handle the case that, the head and tail are the same.
        if node_pair.head == node_pair.tail:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodePairValidationException(
                    mthd=method,
                    op=NodePairValidationException.OP,
                    msg=NodePairValidationException.MSG,
                    err_code=NodePairValidationException.ERR_CODE,
                    rslt_type=NodePairValidationException.RSLT_TYPE,
                    ex=HeadCannotBeTailException(
                        msg=NodePairValidationException.MSG,
                        err_code=NodePairValidationException.ERR_CODE,
                    )
                )
            )
        # --- The validation checks were passed, send the success result. ---#
        return ValidationResult.success(node_pair)