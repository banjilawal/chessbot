# src/chess/formation/builder/exception.py

"""
Module: chess.formation.builder.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.formation import OrderContextException

__all__ = [
    # ======================# FORMATION_CONTEXT_BUILD_FAILED EXCEPTION #======================#
    "FormationContextBuildFailedException",
]


# ======================# FORMATION_CONTEXT_BUILD_FAILED EXCEPTION #======================#
class FormationContextBuildFailedException(FormationContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the FormationContext build creates an exception. Failed check exceptions are encapsulated
        in an FormationContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The FormationContextBuildFailedException provides a trace for debugging and application recovery.tion recovery.

    # PARENT:
        *   FormationContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "FormationContext build failed."