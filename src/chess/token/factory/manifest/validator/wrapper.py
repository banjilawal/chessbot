# src/chess/occupant/factory/manifest/exception/exception.py

"""
Module: chess.occupant.factory.manifest.exception.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_BUILD_MANIFEST_VALIDATION_FAILURE EXCEPTION #======================#
    "TokenBuildManifestValidationFailedException",
]

from chess.token import TokenBuildManifestException
from chess.system import ValidationFailedException


# ======================# TOKEN_BUILD_MANIFEST_VALIDATION_FAILURE EXCEPTION #======================#
class TokenBuildManifestValidationFailedException(TokenBuildManifestException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Token. The encapsulated
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   TokenException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_BUILD_MANIFEST_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "TokenBuildManifest validation failed."