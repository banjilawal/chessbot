# src/chess/system/service/root/exception.py

"""
Module: chess.system.service.root.exception
Author: Banji Lawal
Created: 2025-11-18
"""

from chess.system import SuperClassException

__all__ = [
    # ======================# SERVICE EXCEPTION #======================#
    "ServiceException",
]


# ======================# SERVICE EXCEPTION #======================#
class ServiceException(SuperClassException):
    """
    # ROLE: Catchall, Exception Messaging
    
    # RESPONSIBILITIES:
    1. Outermost layer of the 3-part exception chain that is created when a Service operation's crashes.

    # PARENT:
        *   SuperClassException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SERVICE_ERROR"
    MSG = "Service raised an exception."