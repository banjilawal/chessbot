# src/board/search/context/validator.py

"""
Module: chess.board.search.context.validator
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


from typing import Any, cast


from chess.coord import Coord, CoordValidator
from chess.system import Validator, IdValidator, NameValidator, ValidationResult, LoggingLevelRouter
from chess.board import (
    BoardSearchContext, InvalidBoardSearchContextException, NullBoardSearchContextException,
    MoreThanOneBoardSearchOptionPickedException, NoBoardSearchOptionSelectedException
)

class BoardSearchContextValidator(Validator):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1. Verify a candidate is a BoardSearchContext that meets the application's safety contract before the client
        is allowed to use the BoardSearchContext object.
    2. Provide pluggable factories for validating different options separately.
    
    # PROVIDES:
      ValidationResult[BoardSearchContext] containing either:
            - On success: Board in payload.
            - On failure: Exception.

    # ATTRIBUTES:
    No attributes.
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            id_validator: type[IdValidator]=IdValidator,
            name_validator: type[NameValidator]=NameValidator,
            coord_validator: type[CoordValidator]=CoordValidator
    ) -> ValidationResult[BoardSearchContext]:
        """
        # Action:
        Verifies candidate is a BoardSearchContext in two steps.
            1. Test the candidate is a valid SearchBoardContext with a single search option switched on.
            2. Test the value passed to BoardSearchContext passes its validation contract..

        # Parameters:
          * candidate (Any): Object to verify is a Board.
          * id_validator (type[IdValidator]): Enforces safety requirements on id-search targets.
          * name_validator (type[NameValidator]): Enforces safety requirements on name-search targets.
          * coord_validator (type[CoordValidator]): Enforces safety requirements on name-search targets.
          
        # Returns:
          ValidationResult[BoardSearchContext] containing either:
                - On success: BoardSearchContext in payload.
                - On failure: Exception.

        # Raises:
            * TypeError
            * InvalidBoardSearchContextException
            * NullBoardSearchContextException
            * NoBoardSearchOptionSelectedException
            * MoreThanOneBoardSearchOptionPickedException
        """
        method = "BoardSearchContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullBoardSearchContextException(f"{method} {NullBoardSearchContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, BoardSearchContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected BoardSearchContext, got {type(candidate).__name__} instead.")
                )
            
            board_search_context = cast(BoardSearchContext, candidate)
            if len(board_search_context.to_dict() == 0):
                return ValidationResult.failure(
                    NoBoardSearchOptionSelectedException(
                        f"{method}: {NoBoardSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
        
            if len(board_search_context.to_dict()) > 1:
                return ValidationResult.failure(
                    MoreThanOneBoardSearchOptionPickedException(
                        f"{method}: {MoreThanOneBoardSearchOptionPickedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if board_search_context.id is not None:
                return cls.validate_id_search_option(
                    candidate=board_search_context.id,
                    id_validator=id_validator
                )
            
            if board_search_context.name is not None:
                return cls.validate_name_search_option(
                    name=board_search_context.name,
                    name_validator=name_validator
                )
            
            if board_search_context.coord is not None:
                return cls.validate_coord_search_option(
                    coord=board_search_context.coord,
                    coord_validator=coord_validator
                )
            
        except Exception as e:
            return ValidationResult.failure(
                InvalidBoardSearchContextException(
                    f"{method}: {InvalidBoardSearchContextException.DEFAULT_MESSAGE}", e
                )
            )

    @classmethod
    @LoggingLevelRouter.monitor
    def validate_id_search_option(
            cls,
            candidate: Any,
            id_validator: type[IdValidator]=IdValidator
    ) -> ValidationResult[BoardSearchContext]:
        """
        # Action:
        Verify an id_candidate meets application BoardSearchContext safety requirements.

        # Parameters:
          * candidate (Any): Object to verify is an id.
          * id_validator (type[IdValidator]): Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[BoardSearchContext] containing either:
                - On success: BoardSearchContext in payload.
                - On failure: Exception.

        # Raises:
            * InvalidBoardSearchContextException
        """
        method = "BoardSearchContextValidator.validate_id_search_option"
        
        try:
            id_validation = id_validator.validate(candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            return ValidationResult.success(payload=BoardSearchContext(id=id_validation.payload))
        except Exception as e:
            return ValidationResult.failure(
                InvalidBoardSearchContextException(
                    f"{method}: {InvalidBoardSearchContextException.DEFAULT_MESSAGE}", e
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_name_search_option(
            cls,
            candidate: Any,
            name_validator: type[NameValidator]=NameValidator
    ) -> ValidationResult[BoardSearchContext]:
        """
        # Action:
        Verify a name_candidate meets application BoardSearchContext safety requirements.

        # Parameters:
          * candidate (Any): Object to verify is a name.
          * name_validator (type[NameValidator]): Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[BoardSearchContext] containing either:
                - On success: BoardSearchContext in payload.
                - On failure: Exception.

        # Raises:
            * InvalidBoardSearchContextException
        """
        method = "BoardSearchContextValidator.validate_name_search_option"
        
        try:
            name_validation = name_validator.validate(candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            return ValidationResult.success(payload=BoardSearchContext(name=name_validation.payload))
        except Exception as e:
            return ValidationResult.failure(
                InvalidBoardSearchContextException(
                    f"{method}: {InvalidBoardSearchContextException.DEFAULT_MESSAGE}", e
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_coord_search_option(
            cls,
            candidate: Any,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> ValidationResult[BoardSearchContext]:
        """
        # Action:
        Verify a coord_candidate meets application BoardSearchContext safety requirements.

        # Parameters:
          * candidate (Any): Object to verify is a coord.
          * name_validator (type[CoordValidator]): Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[BoardSearchContext] containing either:
                - On success: BoardSearchContext in payload.
                - On failure: Exception.

        # Raises:
            * InvalidBoardSearchContextException
        """
        method = "BoardSearchContextValidator.validate_coord_search_option"
        
        try:
            coord_validation = coord_validator.validate(candidate)
            if coord_validation.is_failure():
                return ValidationResult.failure(coord_validation.exception)
            
            return ValidationResult.success(payload=BoardSearchContext(coord=coord_validation.payload))
        except Exception as e:
            return ValidationResult.failure(
                InvalidBoardSearchContextException(
                    f"{method}: {InvalidBoardSearchContextException.DEFAULT_MESSAGE}", e
                )
            )