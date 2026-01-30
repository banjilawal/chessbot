# src/chess/tokenBuildManifest/validator/exception/debug/__init__.py

"""
Module: chess.tokenBuildManifest.validator.exception.debug.__init__
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_TOKEN_BUILD_MANIFEST EXCEPTION #======================#
    "NullTokenManifestException",
]

from chess.system import NullException
from chess.token import TokenManifestException


# ======================# NULL_TOKEN_BUILD_MANIFEST EXCEPTION #======================#
class NullTokenManifestException(TokenManifestException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that TokenManifest validation failed because the candidate was null.

    # PARENT:
        *   NullException
        *   TokenManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TOKEN_BUILD_MANIFEST_ERROR"
    DEFAULT_MESSAGE = "TokenManifest validation failed: The candidate was null."