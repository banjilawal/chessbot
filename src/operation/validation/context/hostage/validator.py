# src/operation/validation/context/hostage/operation.py

"""
Module: operation.validation.context.hostage.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class HostageContextValidator(Validator[HostageContext]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1. Verify a rank is a HostageContext that meets the application's safety contract before the client
        is allowed to use the HostageContext object.
    2. Provide pluggable factories for validating different options separately.

    Super Class:
        * Validator

    3 PROVIDES:
    None


    3 INHERITED ATTRIBUTES:
        *   See Validator class for inherited attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            hostage_service: HostageService = HostageService(),
            square_service: SquareService = SquareService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[HostageContext]:
        """
        # ACTION:
        Verifies rank is a HostageContext in two steps.
            1. Test the rank is a valid SearchHostageContext with a single searcher option switched on.
            2. Test the value passed to HostageContext passes its validation contract.
        # PARAMETERS:
            * rank (Any): Object to verify is a Square.
            * validation (type[SquareValidator]): Enforces safety requirements on row, column, square_name squares.
        # RETURNS:
            * ValidationResult[HostageContext] containing either:
                    - On failure: Exception.
                    - On success: HostageContext in the payload.
        Raises:
            * TypeError
            * NullHostageContextException
            * ZeroHostageContextFlagsException
            * HostageContextValidationException
            * HostageContextValidationRouteException
        """
        method = "HostageContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                HostageContextValidationException(
                    msg=f"{method}: {HostageContextValidationException.MSG}",
                    ex=NullHostageContextException(f"{method}: {NullHostageContextException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, HostageContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                HostageContextValidationException(
                    msg=f"{method}: {HostageContextValidationException.MSG}",
                    ex=TypeError(f"{method}: Expected a HostageContext, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast rank to the HostageContext for additional tests. ---#
        context = cast(HostageContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                HostageContextValidationException(
                    msg=f"{method}: {HostageContextValidationException.MSG}",
                    ex=ZeroHostageContextFlagsException(
                        f"{method}: {ZeroHostageContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                HostageContextValidationException(
                    msg=f"{method}: {HostageContextValidationException.MSG}",
                    ex=ArenaHostageContextFlagsException(
                        f"{method}: {ArenaHostageContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation = identity_service.validate_id(context.id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    HostageContextValidationException(
                        msg=f"{method}: {HostageContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_HostageContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-victor target.
        if context.victor is not None:
            validation = hostage_service.validator.validate(context.victor)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    HostageContextValidationException(
                        msg=f"{method}: {HostageContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the victor_HostageContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-prisoner target.
        if context.prisoner is not None:
            validation = hostage_service.validator.verify_hostage_is_combatant(candidate=context.prisoner)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    HostageContextValidationException(
                        msg=f"{method}: {HostageContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the prisoner_HostageContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-captured_square target.
        if context.captured_square is not None:
            validation = square_service.validator.validate(context.captured_square)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    HostageContextValidationException(
                        msg=f"{method}: {HostageContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the captured_square_HostageContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there was no validation route for the context.
        return ValidationResult.failure(
            HostageContextValidationException(
                msg=f"{method}: {HostageContextValidationException.MSG}",
                ex=HostageContextValidationRouteException(
                    f"{method}: {HostageContextValidationRouteException.MSG}"
                )
            )
        )