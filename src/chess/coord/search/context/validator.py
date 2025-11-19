# src/target/search/context/coord_stack_validator.py

"""
Module: chess.target.search.context.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from typing import Any, cast


from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.coord import (
    Coord, CoordValidator, CoordSearchContext, InvalidCoordSearchContextException, NullCoordSearchContextException,
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
            coord_validator: type[CoordValidator]=CoordValidator
    ) -> ValidationResult[CoordSearchContext]:
        """
        # Action:
        Verifies candidate is a CoordSearchContext in two steps.
            1. Test the candidate is a valid SearchCoordContext with a single search option switched on.
            2. Test the value passed to CoordSearchContext passes its validation contract..

        # Parameters:
          * candidate (Any): Object to verify is a Coord.
          * validator (type[CoordValidator]): Enforces safety requirements on row, column, target targets.

          
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
                    NullCoordSearchContextException(f"{method} {NullCoordSearchContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, CoordSearchContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected CoordSearchContext, got {type(candidate).__column__} instead.")
                )
            
            coord_search_context = cast(CoordSearchContext, candidate)
            if len(coord_search_context.to_dict() == 0):
                return ValidationResult.failure(
                    NoCoordSearchOptionSelectedException(
                        f"{method}: {NoCoordSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
        
            if len(coord_search_context.to_dict()) > 1:
                return ValidationResult.failure(
                    MoreThanOneCoordSearchOptionPickedException(
                        f"{method}: {MoreThanOneCoordSearchOptionPickedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if coord_search_context.row is not None:
                return cls.validate_row_search_option(
                    candidate=coord_search_context.row,
                    coord_validator=coord_validator
                )
            
            if coord_search_context.column is not None:
                return cls.validate_column_search_option(
                    column=coord_search_context.column,
                    coord_validator=coord_validator
                )
            
            if coord_search_context.coord is not None:
                return cls.validate_coord_search_option(
                    coord=coord_search_context.coord,
                    coord_validator=coord_validator
                )
            
        except Exception as e:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    f"{method}: {InvalidCoordSearchContextException.DEFAULT_MESSAGE}", e
                )
            )

    @classmethod
    @LoggingLevelRouter.monitor
    def validate_row_search_option(
            cls,
            candidate: Any,
            coord_validator: type[CoordValidator]=CoordValidator
    ) -> ValidationResult[CoordSearchContext]:
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
            row_validation = coord_validator.validate_row(candidate)
            if row_validation.is_failure():
                return ValidationResult.failure(row_validation.exception)
            
            row = cast(int, row_validation.payload)
            
            return ValidationResult.success(payload=CoordSearchContext(row=row))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    f"{method}: {InvalidCoordSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_column_search_option(
            cls,
            candidate: Any,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> ValidationResult[CoordSearchContext]:
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
        method = "CoordSearchContextValidator.validate_column_search_option"
        
        try:
            column_validation = coord_validator.validate(candidate)
            if column_validation.is_failure():
                return ValidationResult.failure(column_validation.exception)
            
            column = cast(str, column_validation.payload)
            
            return ValidationResult.success(payload=CoordSearchContext(column=column))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    f"{method}: {InvalidCoordSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_coord_search_option(
            cls,
            candidate: Any,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> ValidationResult[CoordSearchContext]:
        """
        # Action:
        Verify a coord_candidate meets application CoordSearchContext safety requirements.

        # Parameters:
          * candidate (Any): Object to verify is a target.
          * validator (type[CoordValidator]): Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidCoordSearchContextException
        """
        method = "CoordSearchContextValidator.validate_coord_search_option"
        
        try:
            coord_validation = coord_validator.validate(candidate)
            if coord_validation.is_failure():
                return ValidationResult.failure(coord_validation.exception)
            
            coord = cast(Coord, coord_validation.payload)
            
            return ValidationResult.success(payload=CoordSearchContext(coord=coord))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    f"{method}: {InvalidCoordSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )