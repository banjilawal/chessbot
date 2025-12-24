# src/chess/formation/builder/exception.py

"""
Module: chess.formation.builder.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ======================# FORMATION_SUPER_KEY_BUILD_FAILED EXCEPTION #======================#
    "FormationSuperKeyBuildFailedException",
]

from chess.formation.key import FormationSuperKeyException


# ======================# FORMATION_SUPER_KEY_BUILD_FAILED EXCEPTION #======================#
class FormationSuperKeyBuildFailedException(FormationSuperKeyException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the FormationSuperKey build creates an exception. Failed check exceptions are encapsulated
        in a FormationSuperKeyBuildFailedException which is sent to the caller in a BuildResult.
    2.  The FormationSuperKeyBuildFailedException provides a trace for debugging and application recovery.
        # RESPONSIBILITIES:

    # PARENT:
        *   BuildFailedException
        *   FormationSuperKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_SUPER_KEY_BUILD_FAILED"