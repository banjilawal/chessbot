# src/chess/piece/map/builder/exception.py

"""
Module: chess.piece.map.builder.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""


from chess.system import BuildFailedException
from chess.piece import PieceContextException

__all__ = [
    #======================# PIECECONTEXT BUILD EXCEPTION #======================#
    "PieceContextBuildFailedException",
]


#======================# PIECECONTEXT BUILD EXCEPTION #======================#
class PieceContextBuildFailedException(PieceContextException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by PieceContextBuilder 
    prevents successful PieceContext creation.
    """
    ERROR_CODE = "PIECE_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "PieceContext build failed."