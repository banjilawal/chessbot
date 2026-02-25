from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# DEBUG EXCEPTION #======================#
    "DebugException",
]



from chess.system import ChessException


# ======================# DEBUG EXCEPTION #======================#
class DebugException(ChessException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Identifies the code block in a method where the error occurred.
    2.  Describe what condition or state prevented an operation from completing successfully.
    3.  Lowest part of the 3-layer exception chain. Should not contain other exceptions.
    
    # ERROR CODE CONVENTION:
    1.  All caps, snake case description of the error with _ERROR as the suffix.
    
    # DEFAULT MSG CONVENTION:
    1.  Wrapper msg followed by a colon. Description of the error after the colon.
    2.  The Syntax is: [Class] operation failed: [Description]

    # PARENT:
        *   Exception

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   mthd (Optional[str])
        *   var (Optional[str])
        *   val Optional[None])

    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   var (Optional[str])
        *   val Optional[None])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ChessException class for inherited methods.
    """
    ERROR_CODE = "DEBUG_ERROR"
    MSG: str = "An error occurred."
    MTHD: ""
    VAR: ""
    VAL: None
    
    _mthd: Optional[str]
    _var: Optional[str]
    _val: Optional[None]
    
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[None] = None,
            ex: Optional[Exception] = None,
    ):
        msg = msg or self.MSG
        err_code = err_code or self.ERROR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        self._mthd = mthd
        self._var = var
        self._val = val
    
    @property
    def mthd(self) -> Optional[str]:
        return self._mthd
    
    @property
    def var(self) -> Optional[str]:
        return self._var
    
    @property
    def val(self) -> Optional[None]:
        return self._val
