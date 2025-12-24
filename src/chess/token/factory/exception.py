# src/chess/piece/factory/exception

"""
Module: chess.piece.factory.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.piece import PieceException
from chess.system import BuilderException, BuildFailedException, NullException

__all__ = [
    # ======================# PIECE_BUILD_FAILED EXCEPTION #======================#
    "PieceBuildFailedException",
]


# ======================# PIECE_BUILD_FAILED EXCEPTION #======================#
class PieceBuildFailedException(PieceException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Token build creates an exception. Failed check exceptions are encapsulated
        in an PieceBuildFailedException which is sent to the caller in a BuildResult.
    2.  The PieceBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   PieceException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Token build failed."