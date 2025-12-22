# src/chess/schema/lookup/lookup.py

"""
Module: chess.schema.lookup.lookup
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from chess.schema import (
    SchemaColorBoundsException, SchemaNameBoundsException, SchemaSuperKey, SchemaMapBuilder,
    SchemaSuperKeyValidator, SchemaLookupFailedException, SchemaValidator, Schema, SchemaLookupException
)
from chess.system import (
    ForwardLookup, FailsafeBranchExitPointException, GameColor, LoggingLevelRouter, SearchResult,
    id_emitter
)


class SchemaLookup(ForwardLookup[SchemaSuperKey]):
    """
    # ROLE: Forward Lookups

    # RESPONSIBILITIES:
    1.  Run forward lookups on the Schema hashtable to find a Team's play_directive_metadata for a game.
    2.  Indicate there is no play_directive for a given key-value pair by returning an exception to the caller.
    3.  Verifies correctness of key-value map before running the forward lookup.

    # PARENT:
        *   ForwardLookup

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    # SERVICE_NAME = "SchemaLookup"
    # def lookup(
    #         self,
    #         name: str = SERVICE_NAME,
    #         id: int = id_emitter.lookup_id,
    #         enum_validator: SchemaValidator = SchemaValidator(),
    #         map_builder: SchemaMapBuilder = SchemaMapBuilder(),
    #         map_validator: SchemaSuperKeyValidator = SchemaSuperKeyValidator(),
    # ):
    #     super().lookup(
    #         id=id,
    #         name=name,
    #         enum_validator=enum_validator,
    #         map_builder=map_builder,
    #         map_validator=map_validator
    #     )
    #
    # @property
    # def schema_validator(self) -> SchemaValidator:
    #     """Return an SchemaValidator."""
    #     return cast(SchemaValidator, self.enum_validator)
    #
    # @property
    # def map_builder(self) -> SchemaMapBuilder:
    #     """Return an SchemaMapBuilder."""
    #     return cast(SchemaMapBuilder, self.map_builder)
    #
    # @property
    # def map_validator(self) -> SchemaSuperKeyValidator:
    #     """Return an SchemaSuperKeyValidator."""
    #     return cast(SchemaSuperKeyValidator, self.map_validator)
    #
    # @property
    # def allowed_colors(self) -> List[GameColor]:
    #     """Returns a list of all permissible schema colors."""
    #     return [member.color for member in Schema]
    #
    # @property
    # def allowed_names(self) -> List[str]:
    #     """Returns a list of all permissible schema names in upper case."""
    #     return [member.name.upper() for member in Schema]
    
    @classmethod
    @LoggingLevelRouter.monitor
    def lookup(
            cls,
            map: SchemaSuperKey,
            map_validator: SchemaSuperKeyValidator = SchemaSuperKeyValidator()
    ) -> SearchResult[List[Schema]]:
        """
        # Action:
        1.  Certify the provided map with the validator.
        2.  If the map validation fails return the exception in a validation result. Otherwise, return
            the schema entries with the targeted key-values.
            
        # Parameters:
            *   map: SchemaSuperKey
            *   map_validator: SchemaSuperKeyValidator

        # Returns:
        SearchResult[List[Schema]] containing either:
            - On error: Exception , payload null
            - On finding a match: List[Schema] in the payload.
            - On no matches found: Exception null, payload null

        # Raises:
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup.lookup"
        try:
            # certify the map is safe.
            validation = map_validator.validate(candidate=map)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            # After verification use the hash key to route to the appropriate lookup method.
            
            # Entry point into forward lookups by name.
            if map.name is not None:
                return cls._lookup_by_name(name=map.name)
            # Entry point into forward lookups by name.
            if map.color is not None:
                return cls._lookup_by_color(color=map.color)
            
            # Failsafe if any map cases was missed
            return SearchResult.failure(
                FailsafeBranchExitPointException(
                    f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}"
                )
            )

        # Finally, if some exception is not handled by the checks wrap it inside a SchemaLookupFailedException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SchemaLookupFailedException(ex=ex, message=f"{method}: {SchemaLookupFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_name(cls, name: str) -> SearchResult[List[Schema]]:
        """
        # Action:
        1.  Get any Schema entry which matches the targeted name-value key.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[Schema]] containing either:
            - On error: Exception , payload null
            - On finding a match: List[Schema] in the payload.
            - On no matches found: Exception null, payload null

        # Raises:
            *   SchemaNameBoundsException
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup._find_by_name"
        try:
            matches = [entry for entry in Schema if entry.name.upper() == name.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            
            # If no Schema entry has the targeted key-value return an exception because no hits in the hash table
            # indicate that  there is either no subclass whose different behavior is implemented with a strategy or,
            # class objects of the same type, same behavior but different metadata.
            return SearchResult.failure(
                SchemaColorBoundsException(f"{method}: {SchemaNameBoundsException.DEFAULT_MESSAGE}")
            )
        
        # Finally, if some exception is not handled by the checks wrap it inside a
        # SchemaLookupFailedException then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SchemaLookupFailedException(ex=ex, message=f"{method}: {SchemaLookupFailedException.DEFAULT_MESSAGE}")
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
        try:
            matches = [entry for entry in Schema if entry.color == color]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            
            # If no Schema entry has the targeted key-value return an exception because no hits in the hash table
            # indicate that  there is either no subclass whose different behavior is implemented with a strategy or,
            # class objects of the same type, same behavior but different metadata.
            return SearchResult.failure(
                SchemaColorBoundsException(f"{method}: {SchemaNameBoundsException.DEFAULT_MESSAGE}")
            )
        
        # Finally, if some exception is not handled by the checks wrap it inside a
        # SchemaLookupFailedException then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SchemaLookupFailedException(ex=ex, message=f"{method}: {SchemaLookupFailedException.DEFAULT_MESSAGE}")
            )
    
    # _id: int
    # _name: str
    # _enum_validator: Validator[Enum]
    # _context_builder: Builder[Context[Enum]]
    # _context_validator: Validator[Context[Enum]]
    #
    # def __init__(
    #         self,
    #         id: int,
    #         name: str,
    #         enum_validator: Validator[Enum],
    #         context_builder: Builder[Context[Enum]],
    #         context_validator: Validator[Context[Enum]],
    # ):
    #     self._id = id
    #     self._name = name
    #     self._enum_validator = enum_validator
    #     self._context_builder = context_builder
    #     self._context_validator = context_validator
    #
    # @property
    # def id(self) -> int:
    #     return self._id
    #
    # @@property
    # def name(self) -> str:
    #     return self._name
    #
    # @property
    # def enum_validator(self) -> Validator[Enum]:
    #     return self._enum_validator
    #
    # @property
    # def context_builder(self) -> Builder[Context[Enum]]:
    #     return self._context_builder
    #
    # @property
    # def context_validator(self) -> Validator[Context[Enum]]:
    #     return self._context_validator