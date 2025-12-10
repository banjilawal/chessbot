# src/chess/team/schema/finder/finder.py

"""
Module: chess.team.schema.finder.finder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from typing import List

from chess.system.find.finder import D
from chess.team import TeamColorBoundsException, TeamNameBoundsException, TeamSchema
from chess.system import Context, Finder, GameColor, GameColorValidator, IdentityService, SearchResult, Validator


class TeamSchemaFinder(Finder[TeamSchema]):

        
    @classmethod
    def find(
            cls,
            data_set: List[TeamSchema],
            context: TeamSchemaContext,
            context_validator: TeamSchemaContextValidator = TeamschemaValidator()
    ) -> SearchResult[List[TeamSchema]]:
        try:
            context_validation = context_validator.validate(candidate=context)
            if context_validation.is_failure:
                return SearchResult.failure(context_validation.exception)
            
            if context.color is not None:
                return cls._find_by_color(context.color)
            if context.name is not None:
                return cls._find_by_name(context.name)
            
        except Exception as ex:
            return SearchResult.failure(
                TeamSchemaFinderException(ex=ex, message=f"{method}: {TeamSchemaFinderException.DEFAULT_MESSAGE}")
            )
            
    
    def _find_by_color(
            self,
            color: GameColor,
            color_validator: GameColorValidator = GameColorValidator()
    ) -> SearchResult[List[TeamSchema]]:
        method = "TeamSchemaFinder._find_by_color"
        try:
            validation = color_validator.validate(color)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            if color in self._schema.color:
                return SearchResult.success(List[self._schema.color])
            return SearchResult.failure(
                TeamColorBoundsException(f"{method}: {TeamColorBoundsException.DEFAULT_MESSAGE}")
            )
        except Exception as ex:
            return SearchResult.failure(
                TeamSchemaFinderException(ex=ex, message=f"{method}: {TeamSchemaFinderException.DEFAULT_MESSAGE}")
            )
    
    def _find_by_name(
            self,
            name: str,
            identity_service: IdentityService = IdentityService(),
    ) -> SearchResult[List[TeamSchema]]:
        method = "TeamSchemaFinder._find_by_color"
        try:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            if name in self._schema.name:
                return SearchResult.success(List[self._schema.color])
            return SearchResult.failure(
                TeamColorBoundsException(f"{method}: {TeamNameBoundsException.DEFAULT_MESSAGE}")
            )
        except Exception as ex:
            return SearchResult.failure(
                TeamSchemaFinderException(ex=ex, message=f"{method}: {TeamSchemaFinderException.DEFAULT_MESSAGE}")
            )