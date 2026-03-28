# src/logic/battle_space/searcher/exception.py

"""
Module: logic.battle_space.searcher.coord_stack_validator
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""

from typing import Any, cast

from logic.system import LoggingLevelRouter, ValidationResult, ValidationTransaction
from logic.battle_space.search.search import ProjectionSearchContext


class ProjectionSearchContextValidationTransaction(ValidationTransaction[ProjectionSearchContext]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, candidate: Any) -> ValidationResult[ProjectionSearchContext]:
        """"""
        method = "ProjectionSearchContextValidationTransaction.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullProjectionSearchContextException(
                        f"{method}: {NullProjectionSearchContextException.MSG}"
                    )
                )
            
            if not isinstance(candidate, ProjectionSearchContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected ProjectionSearchContext, got {type(candidate).__name__}"
                    )
                )
            
            search_context = cast(ProjectionSearchContext, candidate)
            
            return ValidationResult.success(search_context)
        
        except Exception as e:
            return ValidationResult.failure(e)