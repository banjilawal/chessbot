# src/chess/system/collection/operation/search/exception/wrapper.py

"""
Module: chess.system.collection.operation.search.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""
from typing import Optional

from chess.system import CollectionOperationException

__all__ = [
    # ======================# SEARCH_FAILURE #======================#
    "SearchException",
]


# ======================# SEARCH_FAILURE #======================#
class SearchException(CollectionOperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes the cause the search failed.

    # PARENT:
        *   CollectionOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SEARCH_FAILURE"
    MSG = "Search failed."
    MTHD = "search"
    OP_NAME = "search"
    RSLT = "SearchResult"
    
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
        
        super().__init__(msg=msg, err_code=err_code, ex=ex, rslt=rslt, mthd=mthd, op_name=op_name)