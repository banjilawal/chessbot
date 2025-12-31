# src/chess/persona/validator/validator.py

"""
Module: chess.persona.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.persona import Persona, InvalidPersonaException, NullPersonaException


class PersonaValidator(Validator[Persona]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a candidate is not null and the correct type before its used as a Persona.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, ) -> ValidationResult[Persona]:
        """
        # ACTION:.
            1.  If the candidate passes existence and type checks cast into a Persona instance and return
                in the ValidationResult. Else return an exception in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
        # RETURNS:
            *   ValidationResult[Persona] containing either:
                    - On failure: Exception.
                    - On success: Persona in the payload.
        # RAISES:
            *   TypeError
            *   NullPersonaException
            *   InvalidPersonaException
        """
        method = "PersonaValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidPersonaException(
                    message=f"{method}: {InvalidPersonaException.ERROR_CODE}",
                    ex=NullPersonaException(f"{method} {NullPersonaException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Persona):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidPersonaException(
                    message=f"{method}: {InvalidPersonaException.ERROR_CODE}",
                    ex=TypeError(f"{method} Expected Persona, got {type(candidate).__name__} instead.")
                )
            )
        # On certification success return the schema instance in a ValidationResult.
        return ValidationResult.success(cast(Persona, candidate))
