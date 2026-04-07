# src/logic/schema/database/search/route/router.py

"""
Module: logic.schema.database.search.route.router
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Type

from system import GameColor, LoggingLevelRouter, SearchResult, SearchRouter
from model.catalog import (
    MissingSchemaSearchRouteException, Schema, SchemaQuery, SchemaQueryValidator,
    SchemaSearchException
)


class SchemaSearchRouter(SearchRouter[Schema]):
    """
    Role:SearchRouter

    Responsibilities:
    1.  Send bag in a SchemaList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.
    
    # LIMITATIONS:
    1.  SchemaSearchRouter sends the raw list of matches. Resolving id collisions is the caller's responsibility.

    # PARENT
        *   SearchRouter

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def route(
            cls,
            query: SchemaQuery,
            query_validator:SchemaQueryValidator = SchemaQueryValidator(),
    ) -> SearchResult[List[Schema]]:
        """
        Find schemas whith an attribute that fits the context.
        
        Action:
            1.  Send an exception chain in the SearchResult if either:
                    -   The params check fails.
                    -   There is no search logic for the context
            2.  Otherwise, send the success result.
        Args:
            query: SchemaQuery,
            query_validator: SchemaQueryValidator,
        Returns:
            SearchResult[List[Schema]]
        Raises:
            SchemaSearchException
            MissingSchemaSearchRouteException
        """
        method = f"{cls.__name__}.route"

        # Handle the case that, the query is not safe to use.
        query_validation_result = query_validator.validate(query)
        if query_validation_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                SchemaSearchException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=SchemaSearchException.OP,
                    msg=SchemaSearchException.MSG,
                    err_code=SchemaSearchException.ERR_CODE,
                    rslt_type=SchemaSearchException.RSLT_TYPE,
                    ex=query_validation_result.exception
                )
            )
    # --- Route to the search method which matches the context key. ---#
        
        # schema.name search entry point.
        if query.context.name is not None:
            return cls._find_by_name(
                catalog=query.catalog,
                name=query.context.name,
            )
        # schema.color search entry point
        if query.context.color is not None:
            return cls._find_by_name(
                catalog=query.catalog,
                color=query.context.name,
            )

        # Handle the case that, there is no search path for the context context..
        return SearchResult.failure(
            SchemaSearchException(
                cls_mthd=method,
                cls_name=method.__name__,
                op=SchemaSearchException.OP,
                msg=SchemaSearchException.MSG,
                err_code=SchemaSearchException.ERR_CODE,
                rslt_type=SchemaSearchException.RSLT_TYPE,
                ex=MissingSchemaSearchRouteException(
                    msg=MissingSchemaSearchRouteException.MSG,
                    err_code=MissingSchemaSearchRouteException.ERR_CODE,
                )
            )
        )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(
            cls,
            name: str,
            catalog: Type[Schema],
    ) -> SearchResult[List[Schema]]:
        """
        Search the schema by a schema id
        
            1.  Get the Schemas with the desired id.
        Args:
            name: str
            catalog: List[Schema]
        Returns:
            SearchResult[List[Schema]]
        Raises:
        """
        matches = [entry for entry in catalog if entry.name.upper() == name.upper()]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_color(
            cls,
            catalog: Type[Schema],
            color: GameColor,
    ) -> SearchResult[List[Schema]]:
        """
        Search the schema by color.

        Args:
            color: GameColor
            catalog: Schema
        Returns:
            SearchResult[List[Schema]]
        Raises
        """
        matches = [entry for entry in catalog if entry.color == color]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)