# src/chess/coord/validator/validator.py

"""
Module: chess.coord.validator
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from typing import Any, cast

from chess.coord.context.validator.exception.debug.null import NullCoordContextException
from chess.coord.context.validator.exception.wrapper import CoordContextValidationFailedException
from chess.system import NumberValidator, Validator, ValidationResult, LoggingLevelRouter
from chess.coord import CoordValidator, CoordContext, ZeroCoordContextFlagsException


class CoordContextValidator(Validator[CoordContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1. Verify a candidate is a CoordContext that meets the application's safety contract before the client
        is allowed to use the CoordContext object.
    2. Provide pluggable factories for validating different options separately.
    
    # PROVIDES:
      ValidationResult[CoordContext] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator(),
    ) -> ValidationResult[CoordContext]:
        """
        # ACTION:
        Verifies candidate is a CoordContext in two steps.
            1. Test the candidate is a valid SearchCoordContext with a single searcher option switched on.
            2. Test the value passed to CoordContext passes its validation contract..
        # PARAMETERS:
          * candidate (Any): Object to verify is a Coord.
          * validator (type[CoordValidator]): Enforces safety requirements on row, column, square_name coords.
        # RETURNS:
          ValidationResult[CoordContext] containing either:
                - On success: CoordContext in the payload.
                - On failure: Exception.
        # RAISES:
            * TypeError
            * NullCoordContextException
            * NullCoordSearchContextException
            * NoCoordSearchOptionSelectedException
            * MoreThanOneCoordSearchOptionPickedException
        """
        method = "CoordSearchContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationFailedException(
                    message=f"{method}: {CoordContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullCoordContextException(f"{method}: {NullCoordContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that they type is wrong.
        if not isinstance(candidate, CoordContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationFailedException(
                    message=f"{method}: {CoordContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a CoordContext, got {type(candidate).__name__} instead.")
                )
            )
       
        context = cast(CoordContext, candidate)
        switch_count = len(context.to_dict())
        if switch_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationFailedException(
                    message=f"{method}: {CoordContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ZeroCoordContextFlagsException(f"{method}: {ZeroCoordContextFlagsException.DEFAULT_MESSAGE}")
                )
            )
        
        if switch_count == 2:
            row_validation = number_validator.validate(context.row)
            if row_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CoordContextValidationFailedException(
                        message=f"{method}: {CoordContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=row_validation.exception
                    )
                )
            column_validation = number_validator.validate(context.column)
            if column_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CoordContextValidationFailedException(
                        message=f"{method}: {CoordContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=column_validation.exception
                    )
                )
            return ValidationResult.success(payload=context)
        
        if context.row is not None and context.column is not None:
            row_validation = number_validator.validate(context.row)
            if row_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CoordContextValidationFailedException(
                        message=f"{method}: {CoordContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=row_validation.exception
                    )
                )
            return ValidationResult.success(payload=context)
            
        column_validation = number_validator.validate(context.column)
        if column_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationFailedException(
                    message=f"{method}: {CoordContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=column_validation.exception
                )
            )
        return ValidationResult.success(payload=context)