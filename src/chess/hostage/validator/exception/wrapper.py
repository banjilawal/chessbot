# src/chess/persona/validator/exception/wrapper.py

"""
Module: chess.persona.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# PERSONA_VALIDATION_FAILURE #======================#
    "PersonaValidationException",
]


# ======================# PERSONA_VALIDATION_FAILURE #======================#
class PersonaValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in PersonaValidator.validate that, prevented ValidationResult.success()
        from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Persona validation failed."

# src/chess/hostage/validator/exception/wrapper.py

"""
Module: chess.hostage.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-19
"""

from chess.hostage import HostageManifestException
from chess.system import ValidationException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_VALIDATION_FAILURE #======================#
    "HostageManifestValidationException",
]


# ======================# HOSTAGE_MANIFEST_VALIDATION_FAILURE #======================#
class HostageManifestValidationException(HostageManifestException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a HostageManifest. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   HostageManifestException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "HostageManifest validation failed."