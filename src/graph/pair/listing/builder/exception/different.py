from __future__ import annotations
from typing import Any, Optional

___all__ = [
    # ======================# TREE_DOES_NOT_OWN_RAY_EXCEPTION #======================#
    "TreeDoesNotOwnRayException",
]

from system import NoRelationException


# ======================# TREE_DOES_NOT_OWN_RAY_EXCEPTION #======================#
class TreeDoesNotOwnRayException(NoRelationException):
    """
    Role: Exception Messaging, Exception Chain Layer 2
    # TASK: Capture Error Variable State

    Responsibilities:
    1.  Produce the:
            *   variable,
            *   it's Value,
            *   event which fired the variable into its error state.
        which occurred in the Anchor method identified in layer-0 of the exception chain.
        
    2.  Indicate that, a failing result was returned because the NodeTree does not own the
        SquareRay.

    Super Class:
        *   NoRelationException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See NoRelationException class for inherited attributes.

    Attributes:
        var: Optional[str]
        val: Optional[str]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See NoRelationException class for inherited methods.
    """
    ERR_CODE = "TREE_DOES_NOT_OWN_RAY_EXCEPTION"
    MSG = "The ray belongs to a different NodeTree"
    
    def method(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[str]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)