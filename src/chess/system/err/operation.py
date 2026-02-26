# src/chess/system/err/operation.py

"""
Module: chess.system.err.operation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# OPERATION_FAILURE #======================#
    "OperationException",
]

from typing import Optional

from chess.system import WrapperException


# ======================# OPERATION_FAILURE #======================#
class OperationException(WrapperException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Identifies the method in a class where the error occurred.
    2.  Encapsulates the DebugException which identifies the method's code block that raised the error.
    3.  Middle part of the 3-layer exception chain. Should only contain a DebugException.

    # NAMING CONVENTION:
    1.  Prefix is the Class name with the Result name. The operation name should match the Result subclass.
    2.  Operation outcome. This will always be Failed.
    3.  Suffix is Exception.
    4.  The Syntax is: [ClassName][ResultClassName]FailedException

    # ERROR CODE CONVENTION:
    1.  All caps, snake case. Prefix is the class name followed by the operation name. The operation name should
        match the type of result.
    3.  Suffix is Exception.
    2.  The Syntax is: [Class]_[OPERATION]_FAILURE

    # DEFAULT MSG CONVENTION:
    1.  Sentence whose first word is the class name followed by the operation name. The sentence ends with failed.
    2.  The Syntax is: [Class] operation failed.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

   # LOCAL ATTRIBUTES:
        *   op_name (Optional[str])

    INHERITED ATTRIBUTES:
        *   See WrapperException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        # LOCAL ATTRIBUTES:
            *   op_name (Optional[str])
            *   rslt (Optional[str])
            
        # INHERITED ATTRIBUTES:
            See WrapperException class for inherited attributes.

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See WrapperException class for inherited methods.
    """
    ERR_CODE = "OPERATION_FAILURE"
    MSG = "Operation failed."
    MTHD: None
    OP_NAME = None
    RSLT: None
    
    _op_name: Optional[str]
    _rslt: Optional[str]
    
    def __init__(
            self,
            rslt: Optional[str] = None,
            op_name: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        rslt = rslt or self.RSLT
        op_name = op_name or self.OP_NAME
        mthd = mthd or self.MTHD
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
    
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        self._rslt = rslt
        self._mthd = mthd
        self._op_name = op_name or self.OP_NAME
    
    @property
    def rslt(self) -> Optional[str]:
        return self._rslt
    
    @property
    def mthd(self) -> Optional[str]:
        return self._mthd
    
    @property
    def op_name(self) -> Optional[str]:
        return self._op_name
    
    def __str__(self):
        return f"{super().__str__()}, op_name:{self._op_name}, rslt:{self._rslt}"


    

