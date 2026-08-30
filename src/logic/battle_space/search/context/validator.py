# src/logic/battle_space/searcher/exception.py

"""
Module: logic.battle_space.searcher.coord_stack_validator
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""

from typing import Any, cast

from system import LoggingLevelRouter, ValidationResult, Validator
from logic.battle_space.search.search import ProjectionContext


class ProjectionContextValidator(Validator[ProjectionContext]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[ProjectionContext]:
        """"""
        method = "ProjectionContextValidator.execute"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullProjectionContextException(
                        f"{method}: {NullProjectionContextException.MSG}"
                    )
                )
            
            if not isinstance(candidate, ProjectionContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected ProjectionContext, got {type(candidate).__name__}"
                    )
                )
            
            search_context = cast(ProjectionContext, candidate)
            
            return ValidationResult.success(search_context)
        
        except Exception as e:
            return ValidationResult.failure(e)