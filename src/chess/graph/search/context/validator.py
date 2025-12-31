# src/chess/domain/searcher/factory.py

"""
Module: chess.domain.searcher.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast

from chess.coord import CoordValidator
from chess.domain import NullVisitorSearchContextException, VisitorSearchContext
from chess.rank import RankBoundsChecker, RankBoundsException
from chess.system import Validator, IdValidator, NameValidator, ValidationResult, LoggingLevelRouter
from chess.neighbor import ExcessiveVisitationSearchParamsException, ZeroVisitationSearchParamsException


class VisitorSearchContextValidator(Validator[VisitorSearchContext]):
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
    def validate(cls, candidate: Any) -> ValidationResult[VisitorSearchContext]:
        """"""
        method = "VisitorSearchContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullVisitorSearchContextException(f"{method} {NullVisitorSearchContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, VisitorSearchContext):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected VisitorSearchContext, got {type(candidate).__name__} instead.")
                )
            
            search_context = cast(VisitorSearchContext, candidate)
            
            if len(search_context.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroVisitationSearchParamsException(
                        f"{method} {ZeroVisitationSearchParamsException.DEFAULT_MESSAGE}"
                        )
                )
            
            if len(search_context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveVisitationSearchParamsException(
                        f"{method} {ExcessiveVisitationSearchParamsException.DEFAULT_MESSAGE}"
                        )
                )
            
            if search_context.visitor_id is not None:
                id_validation = IdValidator.validate(search_context.visitor_id)
                if id_validation.is_failure():
                    return ValidationResult.failure(id_validation.exception)
            
            if search_context.visitor_name is not None:
                name_validation = NameValidator.validate(search_context.visitor_name)
                if name_validation.is_failure():
                    return ValidationResult.failure(name_validation.exception)
            
            if search_context.team_id is not None:
                team_id_validation = IdValidator.validate(search_context.team_id)
                if team_id_validation.is_failure():
                    return ValidationResult.failure(team_id_validation.exception)
            
            if search_context.visitor_team is not None:
                team_name_validation = NameValidator.validate(search_context.visitor_team)
                if team_name_validation.is_failure():
                    return ValidationResult.failure(team_name_validation.exception)
            
            if search_context.visitor_rank is not None:
                rank_name_bounds_check = RankBoundsChecker.name_bounds_check(search_context.visitor_rank)
                if rank_name_bounds_check.is_failure():
                    return ValidationResult.failure(rank_name_bounds_check.exception)
            
            if search_context.visitor_ransom is not None:
                ransom_bounds_check = RankBoundsChecker.name_bounds_check(search_context.visitor_ransom)
                if ransom_bounds_check.is_failure():
                    return ValidationResult.failure(ransom_bounds_check.exception)
            
            if search_context.point is not None:
                coord_validation = CoordValidator.validate(search_context.point)
                if coord_validation.is_failure():
                    return ValidationResult.failure(coord_validation.exception)
            
            return ValidationResult.sucess(search_context)
        
        except Exception as e:
            return ValidationResult.failure(e)
