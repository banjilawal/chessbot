# src/chess/schema/lookup/lookup.py

"""
Module: chess.schema.lookup.lookup
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from chess.schema import (
    SchemaColorBoundsException, SchemaNameBoundsException, SchemaContext, SchemaContextBuilder,
    SchemaContextValidator, SchemaLookupFailedException, SchemaValidator, Schema, SchemaLookupException
)
from chess.system import EnumLookup, GameColor, LoggingLevelRouter, SearchResult, id_emitter


class SchemaLookup(EnumLookup[SchemaContext]):
    """
    # ROLE: EnumLookup, Utility

    # RESPONSIBILITIES:
    1.  Lookup microservice API for mapping metadata values to Schema configurations.
    2.  Encapsulates integrity assurance logic for Schema lookup operations.


    # PARENT:
        *   EnumLookup

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EnumLookup for inherited attributes.
    """
    SERVICE_NAME = "SchemaLookup"
    
    def lookup(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.lookup_id,
            enum_validator: SchemaValidator = SchemaValidator(),
            context_builder: SchemaContextBuilder = SchemaContextBuilder(),
            context_validator: SchemaContextValidator = SchemaContextValidator(),
    ):
        super().lookup(
            id=id,
            name=name,
            enum_validator=enum_validator,
            context_builder=context_builder,
            context_validator=context_validator
        )

    @property
    def schema_validator(self) -> SchemaValidator:
        """Return an SchemaValidator."""
        return cast(SchemaValidator, self.enum_validator)
    
    @property
    def context_builder(self) -> SchemaContextBuilder:
        """Return an SchemaContextBuilder."""
        return cast(SchemaContextBuilder, self.context_builder)
    
    @property
    def context_validator(self) -> SchemaContextValidator:
        """Return an SchemaContextValidator."""
        return cast(SchemaContextValidator, self.context_validator)
    
    @property
    def allowed_colors(self) -> List[GameColor]:
        """Returns a list of all permissible schema colors."""
        return [member.color for member in Schema]
    
    @property
    def allowed_names(self) -> List[str]:
        """Returns a list of all permissible schema names in upper case."""
        return [member.name.upper() for member in Schema]
    
    @classmethod
    @LoggingLevelRouter.monitor
    def lookup(
            cls,
            context: SchemaContext,
            context_validator: SchemaContextValidator = SchemaContextValidator()
    ) -> SearchResult[List[Schema]]:
        """
        # Action:
        1.  Certify the provided context with the class method's validator param.
        2.  If the context validation fails return the exception in a validation result. Otherwise, return
            the configuration entries which matched the context.

        # Parameters:
            *   context: SchemaContext
            *   context_validator: SchemaContextValidator

        # Returns:
        SearchResult[List[Schema]] containing either:
            - On finding a match: List[Schema] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   SchemaLookupFailedException
        """
        method = "SchemaLookup.lookup"
        try:
            # certify the context is safe.
            validation = context_validator.validate(candidate=context)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            # After context is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by name value.
            if context.name is not None:
                return cls._lookup_by_name(name=context.name)
            # Entry point into searching by color value.
            if context.color is not None:
                return cls._lookup_by_color(color=context.color)
            
            # Failsafe if any context cases was missed
            return SearchResult.failure(
                SchemaLookupFailedException(f"{method}: {SchemaLookupFailedException.DEFAULT_MESSAGE}")
            )

        # Finally, if some exception is not handled by the checks wrap it inside a  SchemaLookupException then,
        # return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SchemaLookupException(ex=ex, message=f"{method}: {SchemaLookupException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_name(cls, name: str) -> SearchResult[List[Schema]]:
        """
        # Action:
        1.  Get any Schema which matches the target name.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[Schema]] containing either:
            - On finding a match: List[Schema] in the payload.
            - On error: Exception , payload null
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
            # If a match is not found return an exception. It's important to know if no schema has that name.
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
        1.  Get any Schema which matches the target color.

        # Parameters:
            *   color (GameColor)

        # Returns:
        SearchResult[List[Schema]] containing either:
            - On finding a match: List[Schema] in the payload.
            - On error: Exception , payload null
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
            # If a match is not found return an exception. It's important to know if no schema has that color.
            return SearchResult.failure(
                SchemaColorBoundsException(f"{method}: {SchemaNameBoundsException.DEFAULT_MESSAGE}")
            )
        
        # Finally, if some exception is not handled by the checks wrap it inside a
        # SchemaLookupFailedException then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SchemaLookupFailedException(ex=ex, message=f"{method}: {SchemaLookupFailedException.DEFAULT_MESSAGE}")
            )