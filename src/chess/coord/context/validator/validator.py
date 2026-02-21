# src/chess/coord/context/validator/validator.py

"""
Module: chess.coord.context.validator.validator
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from typing import Any, cast

from chess.system import NumberValidator, Validator, ValidationResult, LoggingLevelRouter
from chess.coord import (
    CoordContextValidationException, CoordContextValidationRouteException, CoordContext,
    NullCoordContextException, ZeroCoordContextFlagsException
)


class CoordContextValidator(Validator[CoordContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1. Verify a candidate is a CoordContext that meets the application's safety contract before the client
        is allowed to use the CoordContext object.
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
          *    ValidationResult[CoordContext] containing either:
                    - On failure: Exception.
                    - On success: CoordContext in the payload.
        # RAISES:
            * TypeError
            * NullCoordContextException
            * ZeroCoordContextFlagsException
            * CoordContextValidationException
            * CoordContextValidationRouteException
        """
        method = "CoordSearchContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationException(
                    message=f"{method}: {CoordContextValidationException.DEFAULT_MESSAGE}",
                    ex=NullCoordContextException(f"{method}: {NullCoordContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that they type is wrong.
        if not isinstance(candidate, CoordContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationException(
                    message=f"{method}: {CoordContextValidationException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a CoordContext, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast candidate to the CoordContext for additional tests. ---#
        context = cast(CoordContext, candidate)
        
        # Get how many context flags are set.
        switch_count = len(context.to_dict())
        
        # Handle the case that no context flags are set.
        if switch_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationException(
                    message=f"{method}: {CoordContextValidationException.DEFAULT_MESSAGE}",
                    ex=ZeroCoordContextFlagsException(f"{method}: {ZeroCoordContextFlagsException.DEFAULT_MESSAGE}")
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
                    CoordContextValidationException(
                        message=f"{method}: {CoordContextValidationException.DEFAULT_MESSAGE}",
                        ex=row_validation.exception
                    )
                )
            # Handle the case that column of search-by-column-and-row target fails its integrity checks.
            column_validation = number_validator.validate(context.column)
            if column_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CoordContextValidationException(
                        message=f"{method}: {CoordContextValidationException.DEFAULT_MESSAGE}",
                        ex=column_validation.exception
                    )
                )
            # On certification success return the row-and-column_CoordContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-row target.
        if context.row is not None and context.column is not None:
            row_validation = number_validator.validate(context.row)
            if row_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CoordContextValidationException(
                        message=f"{method}: {CoordContextValidationException.DEFAULT_MESSAGE}",
                        ex=row_validation.exception
                    )
                )
            # On certification success return the row_CoordContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-column target.
        if context.column is not None and context.column is not None:
            column_validation = number_validator.validate(context.column)
            if column_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CoordContextValidationException(
                        message=f"{method}: {CoordContextValidationException.DEFAULT_MESSAGE}",
                        ex=column_validation.exception
                    )
                )
            # On certification success return the column_CoordContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there was no validation route for the context.
        return ValidationResult.failure(
            CoordContextValidationException(
                message=f"{method}: {CoordContextValidationException.DEFAULT_MESSAGE}",
                ex=CoordContextValidationRouteException(f"{method}: {CoordContextValidationRouteException.DEFAULT_MESSAGE}")
            )
        )
        



