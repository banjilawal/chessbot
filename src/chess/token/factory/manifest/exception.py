# src/chess/token/factory/manifest/exception.py

"""
Module: chess.token.factory.manifest.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


__all__ = [
    # ======================# TOKEN_MANIFEST EXCEPTION #======================#
    "TokenManifestException",
]

from chess.system import ChessException


# ======================# TOKEN_MANIFEST EXCEPTION #======================#
class TokenManifestException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for TokenManifest errors.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_MANIFEST_ERROR"
    DEFAULT_MESSAGE = "TokenManifest raised an exception."