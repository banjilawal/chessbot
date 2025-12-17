# src/chess/team/schema/lookup/lookup.py

"""
Module: chess.team.schema.lookup.lookup
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import List, cast

from chess.team import (
    TeamColorBoundsException, TeamNameBoundsException, SchemaContext, SchemaContextBuilder,
    SchemaContextValidator, TeamSchemaLookupException, TeamSchemaValidator, TeamSchema
)
from chess.system import EntityService, GameColor, LoggingLevelRouter, Result, SearchResult, id_emitter


class TeamSchemaLookup(EntityService[SchemaContext]):
    """
    # ROLE: MetadataLookup, Utility

    # RESPONSIBILITIES:
    1.  Public facing Team State Machine microlookup API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Team state by providing single entry and exit points to Team
        lifecycle.

    # PARENT:
        *   EntityLookup

    # PROVIDES:
        *   allowed_colors() -> List[GameColor]:
        *   allowed_names() -> List[str]:
        *   enemy_schema(schema: TeamSchema) -> Result[TeamSchema]:

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityLookup for inherited attributes.
    """
    DEFAULT_NAME = "TeamSchemaLookup"
    _schema_validator: TeamSchemaValidator
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.lookup_id,
            schema_validator: TeamSchemaValidator = TeamSchemaValidator(),
            context_builder: SchemaContextBuilder = SchemaContextBuilder(),
            context_validator: SchemaContextValidator = SchemaContextValidator(),
    ):
        super().__init__(id=id, name=name, builder=context_builder, validator=context_validator)
        self._schema_validator = schema_validator
    
    @property
    def schema_validator(self) -> TeamSchemaValidator:
        return self._schema_validator
    
    @property
    def schema_context_builder(self) -> SchemaContextBuilder:
        return cast(SchemaContextBuilder, self.entity_builder)
    
    @property
    def schema_context_validator(self) -> SchemaContextValidator:
        return cast(SchemaContextValidator, self.entity_validator)
    
    @property
    def allowed_colors(self) -> List[GameColor]:
        """Returns a list of all permissible team colors."""
        return [member.color for member in TeamSchema]
    
    @property
    def allowed_names(self) -> List[str]:
        """Returns a list of all permissible team names in upper case."""
        return [member.name.upper() for member in TeamSchema]
    
    def enemy_schema(self, schema: TeamSchema) -> Result[TeamSchema]:
        validation = self._schema_validator.validate(schema)
        if validation.is_failure:
            return Result.failure(validation.exception)
        if schema == TeamSchema.WHITE: return Result[TeamSchema.BLACK]
        return Result[TeamSchema.WHITE]
    
    @classmethod
    @LoggingLevelRouter.monitor
    def lookup_schema(
            cls,
            context: SchemaContext,
            context_validator: SchemaContextValidator = SchemaContextValidator()
    ) -> SearchResult[List[TeamSchema]]:
        """
        # Action:
        1.  TeamSchema is an Enum to follow the Finder contract a default dataset of List[TeamSchema] has been set.
            It's not used anywhere. even if a dataset argument is passed.
        2.  Use context_validator to certify the provided context.
        3.  Context attribute routes the search. Attribute value is the search target.
        4.  The outcome of the search is sent back to the caller in a SearchResult object.

        # Parameters:
            *   dataset (List[TeamSchema]):
            *   context: SchemaContext
            *   context_validator: SchemaContextValidator

        # Returns:
        SearchResult[List[TeamSchema]] containing either:
            - On finding a match: List[TeamSchema] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TeamSchemaLookupException
        """
        method = "TeamSchemaFinder.find"
        try:
            # certify the context is safe.
            validation = context_validator.validate(candidate=context)
            if validation.is_failure:
                return SearchResult.failure(validation.exception)
            # After context is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by color value.
            if context.color is not None:
                return cls._lookup_by_color(color=context.color)
            # Entry point into searching by name value.
            if context.name is not None:
                return cls._lookup_by_name(name=context.name)
        
        # Finally, if some exception is not handled by the checks wrap it inside a
        # TeamSchemaLookupException then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamSchemaLookupException(
                    ex=ex, message=f"{method}: {TeamSchemaLookupException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_color(cls, color: GameColor) -> SearchResult[List[TeamSchema]]:
        """
        # Action:
        1.  Get the TeamSchema which matches the target color.

        # Parameters:
            *   color (TeamSchemaColor)

        # Returns:
        SearchResult[List[TeamSchema]] containing either:
            - On finding a match: List[TeamSchema] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TeamColorBoundsException
            *   TeamSchemaFinderOperationException
        """
        method = "TeamSchemaFinder._find_by_color"
        try:
            if color in TeamSchema.color:
                return SearchResult.success(List[TeamSchema.color])
            # If a match is not found return an exception. It's important to know if no schema has that color.
            return SearchResult.failure(
                TeamColorBoundsException(f"{method}: {TeamColorBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a
        # TeamSchemaLookupException then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamSchemaLookupException(
                    ex=ex, message=f"{method}: {TeamSchemaLookupException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _lookup_by_name(cls, name: str) -> SearchResult[List[TeamSchema]]:
        """
        # Action:
        1.  Get the TeamSchema which matches the target name.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[TeamSchema]] containing either:
            - On finding a match: List[TeamSchema] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TeamNameBoundsException
            *   TeamSchemaFinderOperationException
        """
        method = "TeamSchemaFinder._find_by_name"
        try:
            if name.upper() in TeamSchema.name.upper():
                return SearchResult.success(List[TeamSchema.name])
            # If a match is not found return an exception. Its important to know if no schema has that name.
            return SearchResult.failure(
                TeamColorBoundsException(f"{method}: {TeamNameBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside a
        # TeamSchemaLookupException then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                TeamSchemaLookupException(
                    ex=ex, message=f"{method}: {TeamSchemaLookupException.DEFAULT_MESSAGE}"
                )
            )