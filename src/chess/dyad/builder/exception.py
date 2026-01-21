# src/chess/dyad/builder/exception.py

"""
Module: chess.dyad.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.dyad import SchemaAgentPairException


__all__ = [
    # ======================# SCHEMA_AGENT_PAIR_BUILD_FAILURE EXCEPTION #======================#
    "SchemaAgentPairBuildFailedException",
]


# ======================# SCHEMA_AGENT_PAIR_BUILD_FAILURE EXCEPTION #======================#
class SchemaAgentPairBuildFailedException(SchemaAgentPairException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the SchemaAgentPair build creates an exception. Failed check exceptions are encapsulated
        in an SchemaAgentPairBuildFailedException which is sent to the caller in a BuildResult.
    2.  The SchemaAgentPairBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   SchemaAgentPairException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_AGENT_PAIR_BUILD_FAILE_ERROR"
    DEFAULT_MESSAGE = "SchemaAgentPair build failed."