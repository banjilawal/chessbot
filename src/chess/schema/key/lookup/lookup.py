# src/chess/schema/key/lookup/lookup.py

"""
Module: chess.schema.key.lookup.lookup
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List

from chess.schema import (
    SchemaLookupFailedException, UnhandledSchemaLookupRouteException, SchemaColorBoundsException,
    SchemaNameBoundsException, SchemaSuperKey, SchemaSuperKeyValidator, Schema,
)
from chess.system import ForwardLookup, GameColor, LoggingLevelRouter, SearchResult


class SchemaLookup(ForwardLookup[SchemaSuperKey]):
    """
    # ROLE: Forward Lookups

    # RESPONSIBILITIES:
    1.  Run forward lookups on the Schema hashtable to find a Team's play_directive_metadata for a game.
    2.  Indicate there is no play_directive for a given key-value pair by returning an exception to the caller.
    3.  Verifies correctness of key-value key before running the forward lookup.

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
    def lookup(cls, super_key: SchemaSuperKey, super_key_validator: SchemaSuperKeyValidator) -> SearchResult[List[Schema]]:
        """
        # Action:
        1.  Certify the provided key with the validator.
        2.  If the key validation fails return the exception in a validation result. Otherwise, return
            the schema entries with the targeted key-values.

        # Parameters:
            *   key: SchemaSuperKey
            *   key_validator: SchemaSuperKeyValidator

        # Returns:
        SearchResult[List[Schema]] containing either:
            - On error: Exception , payload null
            - On finding a match: List[Schema] in the payload.
            - On no matches found: Exception null, payload null

        # Raises:
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup.lookup"

        # Handle the case that the SuperKey fails validation.
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
            return cls._lookup_by_name(name=super_key.name)
        # Entry point into forward lookups by color.
        if super_key.color is not None:
            return cls._lookup_by_color(color=super_key.color)
        
        # The default result path is failure.
        return SearchResult.failure(
            SchemaLookupFailedException(
                message=f"{method}: {SchemaLookupFailedException.ERROR_CODE} -> ",
                ex=UnhandledSchemaLookupRouteException(f"{method}: {UnhandledSchemaLookupRouteException.DEFAULT_MESSAGE}"
                )
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_name(cls, target: str) -> SearchResult[List[Schema]]:
        """
        # Action:
        1.  Get any Schema entry whose name matches the target value.

        # Parameters:
            *   target (str)

        # Returns:
        SearchResult[List[Schema]] containing either:
            - On error: Exception
            - On finding a match: List[Schema] in the payload.
            - On no matches found: Exception null, payload null

        # Raises:
            *   SchemaNameBoundsException
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup._lookup_by_name"
        matches = [entry for entry in Schema if entry.name.upper() == target.upper()]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        # The default path is a failure.
        return SearchResult.failure(
            SchemaLookupFailedException(
                message=f"{method}: {SchemaLookupFailedException.ERROR_CODE} -> ",
                ex=SchemaColorBoundsException(f"{method}: {SchemaNameBoundsException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_color(cls, color: GameColor) -> SearchResult[List[Schema]]:
        """
        # Action:
        1.  Get any Schema entry which matches the targeted color-value key.

        # Parameters:
            *   color (GameColor)

        # Returns:
        SearchResult[List[Schema]] containing either:
            - On error: Exception , payload null
            - On finding a match: List[Schema] in the payload.
            - On no matches found: Exception null, payload null

        # Raises:
            *   SchemaColorBoundsException
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup._find_by_color"
        matches = [entry for entry in Schema if entry.color == color]
        # Finding at least one match is success.
        if len(matches) >= 1:
            return SearchResult.success(matches)
        # The default path is failure
        return SearchResult.failure(
            SchemaLookupFailedException(
                message=f"{method}: {SchemaLookupFailedException.ERROR_CODE}",
                ex=SchemaColorBoundsException(f"{method}: {SchemaColorBoundsException.DEFAULT_MESSAGE}")
            )
        )