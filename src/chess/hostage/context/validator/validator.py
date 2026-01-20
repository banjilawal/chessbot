from typing import Any, cast

from chess.square import SquareService
from chess.hostage import (
    CaptivityContextValidationFailedException, CaptivityContextValidationRouteException, CaptivityContext,
    ExcessiveCaptivityContextFlagsException, NullCaptivityContextException, ZeroCaptivityContextFlagsException,
)
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.token import CombatantToken, TokenService


class CaptivityContextValidator(Validator[CaptivityContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1. Verify a candidate is a CaptivityContext that meets the application's safety contract before the client
        is allowed to use the CaptivityContext object.
    2. Provide pluggable factories for validating different options separately.

    # PARENT:
        * Validator

    3 PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    3 INHERITED ATTRIBUTES:
        *   See Validator class for inherited attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[CaptivityContext]:
        """
        # ACTION:
        Verifies candidate is a CaptivityContext in two steps.
            1. Test the candidate is a valid SearchCaptivityContext with a single searcher option switched on.
            2. Test the value passed to CaptivityContext passes its validation contract.
        # PARAMETERS:
            * candidate (Any): Object to verify is a Square.
            * validator (type[SquareValidator]): Enforces safety requirements on row, column, square_name squares.
        # RETURNS:
            * ValidationResult[CaptivityContext] containing either:
                    - On failure: Exception.
                    - On success: CaptivityContext in the payload.
        # RAISES:
            * TypeError
            * NullCaptivityContextException
            * ZeroCaptivityContextFlagsException
            * CaptivityContextValidationFailedException
            * CaptivityContextValidationRouteException
        """
        method = "CaptivityContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CaptivityContextValidationFailedException(
                    message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullCaptivityContextException(f"{method}: {NullCaptivityContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, CaptivityContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CaptivityContextValidationFailedException(
                    message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a CaptivityContext, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast candidate to the CaptivityContext for additional tests. ---#
        context = cast(CaptivityContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CaptivityContextValidationFailedException(
                    message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ZeroCaptivityContextFlagsException(
                        f"{method}: {ZeroCaptivityContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CaptivityContextValidationFailedException(
                    message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ExcessiveCaptivityContextFlagsException(
                        f"{method}: {ExcessiveCaptivityContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None and context.id is not None:
            validation = identity_service.validate_id(context.id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CaptivityContextValidationFailedException(
                        message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_CaptivityContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-victor target.
        if context.victor is not None:
            validation = token_service.validator.validate(context.victor)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CaptivityContextValidationFailedException(
                        message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the victor_CaptivityContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-prisoner target.
        if context.prisoner is not None:
            validation = token_service.validator.validate(context.prisoner)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CaptivityContextValidationFailedException(
                        message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # Handle the case that the class is wrong.
            if not isinstance(context.prisoner, CombatantToken):
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CaptivityContextValidationFailedException(
                        message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=TypeError(
                            f"{method}: Expected a CombatantToken, got {type(candidate).__name__} instead."
                        )
                    )
                )
            # On certification success return the prisoner_CaptivityContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-captured_square target.
        if context.captured_square is not None:
            validation = square_service.validator.validate(context.captured_square)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CaptivityContextValidationFailedException(
                        message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the captured_square_CaptivityContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there was no validation route for the context.
        return ValidationResult.failure(
            CaptivityContextValidationFailedException(
                message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                ex=CaptivityContextValidationRouteException(
                    f"{method}: {CaptivityContextValidationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )