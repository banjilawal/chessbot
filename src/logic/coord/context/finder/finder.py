# src/logic/query/coord/finder/finder.py

"""
Module: logic.query.coord.finder.finder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import List

from logic.system import DataFinder, LoggingLevelRouter, Finder, SearchException, SearchResult
from logic.coord import (
    Coord, CoordContext, CoordContextValidationProcess, CoordDatasetNullException,
    CoordSearchException, CoordSearchPayloadTypeException, CoordSearchRouteException
)


class CoordFinder(DataFinder[Coord]):
    """
    Role:SearchProcess

    Responsibilities:
    1.  Send bag in a TokenList whose attribute value match the query.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.

    # LIMITATIONS:
    1.  TokenFinder sends the raw list of matches. Resolving id collisions is the caller's responsibility.

    # PARENT
        *   SearchProcess

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            dataset: List[Coord],
            context: CoordContext,
            context_validator: CoordContextValidationProcess = CoordContextValidationProcess(),
    ) -> SearchResult[List[Coord]]:
        """
        # ACTION:
            1.  If the collider_candidates is null or the wrong type send the exception in the SearchResult.
            2.  If the query fails validation send the exception in the SearchResult. Else, route to the
                search method which matches the query key.
            3.  The search method returns either an empty result or a list of tokens. Any exceptions were caught earlier
                by the search router.
       # PARAMETERS:
            *   collider_candidates (List[Token]):
            *   query: TokenContext
            *   context_validator: TokenContextValidationProcess
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            *   TypeError
            *   TokenNullDatasetException
            *   TokenSearchException
        """
        method = "CoordFinder.find"
        
        # Handle the case that, the collider_candidates is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordSearchException(
                    msg=f"{method}: {CoordSearchException.MSG}",
                    ex=CoordDatasetNullException(f"{method}: {CoordDatasetNullException.MSG}")
                )
            )
        # Handle the case that, the collider_candidates is of the wrong type.
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordSearchException(
                    msg=f"{method}: {CoordSearchException.MSG}",
                    ex=CoordSearchPayloadTypeException(f"{method}: {CoordSearchPayloadTypeException.MSG}")
                )
            )
        # handle the case that, query fails integrity tests.
        context_validation = context_validator.execute(context)
        if context_validation.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordSearchException(
                    msg=f"{method}: {CoordSearchException.MSG}",
                    ex=context_validation.exception
                )
            )
        # --- Route to the search method which matches the query key. ---#
        
        # Entry point into finding by coord's row.
        if context.row is not None and context.column is None:
            return cls._find_by_row(dataset=dataset, row=context.row)
        # Entry point into finding by coord's column.
        if context.column is not None and context.row is None:
            return cls._find_by_column(dataset=dataset, column=context.column)
        # Entry point into finding by coord's row and column.
        if context.column is not None and context.row is not None:
            return cls._find_by_row_and_column(dataset=dataset, row=context.row, column=context.column)
        
        # If a query does not have a search route defined send an exception chain.
        return SearchResult.failure(
            CoordSearchException(
                msg=f"{method}: {CoordSearchException.MSG}",
                ex=CoordSearchRouteException(f"{method}: {CoordSearchRouteException.MSG}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_row( cls, dataset: List[Coord], row: int ) -> SearchResult[List[Coord]]:
        """
        # ACTION:
            1.  Get coords with the matching row.
        # PARAMETERS:
            *   row (int)
            *   column (int)
        # RETURNS:
            *   SearchResult[List[Coord]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Coord] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "CoordFinder._find_by_row"
        matches = [coord for coord in dataset if coord.row == row]
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_column(cls, dataset: List[Coord], column: int) -> SearchResult[List[Coord]]:
        """
        # ACTION:
            1.  Get coords with the matching column.
        # PARAMETERS:
            *   row (int)
            *   column (int)
        # RETURNS:
            *   SearchResult[List[Coord]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Coord] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "CoordFinder._find_by_column"
        matches = [coord for coord in dataset if coord.column == column]
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_row_and_column(cls, dataset: List[Coord], row:int, column: int) -> SearchResult[List[Coord]]:
        """
        # ACTION:
            1.  Get the Coord which matches the row and column.
        # PARAMETERS:
            *   row (int)
            *   column (int)
        # RETURNS:
            *   SearchResult[List[Coord]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Coord] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "CoordFinder._find_by_row_and_column"
        matches = [coord for coord in dataset if coord.row == row and coord.column == column]
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(payload=matches)