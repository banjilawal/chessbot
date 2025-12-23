# src/chess/schema/lookup/lookup.py

"""
Module: chess.schema.lookup.lookup
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from enum import Enum
from typing import List, cast

from chess.schema import (
    SchemaColorBoundsException, SchemaNameBoundsException, SchemaSuperKey,
    SchemaSuperKeyValidator, Schema,
)
from chess.schema.lookup.forward.route import ForwardSchemaRouteException
from chess.schema.lookup.forward.wrapper import ForwardSchemaFailedException
from chess.system import (
    ForwardLookup, GameColor, LoggingLevelRouter, SearchResult
)


class ForwardSchemaLookup(ForwardLookup[SchemaSuperKey]):
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
    method = "SchemaSuperKeyBuilder.build"
    try:
        # Count how many optional parameters are not-null.
        params = [name, color, ]
        param_count = sum(bool(p) for p in params)
        

        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaSuperKeyBuildFailedException(
                    message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE} - ",
                    ex=ZeroSchemaSuperKeysException(f"{method}: {ZeroSchemaSuperKeysException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaSuperKeyBuildFailedException(
                    message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE} - ",
                    ex=ExcessiveSchemaSuperKeysException(f"{method}: {ExcessiveSchemaSuperKeysException}")
                )
            )
        
        # Route to the appropriate validation branch.
        
        # Build the name SchemaSuperKey if its value is set.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SchemaSuperKeyBuildFailedException(
                        message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE} - ",
                        ex=validation.exception
                    )
                )
            # On validation success return a SchemaKey_name in the BuildResult.
            return BuildResult.success(SchemaSuperKey(name=name))
        
        # Build the color_key SchemaSuperKey if its value is set.
        if color is not None:
            validation = color_validator.validate(candidate=color)
            if validation.is_failure:

                return BuildResult.failure(
                    SchemaSuperKeyBuildFailedException(
                        message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE} - ",
                        ex=validation.exception
                    )
                )
            # On validation success return a SchemaKey_color in the BuildResult.
            return BuildResult.success(SchemaSuperKey(color=color))
        


    except Exception as ex:
        return BuildResult.failure(
            SchemaSuperKeyBuildFailedException(
                ex=ex, message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE}"
            )
        )
    
    @classmethod
    def lookup(
            cls,
            super_key: SchemaSuperKey,
            super_key_validator: SchemaSuperKeyValidator
    ) -> SearchResult[List[Schema]]:
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
        method = "ForwardSchemaLookup.lookup"
        try:
            # Handle the case that the SuperKey fails validation.
            validation = super_key_validator.validate(candidate=super_key)
            if validation.is_failure:
                # Return the exception chain on failure.
                return SearchResult.failure(
                    ForwardSchemaFailedException(
                        ex=validation.exception, message=f"{method}: {ForwardSchemaFailedException.ERROR_CODE}"
                    )
                )
            # After verification use the hash key to route to the appropriate lookup method.
            
            # Entry point into forward lookups by name.
            if super_key.name is not None:
                return cls._lookup_by_name(name=super_key.name)
            # Entry point into forward lookups by name.
            if super_key.color is not None:
                return cls._lookup_by_color(color=super_key.color)
            
            # Handle the default case where no exception is raised and SchemaSuperKey was not covered with an if-block
            return SearchResult.failure(
                ForwardSchemaFailedException(
                    message=f"{method}: {ForwardSchemaFailedException.ERROR_CODE} -> ",
                    ex=ForwardSchemaRouteException(f"{method}: {ForwardSchemaRouteException.DEFAULT_MESSAGE}")
                )
            )
        
        # Finally, wrap a ForwardSchemaFailedException around any missed exception then return the exception-chain
        # in the SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                ForwardSchemaFailedException(
                    ex=ex, message=f"{method}: {ForwardSchemaFailedException.ERROR_CODE}"
                )
            )
        
    
    # SERVICE_NAME = "ForwardSchemaLookuo"
    # def lookup(
    #         self,
    #         name: str = SERVICE_NAME,
    #         id: int = id_emitter.lookup_id,
    #         enum_validator: SchemaValidator = SchemaValidator(),
    #         key_builder: SchemaSuperKeyBuilder = SchemaSuperKeyBuilder(),
    #         key_validator: SchemaSuperKeyValidator = SchemaSuperKeyValidator(),
    # ):
    #     super().lookup(
    #         id=id,
    #         name=name,
    #         enum_validator=enum_validator,
    #         key_builder=key_builder,
    #         key_validator=key_validator
    #     )
    #
    # @property
    # def schema_validator(self) -> SchemaValidator:
    #     """Return an SchemaValidator."""
    #     return cast(SchemaValidator, self.enum_validator)
    #
    # @property
    # def key_builder(self) -> SchemaSuperKeyBuilder:
    #     """Return an SchemaSuperKeyBuilder."""
    #     return cast(SchemaSuperKeyBuilder, self.key_builder)
    #
    # @property
    # def key_validator(self) -> SchemaSuperKeyValidator:
    #     """Return an SchemaSuperKeyValidator."""
    #     return cast(SchemaSuperKeyValidator, self.key_validator)
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
    def _lookup_by_name(cls, name: str) -> SearchResult[List[Schema]]:
        """
        # Action:
        1.  Get any Schema entry which matches the targeted name-value key.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[Schema]] containing either:
            - On error: Exception
            - On finding a match: List[Schema] in the payload.
            - On no matches found: Exception null, payload null

        # Raises:
            *   SchemaNameBoundsException
            *   SchemaLookupFailedException
        """
        method = "ForwardSchemaLookup._lookup_by_name"
        try:
            matches = [entry for entry in Schema if entry.name.upper() == name.upper()]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            
            # If no Schema entry has the targeted key-value return an exception because no hits in the hash table
            # indicate that  there is either no subclass whose different behavior is implemented with a strategy or,
            # class objects of the same type, same behavior but different metadata.
            return SearchResult.failure(
                ForwardSchemaFailedException(
                    message=f"{method}: {ForwardSchemaFailedException.ERROR_CODE}",
                    ex=SchemaColorBoundsException(f"{method}: {SchemaNameBoundsException.DEFAULT_MESSAGE}")
                )
            )
        
        # Finally, if some exception is not handled by the checks wrap it inside a
        # SchemaLookupFailedException then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                ForwardSchemaFailedException(ex=ex, message=f"{method}: {ForwardSchemaFailedException.ERROR_CODE}")
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
        method = "ForwardSchemaLookup._find_by_color"
        try:
            matches = [entry for entry in Schema if entry.color == color]
            # This is the expected case.
            if len(matches) >= 1:
                return SearchResult.success(matches)
            
            # If no Schema entry has the targeted key-value return an exception because no hits in the hash table
            # indicate that  there is either no subclass whose different behavior is implemented with a strategy or,
            # class objects of the same type, same behavior but different metadata.
            return SearchResult.failure(
                ForwardSchemaFailedException(
                    message=f"{method}: {ForwardSchemaFailedException.ERROR_CODE}",
                    ex=SchemaColorBoundsException(f"{method}: {SchemaColorBoundsException.DEFAULT_MESSAGE}")
                )
            )
        
        # Finally, if some exception is not handled by the checks wrap it inside a
        # SchemaLookupFailedException then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                ForwardSchemaFailedException(ex=ex, message=f"{method}: {ForwardSchemaFailedException.ERROR_CODE}")
            )