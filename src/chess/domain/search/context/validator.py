# src/chess/domain/searcher/context/factory.py

"""
Module: chess.domain.searcher.context.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast

from chess.coord import CoordValidator
from chess.rank import RankBoundsChecker
from chess.system import Validator, IdValidator, NameValidator, ValidationResult, LoggingLevelRouter
from chess.domain import (
    NullResidentSearchContextException, ResidentFilter, NoResidentSearchParamException,
    ExcessiveResidentSearchParamsException
)


class ResidentFilterValidator(Validator[ResidentFilter]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security., Data Integrity
  
    # RESPONSIBILITIES:
    1. Process and validate parameters for creating `GraphSearchContext` instances.
    2. Create new `GraphSearchContext` objects if parameters meet specifications.
    2. Report errors and return `BuildResult` with error details.
  
    # PROVIDES:
    `BuildResult`: Return type containing the built `GraphSearchContext` or error information.
  
    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[ResidentFilter]:
        """"""
        method = "ResidentFilterValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullResidentSearchContextException(f"{method} {NullResidentSearchContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, ResidentFilter):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected ResidentSearchContext, got {type(candidate).__name__} instead.")
                )
            
            search_context = cast(ResidentFilter, candidate)
            
            if len(search_context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoResidentSearchParamException(f"{method} {NoResidentSearchParamException.DEFAULT_MESSAGE}")
                )
            
            if len(search_context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveResidentSearchParamsException(
                        f"{method} {ExcessiveResidentSearchParamsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if search_context.resident_id is not None:
                id_validation = IdValidator.validate(search_context.resident_id)
                if id_validation.is_failure():
                    return ValidationResult.failure(id_validation.exception)
            
            if search_context.resident_name is not None:
                name_validation = NameValidator.validate(search_context.resident_name)
                if name_validation.is_failure():
                    return ValidationResult.failure(name_validation.exception)
            
            if search_context.team_id is not None:
                team_id_validation = IdValidator.validate(search_context.team_id)
                if team_id_validation.is_failure():
                    return ValidationResult.failure(team_id_validation.exception)
            
            if search_context.resident_team is not None:
                team_name_validation = NameValidator.validate(search_context.resident_team)
                if team_name_validation.is_failure():
                    return ValidationResult.failure(team_name_validation.exception)
            
            if search_context.resident_rank is not None:
                rank_name_bounds_check = RankBoundsChecker.name_bounds_check(search_context.resident_rank)
                if rank_name_bounds_check.is_failure():
                    return ValidationResult.failure(rank_name_bounds_check.exception)
            
            if search_context.resident_ransom is not None:
                ransom_bounds_check = RankBoundsChecker.name_bounds_check(search_context.resident_ransom)
                if ransom_bounds_check.is_failure():
                    return ValidationResult.failure(ransom_bounds_check.exception)
            
            if search_context.resident_coord is not None:
                coord_validation = CoordValidator.validate(search_context.resident_coord)
                if coord_validation.is_failure():
                    return ValidationResult.failure(coord_validation.exception)
            
            return ValidationResult.sucess(search_context)
        
        except Exception as e:
            return ValidationResult.failure(e)
