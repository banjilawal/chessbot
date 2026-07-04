# src/validation/blueprint/hostage/validator.py

"""
Module: validation.blueprint.hostage.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class HostageBlueprintValidator(BlueprintValidator[Hostage]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1. Verify a rank is a HostageBlueprint that meets the application's safety contract before the client
        is allowed to use the HostageBlueprint object.
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
    ) -> ValidationResult[Hostage]:
        """
        # ACTION:
        Verifies rank is a HostageBlueprint in two steps.
            1. Test the rank is a valid SearchHostageBlueprint with a single searcher option switched on.
            2. Test the value passed to HostageBlueprint passes its validation contract.
        # PARAMETERS:
            * rank (Any): Object to verify is a Square.
            * validation (type[SquareValidator]): Enforces safety requirements on row, column, square_name squares.
        # RETURNS:
            * ValidationResult[Hostage] containing either:
                    - On failure: Exception.
                    - On success: HostageBlueprint in the payload.
        Raises:
            * TypeError
            * NullHostageBlueprintException
            * ZeroHostageBlueprintFlagsException
            * HostageBlueprintValidationException
            * HostageBlueprintValidationRouteException
        """
        method = "HostageBlueprintValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HostageBlueprintValidationException(
                    msg=f"{method}: {HostageBlueprintValidationException.MSG}",
                    ex=NullHostageBlueprintException(f"{method}: {NullHostageBlueprintException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, HostageBlueprint):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HostageBlueprintValidationException(
                    msg=f"{method}: {HostageBlueprintValidationException.MSG}",
                    ex=TypeError(f"{method}: Expected a HostageBlueprint, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast rank to the HostageBlueprint for additional tests. ---#
        blueprint = cast(HostageBlueprint, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(blueprint.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HostageBlueprintValidationException(
                    msg=f"{method}: {HostageBlueprintValidationException.MSG}",
                    ex=ZeroHostageBlueprintFlagsException(
                        f"{method}: {ZeroHostageBlueprintFlagsException.MSG}"
                    )
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HostageBlueprintValidationException(
                    msg=f"{method}: {HostageBlueprintValidationException.MSG}",
                    ex=ArenaHostageBlueprintFlagsException(
                        f"{method}: {ArenaHostageBlueprintFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if blueprint.id is not None:
            validation = identity_service.validate_id(blueprint.id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    HostageBlueprintValidationException(
                        msg=f"{method}: {HostageBlueprintValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_HostageBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-victor target.
        if blueprint.victor is not None:
            validation = hostage_service.validate.build(blueprint.victor)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    HostageBlueprintValidationException(
                        msg=f"{method}: {HostageBlueprintValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the victor_HostageBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-prisoner target.
        if blueprint.prisoner is not None:
            validation = hostage_service.validate.verify_hostage_is_combatant(candidate=blueprint.prisoner)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    HostageBlueprintValidationException(
                        msg=f"{method}: {HostageBlueprintValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the prisoner_HostageBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-captured_square target.
        if blueprint.captured_square is not None:
            validation = square_service.validate.build(blueprint.captured_square)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    HostageBlueprintValidationException(
                        msg=f"{method}: {HostageBlueprintValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the captured_square_HostageBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Return the exception chain if there was no validation route for the blueprint.
        return ValidationResult.failure(
            HostageBlueprintValidationException(
                msg=f"{method}: {HostageBlueprintValidationException.MSG}",
                ex=HostageBlueprintValidationRouteException(
                    f"{method}: {HostageBlueprintValidationRouteException.MSG}"
                )
            )
        )