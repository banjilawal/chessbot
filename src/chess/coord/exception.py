# src/chess/square/collision.py

"""
Module: chess.square.exception
Author: Banji Lawal
Created: 2025-09-27
version: 1.0.0
"""

from chess.system import BuildFailedException, NullException, ChessException, ValidationException

__all__ = [
    "CoordException",
    
    # ====================== NULL COORD EXCEPTIONS #======================#
    "NullCoordException",
    
    # ====================== COORD BUILD EXCEPTIONS #======================#
    "CoordBuildFailedException",
]


class CoordException(ChessException):
    """
    Super class of exceptions raised by Scalar objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_ERROR"
    DEFAULT_MESSAGE = f"Invalid Coord state threw an err"



    
    
# ====================== COORD BUILD EXCEPTIONS #======================#
class CoordBuildFailedException(CoordException, BuildFailedException):
    """Catchall Exception for CoordBuilder when it stops because of an error."""
    ERROR_CODE = "COORD_BUILD_FAILED"
    DEFAULT_MESSAGE = "Coord build failed."
