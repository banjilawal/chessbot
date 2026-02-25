# src/chess/system/err/super_class.py

"""
Module: chess.system.err.super_class
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

__all__ = [
    # ======================# SUPER_CLASS EXCEPTION #======================#
    "SuperClassException",
]

from chess.system import ChessException


# ======================# SUPER_CLASS EXCEPTION #======================#
class SuperClassException(ChessException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Exception for an Entity or Class.
    2.  Parent of Debug exceptions that are raised by an object being manipulated.

    # NAMING CONVENTION:
    1.  Class name followed by the Exception suffix
    2.  The Syntax is: [Class]Exception

    # ERROR CODE CONVENTION:
    1.  Class name followed by the ERROR suffix.
    2.  The Syntax is: [Class]_ERROR

    # DEFAULT MSG CONVENTION:
    1.  Class name followed by "raised an exception."
    2.  The Syntax is: [Class] raised an exception

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "SUPER_CLASS_ERROR"
    MSG = "SuperClassException."