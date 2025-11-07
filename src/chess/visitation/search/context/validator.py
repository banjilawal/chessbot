# src/chess/visitation/search/context/validator.py

"""
Module: chess.visitation.search.context.validator
Author: Banji Lawal
Created: 2025-11-05
version: 1.0.0
"""

from typing import cast, TypeVar

from chess.coord import CoordValidator
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, RankSpec, Rook
from chess.system import IdValidator, LoggingLevelRouter, NameValidator, Validator, ValidationResult
from chess.piece import (
    DomainSearchContext, InvalidDomainSearchContextException, NullDomainSearchContextException,
    TooManyDomainSearchParamsException, ZeroDomainSearchParamsException, DomainInvalidRankNameParamException
)


class DomainSearchContextValidator(Validator[DomainSearchContext]):
    """
    # ROLE: Validation, Data Integrity
  
    # RESPONSIBILITIES:
    1. Process and validate parameters for creating `DomainSearchContext` instances.
    2. Create new `DomainSearchContext` objects if parameters meet specifications.
    2. Report errors and return `BuildResult` with error details.
  
    # PROVIDES:
    `BuildResult`: Return type containing the built `DomainSearchContext` or error information.
  
    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: T) -> ValidationResult[DomainSearchContext]:
        """"""
        method = "DomainSearchContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullDomainSearchContextException(f"{method} {NullDomainSearchContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, DomainSearchContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method} Expected domainSearchContext DomainSearchContext, got {type(candidate).__name__}"
                        )
                )
            
            search_context = cast(DomainSearchContext, candidate)
            
            if len(search_context.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroDomainSearchParamsException(f"{method} {ZeroDomainSearchParamsException.DEFAULT_MESSAGE}")
                )
            
            if len(search_context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyDomainSearchParamsException(
                        f"{method} {InvalidDomainSearchContextException.DEFAULT_MESSAGE}"
                        )
                )
            
            if search_context.piece_id is not None:
                piece_id_validation = IdValidator.validate(search_context.piece_id)
                if piece_id_validation.is_failure():
                    return ValidationResult.failure(piece_id_validation.exception)
            
            if search_context.name is not None:
                piece_name_validation = NameValidator.validate(search_context.name)
                if piece_name_validation.is_failure():
                    return ValidationResult.failure(piece_name_validation.exception)
            
            if search_context.team_id is not None:
                team_id_validation = IdValidator.validate(search_context.team_id)
                if team_id_validation.is_failure():
                    return ValidationResult.failure(team_id_validation.exception)
            
            if search_context.team_name is not None:
                team_name_validation = NameValidator.validate(search_context.team_name)
                if team_name_validation.is_failure():
                    return ValidationResult.failure(team_name_validation.exception)
            
            if search_context.rank_name is not None and search_context.rank_name.upper() not in RankSpec.__members__:
                return ValidationResult.failure(
                    DomainInvalidRankNameParamException(
                        f"{method}: {DomainInvalidRankNameParamException.DEFAULT_MESSAGE}"
                        )
                )
            
            if search_context.ransom not in range[Queen.ransom]:
                return ValidationResult.failure(
                    DomainInvalidRankNameParamException(
                        f"{method}: {DomainInvalidRankNameParamException.DEFAULT_MESSAGE}"
                        )
                )
            
            if search_context.position is not None:
                position_validation = CoordValidator.validate(search_context.position)
                if position_validation.is_failure():
                    return ValidationResult.failure(position_validation.exception)
            
            return ValidationResult.success(search_context)
        
        except Exception as e:
            return ValidationResult.failure(e)
