# src/chess/schema/key/lookup/lookup.py

"""
Module: chess.schema.key.lookup.lookup
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List

from chess.schema import (
    SchemaLookupFailedException, SchemaLookupRouteException, SchemaColorBoundsException, SchemaKey, Schema,
    SchemaNameBoundsException, SchemaKeyValidator,
)
from chess.system import ForwardLookup, GameColor, HashLookup, LoggingLevelRouter, SearchResult


class SchemaLookup(HashLookup[Schema]):
    """
    # ROLE: Forward Lookups

    # RESPONSIBILITIES:
    1.  Run forward lookups on the Schema hashtable to find a Team's play_directive_metadata for a game.
    2.  Indicate there is no play_directive for a given key-value pair by returning an exception to the caller.
    3.  Verifies correctness of key-value key before running lookup.

    # PARENT:
        *   ForwardLookup

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    def query(
            cls,
            super_key: SchemaKey,
            super_key_validator: SchemaKeyValidator = SchemaKeyValidator()
    ) -> SearchResult[List[Schema]]:
        """
        # ACTION:
            1.  If super_key fails validation send the exception chain in the SearchResult. Else, route to the
                search method by the attribute portion of the Key.
            2.  If the value portion of the Key is not in the permitted attribute values send the exception
                chain in the SearchResult. Else, send Personas whose targeted attribute values match.
        # PARAMETERS:
            *   key: SchemaKey
            *   key_validator: SchemaKeyValidator
        # RETURNS:
            *   SearchResult[List[Schema]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Schema] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup.query"

        # Handle the case that the Key fails validation.
        validation = super_key_validator.validate(candidate=super_key)
        if validation.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SchemaLookupFailedException(
                    ex=validation.exception, message=f"{method}: {SchemaLookupFailedException.ERROR_CODE}"
                )
            )
        # After verification use the hash key to route to the appropriate lookup method.
        
        # Entry point into forward lookups by name.
        if super_key.name is not None:
            return cls._query_by_name(name=super_key.name)
        # Entry point into forward lookups by color.
        if super_key.color is not None:
            return cls._query_by_color(color=super_key.color)
        
        # The default path is failure.
        return SearchResult.failure(
            SchemaLookupFailedException(
                message=f"{method}: {SchemaLookupFailedException.ERROR_CODE}",
                ex=SchemaLookupRouteException(f"{method}: {SchemaLookupRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _query_by_name(cls, name: str) -> SearchResult[List[Schema]]:
        """
        # ACTION:
            1.  Get any Schema entry whose name matches the target value.
        # PARAMETERS:
            *   target (str)
        # RETURNS:
            *   SearchResult[List[Schema]] containing either:
                    - On error: Exception
                    - On finding a match: List[Schema] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   SchemaNameBoundsException
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup._by_name"
        
        matches = [entry for entry in Schema if entry.name.upper() == name.upper()]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        
        # The default path returns failure
        return SearchResult.failure(
            SchemaLookupFailedException(
                message=f"{method}: {SchemaLookupFailedException.ERROR_CODE}",
                ex=SchemaNameBoundsException(f"{method}: {SchemaNameBoundsException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _query_by_color(cls, color: GameColor) -> SearchResult[List[Schema]]:
        """
        # ACTION:
        1.  Get any Schema entry which matches the targeted color-value key.

        # PARAMETERS:
            *   color (GameColor)

        # RETURNS:
        SearchResult[List[Schema]] containing either:
            - On error: Exception , payload null
            - On finding a match: List[Schema] in the payload.
            - On no matches found: Exception null, payload null

        # RAISES:
            *   SchemaColorBoundsException
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup._find_by_color"
        
        matches = [entry for entry in Schema if entry.color == color]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        
        # The default path is failure.
        return SearchResult.failure(
            SchemaLookupFailedException(
                message=f"{method}: {SchemaLookupFailedException.ERROR_CODE}",
                ex=SchemaColorBoundsException(f"{method}: {SchemaColorBoundsException.DEFAULT_MESSAGE}")
            )
        )