# src/logic/pair/tree/validation/validation.py

"""
Module: logic.pair.tree.validation
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast

from graph.pair import NodeTree, NodeTreeNullException, NodeTreeValidationException
from system import LoggingLevelRouter, ValidationResult, Validator


class NodeTreeValidator(Validator[NodeTree]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a rank is not null and the correct type before its used as a Pair.Tree.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[NodeTree]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if, the rank is either
                    *   nulI
                    *   is not a NodeTree instance.
            2.  Otherwise, cast the candidate into a NodeTree then, send in the success result.
            
        Args:
            candidate: Any
            
        Returns:
            ValidationResult[NodeTree]
            
        Raises:
            TypeError
            NodeTreeNullException
            NodeTreeValidationException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeTreeValidationException(
                    cls_mthd=method,
                    op=NodeTreeValidationException.OP,
                    msg=NodeTreeValidationException.MSG,
                    err_code=NodeTreeValidationException.ERR_CODE,
                    mthd_rslt_type=NodeTreeValidationException.MTHD_RSLT,
                    ex=NodeTreeNullException(
                        var="rank",
                        val="None",
                        msg=NodeTreeNullException.MSG,
                        err_code=NodeTreeNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, NodeTree):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeTreeValidationException(
                    cls_mthd=method,
                    op=NodeTreeValidationException.OP,
                    msg=NodeTreeValidationException.MSG,
                    err_code=NodeTreeValidationException.ERR_CODE,
                    mthd_rslt_type=NodeTreeValidationException.MTHD_RSLT,
                    ex=TypeError(
                        f"{method} Expected NodeTree, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Safety checks are passed. Send the success result. ---#
        return ValidationResult.success(cast(NodeTree, candidate))
