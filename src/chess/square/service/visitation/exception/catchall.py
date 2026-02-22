# src/chess/square/service/visitation/exception/catchall.py

"""
Module: chess.square.service.visitation.exception.catchall
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""


from chess.system import CatchallException, ServiceException

__all__ = [
    # ======================# TOKEN_VISIT_HANDLER EXCEPTION #======================#
    "TokenVisitHandlerException",
]


# ======================# TOKEN_VISIT_HANDLER EXCEPTION #======================#
class TokenVisitHandlerException(CatchallException):
    """"
    # ROLE: Catchall, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Outermost layer of the 3-part exception chain that is created when a TokenVisitHandler
        operation aborts.

    # PARENT:
        *   CatchallException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_VISIT_HANDLER_ERROR"
    DEFAULT_MESSAGE = "TokenVisitHandler raised an exception."