# src/chess/token/factory/manifest/exception.py

"""
Module: chess.token.factory.manifest.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


__all__ = [
    # ======================# TOKEN_BUILD_MANIFEST EXCEPTION #======================#
    "TokenBuildManifestException",
]

from chess.system import ChessException


# ======================# TOKEN_BUILD_MANIFEST EXCEPTION #======================#
class TokenBuildManifestException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for TokenBuildManifest errors.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_BUILD_MANIFEST_ERROR"
    DEFAULT_MESSAGE = "TokenBuildManifest raised an exception."