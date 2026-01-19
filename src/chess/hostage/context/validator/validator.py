from typing import Any, cast

from chess.hostage import (
    CaptivityContextValidationFailedException, ExcessiveCaptivityContextFlagsException, NullCaptivityContextException,
    ZeroCaptivityContextFlagsException
)
from chess.hostage.context.context import CaptivityContext
from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.token import TokenService


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
    ) -> ValidationResult[CaptivityContext]:
        """
        # ACTION:
        Verifies candidate is a CaptivityContext in two steps.
            1. Test the candidate is a valid SearchCaptivityContext with a single searcher option switched on.
            2. Test the value passed to CaptivityContext passes its validation contract..
        # PARAMETERS:
          * candidate (Any): Object to verify is a Coord.
          * validator (type[CoordValidator]): Enforces safety requirements on row, column, square_name coords.
        # RETURNS:
          *    ValidationResult[CaptivityContext] containing either:
                    - On failure: Exception.
                    - On success: CaptivityContext in the payload.
        # RAISES:
            * TypeError
            * NullCaptivityContextException
            * ZeroCaptivityContextFlagsException
            * CaptivityContextValidationFailedException
            * CaptivityContextValidationRouteException
        """
        method = "CoordSearchContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CaptivityContextValidationFailedException(
                    message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullCaptivityContextException(f"{method}: {NullCaptivityContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that they type is wrong.
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
        
        # Get how many context flags are set.
        switch_count = len(context.to_dict())
        
        # Handle the case that no context flags are set.
        if switch_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CaptivityContextValidationFailedException(
                    message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ZeroCaptivityContextFlagsException(
                        f"{method}: {ZeroCaptivityContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that more than one context flags are set.
        if switch_count > 1:
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
        
        # Certification for the search-by-column-and-row target.
        if switch_count == 2:
            # Handle the case that row of search-by-column-and-row target fails its integrity checks.
            row_validation = number_validator.validate(context.row)
            if row_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CaptivityContextValidationFailedException(
                        message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=row_validation.exception
                    )
                )
            # Handle the case that column of search-by-column-and-row target fails its integrity checks.
            column_validation = number_validator.validate(context.column)
            if column_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CaptivityContextValidationFailedException(
                        message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=column_validation.exception
                    )
                )
            # On certification success return the row-and-column_CaptivityContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-row target.
        if context.row is not None and context.column is not None:
            row_validation = number_validator.validate(context.row)
            if row_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CaptivityContextValidationFailedException(
                        message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=row_validation.exception
                    )
                )
            # On certification success return the row_CaptivityContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-column target.
        if context.column is not None and context.column is not None:
            column_validation = number_validator.validate(context.column)
            if column_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CaptivityContextValidationFailedException(
                        message=f"{method}: {CaptivityContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=column_validation.exception
                    )
                )
            # On certification success return the column_CaptivityContext in the ValidationResult.
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