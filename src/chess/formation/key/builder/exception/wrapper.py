# src/chess/formation/builder/exception.py

"""
Module: chess.formation.builder.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ======================# FORMATION_KEY_BUILD_FAILED EXCEPTION #======================#
    "FormationKeyBuildFailedException",
]

from chess.formation.key import FormationKeyException


# ======================# FORMATION_KEY_BUILD_FAILED EXCEPTION #======================#
class FormationKeyBuildFailedException(FormationKeyException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the FormationKey build creates an exception. Failed check exceptions are encapsulated
        in a FormationKeyBuildFailedException which is sent to the caller in a BuildResult.
    2.  The FormationKeyBuildFailedException provides a trace for debugging and application recovery.
        # RESPONSIBILITIES:

    # PARENT:
        *   BuildFailedException
        *   FormationKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_KEY_BUILD_FAILED"