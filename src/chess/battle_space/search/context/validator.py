# src/chess/battle_space/search/context/factory.py

"""
Module: chess.battle_space.search.context.coord_stack_validator
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""

from typing import Any, cast

from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.battle_space.search.search import ProjectionSearchContext


class ProjectionSearchContextValidator(Validator[ProjectionSearchContext]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[ProjectionSearchContext]:
        """"""
        method = "ProjectionSearchContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullProjectionSearchContextException(
                        f"{method}: {NullProjectionSearchContextException.DEFAULT_MESSAGE}"
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