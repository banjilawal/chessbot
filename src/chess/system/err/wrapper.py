# src/chess/system/err/wrapper.py

"""
Module: chess.system.err.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# WRAPPER EXCEPTION #======================#
    "WrapperException",
]

from chess.system import ChessException


# ======================# WRAPPER EXCEPTION #======================#
class WrapperException(ChessException):
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
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "WRAPPER_EXCEPTION"
    MSG = "WrapperException"