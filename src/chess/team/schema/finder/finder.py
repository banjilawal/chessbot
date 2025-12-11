# src/chess/team/schema/finder/finder.py

"""
Module: chess.team.schema.finder.finder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from typing import List


from chess.system import Finder, GameColor, LoggingLevelRouter, SearchResult
from chess.team import (
    NullTeamSchemaException, TeamColorBoundsException, TeamNameBoundsException, TeamSchema, TeamSchemaContext,
    TeamSchemaContextValidator, TeamSchemaFinderException
)


class TeamSchemaFinder(Finder[TeamSchema]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Search TeamSchema collections for items which match the attribute target specified in the TeamSchemaContext parameter.
    2.  Safely forward any errors encountered during a search to the caller.

    # PARENT
        *   Finder

    # PROVIDES:
        *   TeamFinder:

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
        
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            context: TeamSchemaContext,
            data_set: List[TeamSchema] = List[TeamSchema],
            context_validator: TeamSchemaContextValidator = TeamSchemaContextValidator()
    ) -> SearchResult[List[TeamSchema]]:
        """
        # Action:
        1.  Verify the data_set is not null and contains only TeamSchema objects,
        2.  Use context_validator to certify the provided context.
        3.  Context attribute routes the search. Attribute value is the search target.
        4.  The outcome of the search is sent back to the caller in a SearchResult object.

        # Parameters:
            *   data_set (List[TeamSchema]):
            *   context: TeamSchemaContext
            *   context_validator: TeamSchemaContextValidator

        # Returns:
        SearchResult[List[TeamSchema]] containing either:
                - On success: List[teamSchema] in the payload.
                - On failure: Exception.

        # Raises:
            *   TypeError
            *   TeamSchemaNullDataSetException
            *   TeamSchemaFinderException
        """
        method = "TeamSchemaFinder.find"
        try:
            # Don't want to run a search if the data_Set is null.
            if data_set is None:
                return SearchResult.failure(
                    NullTeamSchemaException(f"{method}: {NullTeamSchemaException.DEFAULT_MESSAGE}")
                )
            # certify the context is safe.
            context_validation = context_validator.validate(candidate=context)
            if context_validation.is_failure:
                return SearchResult.failure(context_validation.exception)
            # After context is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by color value.
            if context.color is not None:
                return cls._find_by_color(color=context.color)
            # Entry point into searching by name value.
            if context.name is not None:
                return cls._find_by_name(name=context.name)
        # Finally, if some exception is not handled by the checks wrap it inside an TeamSchemaFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamSchemaFinderException(ex=ex, message=f"{method}: {TeamSchemaFinderException.DEFAULT_MESSAGE}")
            )
            
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_color(cls, color: GameColor) -> SearchResult[List[TeamSchema]]:
        """
        # Action:
        1.  Get the TeamSchema which matches the target color.
        2.  If no match is found return an exception.

        # Parameters:
            *   color (TeamSchemaColor)

        # Returns:
        SearchResult[List[TeamSchema]] containing either:
            - On success: List[TeamSchema] in the payload.
            - On failure: Exception.

        # Raises:
            *   TeamColorBoundsException
            *   TeamSchemaFinderException
        """
        method = "TeamSchemaFinder._find_by_color"
        try:
            if color in TeamSchema.color:
                return SearchResult.success(List[TeamSchema.color])
            # If a match is not found return an exception. Its important to know if no schema has that color.
            return SearchResult.failure(
                TeamColorBoundsException(f"{method}: {TeamColorBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside an TeamSchemaFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamSchemaFinderException(ex=ex, message=f"{method}: {TeamSchemaFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, name: str) -> SearchResult[List[TeamSchema]]:
        """
        # Action:
        1.  Get the TeamSchema which matches the target name.
        2.  If no match is found return an exception.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[TeamSchema]] containing either:
            - On success: List[TeamSchema] in the payload.
            - On failure: Exception.

        # Raises:
            *   TeamNameBoundsException
            *   TeamSchemaFinderException
        """
        method = "TeamSchemaFinder._find_by_name"
        try:
            if name.upper() in TeamSchema.name.upper():
                return SearchResult.success(List[TeamSchema.name])
            # If a match is not found return an exception. Its important to know if no schema has that name.
            return SearchResult.failure(
                TeamColorBoundsException(f"{method}: {TeamNameBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside an TeamSchemaFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamSchemaFinderException(ex=ex, message=f"{method}: {TeamSchemaFinderException.DEFAULT_MESSAGE}")
            )