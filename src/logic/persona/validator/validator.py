# src/logic/persona/validator/validator.py

"""
Module: logic.persona.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from logic.system import LoggingLevelRouter, ValidationResult, Validator
from logic.persona import Persona, PersonaValidationException, NullPersonaException


class PersonaValidator(Validator[Persona]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a candidate is not null and the correct type before its used as a Span.Square.Ray.
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
        Action:
            1.  Send an exception chain in the ValidationResult if, the candidate is either
                    *   nulI
                    *   is not a Persona instance.
            2.  Otherwise, cast the candidate to a Persona then, send in the success result.

        Args:
            candidate: Any

        Returns:
            ValidationResult[Persona]

        Raises:
            TypeError
            NullPersonaException
            PersonaValidationException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PersonaValidationException(
                    mthd=method,
                    op=PersonaValidationException.OP,
                    msg=PersonaValidationException.MSG,
                    err_code=PersonaValidationException.ERR_CODE,
                    rslt_type=PersonaValidationException.RSLT_TYPE,
                    ex=NullPersonaException(
                        msg=NullPersonaException.MSG,
                        err_code=NullPersonaException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Persona):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PersonaValidationException(
                    mthd=method,
                    op=PersonaValidationException.OP,
                    msg=PersonaValidationException.MSG,
                    err_code=PersonaValidationException.ERR_CODE,
                    rslt_type=PersonaValidationException.RSLT_TYPE,
                    ex=TypeError(f"{method} Expected Persona, got {type(candidate).__name__} instead.")
                )
            )
        # --- Passed safet checks. Send the success result. ---#
        return ValidationResult.success(cast(Persona, candidate))
