# src/chess/coord/context/validator/validator.py

"""
Module: chess.coord.context.validator.validator
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from typing import Any, cast


from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.coord import (
    CoordValidator, CoordSearchContext, InvalidCoordSearchContextException, NullCoordSearchContextException,
    MoreThanOneCoordSearchOptionPickedException, NoCoordSearchOptionSelectedException,
)

class CoordSearchContextValidator(Validator):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1. Verify a candidate is a CoordSearchContext that meets the application's safety contract before the client
        is allowed to use the CoordSearchContext object.
    2. Provide pluggable factories for validating different options separately.
    
    # PROVIDES:
      ValidationResult[CoordSearchContext] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    No attributes.
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            validator: CoordValidator=CoordValidator()
    ) -> ValidationResult[CoordSearchContext]:
        """
        # Action:
        Verifies candidate is a CoordSearchContext in two steps.
            1. Test the candidate is a valid SearchCoordContext with a single search option switched on.
            2. Test the value passed to CoordSearchContext passes its validation contract..

        # Parameters:
          * candidate (Any): Object to verify is a Coord.
          * validator (type[CoordValidator]): Enforces safety requirements on row, column, square coords.

          
        # Returns:
          ValidationResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * TypeError
            * InvalidCoordSearchContextException
            * NullCoordSearchContextException
            * NoCoordSearchOptionSelectedException
            * MoreThanOneCoordSearchOptionPickedException
        """
        method = "CoordSearchContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullCoordSearchContextException(
                        f"{method} "
                        f"{NullCoordSearchContextException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, CoordSearchContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected a CoordSearchContext, "
                        f"got {type(candidate).__column__} instead."
                    )
                )
            
           
            context = cast(CoordSearchContext, candidate)
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoCoordSearchOptionSelectedException(
                        f"{method}: "
                        f"{NoCoordSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if context.row is not None and context.column is not None:
                validation = cls.validate_both(
                    row_candidate=context.row,
                    column_candidate=context.column,
                    validator=validator
                )
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                else:
                    ValidationResult.success(payload=validation.payload)
            
            if context.row is not None:
                validator = cls.validate_row_context(
                    candidate=context.row,
                    validator=validator
                )
                if validator.is_failure():
                    return ValidationResult.failure(validator.exception)
                else:
                    return ValidationResult.success(payload=validator.payload)
            
            if context.column is not None:
                validation = cls.validate_column_context(
                    column=context.column,
                    coord_validator=validator
                )
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                else:
                    return ValidationResult.success(payload=validation.payload)
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{InvalidCoordSearchContextException.DEFAULT_MESSAGE}"
                    )
                )
            )

    @classmethod
    @LoggingLevelRouter.monitor
    def validate_row_context(
            cls,
            candidate: Any,
            validator: CoordValidator=CoordValidator()
    ) -> ValidationResult[int]:
        """
        # Action:
        Verify a row_candidate meets application CoordSearchContext safety requirements.

        # Parameters:
          * candidate (Any): Object to verify is a row.
          * validator (type[CoordValidator]): Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidCoordSearchContextException
        """
        method = "CoordSearchContextValidator.validate_id_search_option"
        
        try:
            validation = validator.validate_row(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            return ValidationResult.success(payload=validation.payload)
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{InvalidCoordSearchContextException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_column_context(
            cls,
            candidate: Any,
            validator: CoordValidator = CoordValidator()
    ) -> ValidationResult[int]:
        """
        # Action:
        Verify a column_candidate meets application CoordSearchContext safety requirements.

        # Parameters:
          * candidate (Any): Object to verify is a column.
          * validator (type[CoordValidator]): Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidCoordSearchContextException
        """
        method = "CoordSearchContextValidator.validate_column_context"
        
        try:
            validation = validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            return ValidationResult.success(validation.payload)
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{InvalidCoordSearchContextException.DEFAULT_MESSAGE}"
                    )
                )
            )

    @classmethod
    def validate_both(
            cls,
            row_candidate: Any,
            column_candidate: Any
    ) -> ValidationResult[(int, int)]:
        method = "CoordSearchContextValidator.validate_both"
        try:
            row_validation = cls.validate_row_context(row_candidate)
            if row_validation.is_failure():
                return ValidationResult.failure(row_validation.exception)
            
            column_validation = cls.validate_column_context(column_candidate)
            if column_validation.is_failure():
                return ValidationResult.failure(column_validation.exception)
            
            return ValidationResult.success(
                payload=(
                    row_validation.payload,
                    column_validation.payload
                )
            )
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{InvalidCoordSearchContextException.DEFAULT_MESSAGE}"
                    )
                )
            )