# src/validator/persona/validator.py

"""
Module: validator.persona.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class PersonaValidator(Validator[Persona]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a rank is not null and the correct type before its used as a Span.Square.Ray.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, ) -> ValidationResult[Persona]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if, the rank is either
                    *   nulI
                    *   is not a Persona instance.
            2.  Otherwise, cast the candidate into a Persona then, send in the success result.

        Args:
            candidate: Any

        Returns:
            ValidationResult[Persona]

        Raises:
            TypeError
            NullPersonaException
            PersonaValidatorException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PersonaValidatorException(
                    cls_mthd=method,
                    op=PersonaValidatorException.OP,
                    msg=PersonaValidatorException.MSG,
                    err_code=PersonaValidatorException.ERR_CODE,
                    mthd_rslt_type=PersonaValidatorException.MTHD_RSLT,
                    ex=NullPersonaException(
                        msg=NullPersonaException.MSG,
                        err_code=NullPersonaException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Persona):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PersonaValidatorException(
                    cls_mthd=method,
                    op=PersonaValidatorException.OP,
                    msg=PersonaValidatorException.MSG,
                    err_code=PersonaValidatorException.ERR_CODE,
                    mthd_rslt_type=PersonaValidatorException.MTHD_RSLT,
                    ex=TypeError(f"{method} Expected Persona, got {type(candidate).__name__} instead.")
                )
            )
        # --- Passed safet checks. Send the success result. ---#
        return ValidationResult.success(cast(Persona, candidate))
