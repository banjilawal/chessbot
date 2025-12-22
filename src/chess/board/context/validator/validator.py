# src/board/searcher/coord_stack_validator.py

"""
Module: chess.board.searcher.coord_stack_validator
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from typing import Any, cast

from chess.system import Validator, IdValidator, NameValidator, ValidationResult, LoggingLevelRouter



class BoardContextValidator(Validator[BoardContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Verify a candidate is a TeamSearchContext that meets the application's safety contract before the client
        is allowed to use the TeamSearchContext object.
    2.  Provide pluggable factories for validating different options separately.
    
    # PROVIDES:
    ValidationResult[TeamSearchContext] containing either:
        - On success:   Board in the payload.
        - On failure:   Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            id_validator: type[IdValidator] = IdValidator,
            name_validator: type[NameValidator] = NameValidator,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> ValidationResult[BoardContext]:
        """
        # Action:
        Verifies candidate is a TeamSearchContext in two steps.
            1.  Test the candidate is a valid SearchBoardContext with a single searcher option switched on.
            2.  Test the value passed to TeamSearchContext passes its validation contract..

        # Parameters:
          * candidate (Any):                            Object to verify is a Board.
          * id_validator (type[IdValidator]):           Enforces safety requirements on id-searcher targets.
          * name_validator (type[NameValidator]):       Enforces safety requirements on designation-searcher targets.
          * validator (type[CoordValidator]):     Enforces safety requirements on designation-searcher targets.
          
        # Returns:
          ValidationResult[TeamSearchContext] containing either:
                - On success:   TeamSearchContext in the payload.
                - On failure:   Exception.

        # Raises:
            *   TypeError
            *   InvalidBoardSearchContextException
            *   NullBoardContextException
            *   NoBoardSearchOptionSelectedException
            *   MoreThanOneBoardSearchOptionPickedException
        """
        method = "BoardContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullBoardSearchContextException(f"{method} {NullBoardSearchContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, BoardContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected TeamSearchContext, got {type(candidate).__name__} instead.")
                )
            
            board_search_context = cast(BoardContext, candidate)
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
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBoardSearchContextException(
                    f"{method}: {InvalidBoardSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_id_search_option(
            cls,
            candidate: Any,
            id_validator: type[IdValidator] = IdValidator
    ) -> ValidationResult[BoardContext]:
        """
        # Action:
        Verify an id_candidate meets application TeamSearchContext safety requirements.

        # Parameters:
            *   candidate (Any):                    Object to verify is an id.
            *   id_validator (type[IdValidator]):   Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[TeamSearchContext] containing either:
                - On success:   TeamSearchContext in the payload.
                - On failure:   Exception.

        # Raises:
            *   InvalidBoardSearchContextException
        """
        method = "BoardContextValidator.validate_id_search_option"
        
        try:
            id_validation = id_validator.validate(candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            return ValidationResult.success(payload=BoardContext(id=id_validation.payload))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBoardSearchContextException(
                    f"{method}: {InvalidBoardSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_name_search_option(
            cls,
            candidate: Any,
            name_validator: type[NameValidator] = NameValidator
    ) -> ValidationResult[BoardContext]:
        """
        # Action:
        Verify a name_candidate meets application TeamSearchContext safety requirements.

        # Parameters:
          * candidate (Any): Object to verify is a designation.
          * name_validator (type[NameValidator]): Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[TeamSearchContext] containing either:
                - On success: TeamSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * InvalidBoardSearchContextException
        """
        method = "BoardContextValidator.validate_name_search_option"
        
        try:
            name_validation = name_validator.validate(candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            return ValidationResult.success(payload=BoardContext(name=name_validation.payload))
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBoardSearchContextException(
                    f"{method}: {InvalidBoardSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_coord_search_option(
            cls,
            candidate: Any,
            coord_validator: type[CoordValidator] = CoordValidator
    ) -> ValidationResult[BoardContext]:
        """
        # Action:
        Verify a coord_candidate meets application TeamSearchContext safety requirements.

        # Parameters:
            *   candidate (Any):                        Object to verify is a target.
            *   name_validator (type[CoordValidator]):  Checks if candidate complies with safety contract.

        # Returns:
          ValidationResult[TeamSearchContext] containing either:
                - On success:   TeamSearchContext in the payload.
                - On failure:    Exception.

        # Raises:
            *   InvalidBoardSearchContextException
        """
        method = "BoardContextValidator.validate_coord_search_option"
        
        try:
            coord_validation = coord_validator.validate(candidate)
            if coord_validation.is_failure():
                return ValidationResult.failure(coord_validation.exception)
            
            return ValidationResult.success(payload=BoardContext(coord=coord_validation.payload))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBoardSearchContextException(
                    f"{method}: {InvalidBoardSearchContextException.DEFAULT_MESSAGE}",
                    ex
                )
            )
