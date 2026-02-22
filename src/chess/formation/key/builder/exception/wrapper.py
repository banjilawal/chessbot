# src/chess/formation/builder/exception.py

"""
Module: chess.formation.builder.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ======================# FORMATION_KEY_BUILD_FAILURE #======================#
    "FormationKeyBuildException",
]

from chess.formation.key import FormationKeyException


# ======================# FORMATION_KEY_BUILD_FAILURE #======================#
class FormationKeyBuildException(FormationKeyException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the FormationKey build creates an exception. Failed check exceptions are encapsulated
        in a FormationKeyBuildException which is sent to the caller in a BuildResult.
    2.  The FormationKeyBuildException provides a trace for debugging and application recovery.
        # RESPONSIBILITIES:

    # PARENT:
        *   BuildException
        *   FormationKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_KEY_BUILD_FAILED"