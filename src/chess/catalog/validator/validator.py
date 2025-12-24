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
    1.  Simplify Searches based on rank metadata.
    2.  Verifies a candidate is not null and is an actual Persona Enum.
    3.  Only have to write the two verification checks for a Persona once. This gives cleaner code.
    4.  Verifies names and colors used in filtering and branching logic gets arguments in bounds.

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any,) -> ValidationResult[Persona]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check the candidate is a Persona enum
        3.  If both checks pass cast the candidate to a Persona and return in a
            ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[Persona] containing either:
            - On success:   Persona in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullPersonaException
            *   InvalidPersonaException
        """
        method = "PersonaValidator.validate"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullPersonaException(f"{method} {NullPersonaException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Persona):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected Persona, got {type(candidate).__name__} instead.")
                )
            # If no errors are detected cast the candidate to a Persona object then return in
            # a ValidationResult.
            return ValidationResult.success(cast(Persona, candidate))
        
        # Finally, catch any missed exception, wrap an InvalidPieceException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPersonaException(ex=ex, message=f"{method} {InvalidPersonaException.DEFAULT_MESSAGE}")
            )