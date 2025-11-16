# src/coord/search/context/validator.py

"""
Module: chess.coord.search.context.validator
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


from typing import Any, cast


from chess.coord import Coord, CoordValidator
from chess.system import Validator, Coordvalidator, Coordvalidator, ValidationResult, LoggingLevelRouter
from chess.coord import (
    CoordSearchContext, InvalidCoordSearchContextException, NullCoordSearchContextException,
    MoreThanOneCoordSearchOptionPickedException, NoCoordSearchOptionSelectedException
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
          * coord_validator (type[Coordvalidator]): Enforces safety requirements on id-search targets.
          * coord_validator (type[Coordvalidator]): Enforces safety requirements on name-search targets.
          * coord_validator (type[CoordValidator]): Enforces safety requirements on name-search targets.
          
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
                    name=coord_search_context.column,
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
            coord_validator: type[Coordvalidator]=Coordvalidator
    ) -> ValidationResult[CoordSearchContext]:
        """
        # Action:
        Verify an id_candidate meets application CoordSearchContext safety requirements.

        # Parameters:
          * candidate (Any): Object to verify is an id.
          * coord_validator (type[Coordvalidator]): Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidCoordSearchContextException
        """
        method = "CoordSearchContextValidator.validate_id_search_option"
        
        try:
            coord_validator = coord_validator.validate(candidate)
            if coord_validator.is_failure():
                return ValidationResult.failure(coord_validator.exception)
            
            return ValidationResult.success(payload=CoordSearchContext(id=coord_validator.payload))
        except Exception as e:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    f"{method}: {InvalidCoordSearchContextException.DEFAULT_MESSAGE}", e
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_column_search_option(
            cls,
            candidate: Any,
            coord_validator: type[Coordvalidator] = Coordvalidator
    ) -> ValidationResult[CoordSearchContext]:
        """
        # Action:
        Verify a column_candidate meets application CoordSearchContext safety requirements.

        # Parameters:
          * candidate (Any): Object to verify is a name.
          * coord_validator (type[CoordValidator]): Checks if candidate complies with safety contract.

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
            
            return ValidationResult.success(payload=CoordSearchContext(name=column_validation.payload))
        except Exception as e:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    f"{method}: {InvalidCoordSearchContextException.DEFAULT_MESSAGE}", e
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
          * candidate (Any): Object to verify is a coord.
          * coord_validator (type[CoordValidator]): Checks if candidate complies with safety contract.

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
            
            return ValidationResult.success(payload=CoordSearchContext(coord=coord_validation.payload))
        except Exception as e:
            return ValidationResult.failure(
                InvalidCoordSearchContextException(
                    f"{method}: {InvalidCoordSearchContextException.DEFAULT_MESSAGE}", e
                )
            )