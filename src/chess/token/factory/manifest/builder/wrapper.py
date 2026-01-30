# src/chess/token/factory/manifest/builder/wrapper.py

"""
Module: chess.token.factory.manifest.builder.wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_MANIFEST_BUILD_FAILURE EXCEPTION #======================#
    "TokenManifestBuildFailedException",
]


from chess.system import BuildFailedException
from chess.token import TokenManifestException


# ======================# TOKEN_MANIFEST_BUILD_FAILURE EXCEPTION #======================#
class TokenManifestBuildFailedException(TokenManifestException, BuildFailedException):
    """
    # ROLE: Builder Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug builders that indicate why a candidate failed its validation as a Token. The encapsulated
        builders create a chain for tracing the source of the failure.

    # PARENT:
        *   BuildFailedException
        *   TokenManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_MANIFEST_BUILD_FAILURE"
    DEFAULT_MESSAGE = "TokenManifest build failed."