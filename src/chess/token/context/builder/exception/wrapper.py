# src/chess/piece/builder/exception.py

"""
Module: chess.piece.builder.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""


from chess.system import BuildFailedException
from chess.piece import PieceContextException

__all__ = [
    # ======================# PIECE_CONTEXT_BUILD_FAILED EXCEPTION #======================#
    "PieceContextBuildFailedException",
]


# ======================# PIECE_CONTEXT_BUILD_FAILED EXCEPTION #======================#
class PieceContextBuildFailedException(PieceContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the PieceContext build creates an exception. Failed check exceptions are encapsulated
        in an PieceContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The PieceContextBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   TokenContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "PieceContext build failed."