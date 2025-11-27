# src/chess/piece/context/builder/exception.py

"""
Module: chess.piece.context.builder.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""


from chess.system import BuildFailedException
from chess.piece import PieceContextException

__all__ = [
    # ======================# PIECE_CONTEXT BUILD EXCEPTIONS #======================#
    "PieceContextBuildFailedException",
]


# ======================# PIECE_CONTEXT BUILD EXCEPTIONS #======================#
class PieceContextBuildFailedException(PieceContextException, BuildFailedException):
    """Catchall Exception for PieceContextBuilder when it stops because of an error."""
    ERROR_CODE = "PIECE_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "PieceContext build failed."