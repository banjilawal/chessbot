# src/chess/system/err/wrapper.py

"""
Module: chess.system.err.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NOT_IMPLEMENTED EXCEPTION #======================#
    "WrapperException",
]

from chess.system import ChessException


# ======================# WRAPPER EXCEPTION #======================#
class WrapperException(ChessException):
    """
    # ROLE: Wrapper, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulates the debug exception that was raised when a specific condition prevented an operation successfully
        completing. Middle layer of the 3-part exception chain.
        
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
    
    # DEFAULT MESSAGE CONVENTION:
    1.  Sentence whose first word is the class name followed by the operation name. The sentence ends with failed.
    2.  The Syntax is: [Class] operation failed.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "WRAPPER_EXCEPTION"
    DEFAULT_MESSAGE = "WrapperException"