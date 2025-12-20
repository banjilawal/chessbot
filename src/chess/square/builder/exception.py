# src/chess/square/builder/exception.py

"""
Module: chess.square.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from  chess.square import SquareException
from chess.system import BuildFailedException


__all__ = [
    #======================# SQUARE BUILD EXCEPTION #======================#
    "SquareBuildFailedException",
]


#======================# SQUARE BUILD EXCEPTION #======================#
class SquareBuildFailedException(SquareException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by SquareBuilder 
    prevents successful Square creation.
    """
    ERROR_CODE = "SQUARE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Square build failed."

