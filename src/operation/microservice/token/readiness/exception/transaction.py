
from __future__ import annotations
from typing import Optional


__all__ = [
    # ======================# TOKEN_READINESS_ANALYSIS_FAILURE #======================#
    "TokenReadinessAnalysisException",
]

from system import RelationAnalysisException

# ======================# TOKEN_READINESS_ANALYSIS_FAILURE #======================#
class TokenReadinessAnalysisException(RelationAnalysisException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate that an error prevented a token_readiness_analysis from completing.
        2.  Trace the method calls.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt: Optional[ResultCategory]

    Provides:

    Super:
        AnalysisException
    """
    ERR_CODE = "TOKEN_READINESS_ANALYSIS_FAILURE"
    MSG = "An error prevented the readiness analysis from completing."

    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            mthd_rslt: Optional[ResultCategory] = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt: Optional[ResultCategory]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt=mthd_rslt,
        )


__all__ = [
    # ======================# TOKEN_READINESS_ANALYSIS_FAILURE #======================#
    "TokenReadinessAnalysisException",
]

from system import RelationAnalysisException



# ======================# TOKEN_READINESS_ANALYSIS_FAILURE #======================#
class TokenReadinessAnalysisException(RelationAnalysisException):
    """
    Role:Exception Work, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test exception before the
        occupant's state has been evaluated.

    Super Class:
        *   WorkException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_READINESS_ANALYSIS_FAILURE"
    MSG = "RosterRelationTest failed."