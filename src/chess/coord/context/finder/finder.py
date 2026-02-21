# src/chess/context/coord/finder/finder.py

"""
Module: chess.context.coord.finder.finder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import List

from chess.system import DataFinder, LoggingLevelRouter, Finder, SearchException, SearchResult
from chess.coord import (
    Coord, CoordContext, CoordContextValidator, CoordDatasetNullException,
    CoordSearchException, CoordSearchPayloadTypeException, CoordSearchRouteException
)


class CoordFinder(DataFinder[Coord]):
    """
    # ROLE: AbstractSearcher

    # RESPONSIBILITIES:
    1.  Send bag in a TokenList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.

    # LIMITATIONS:
    1.  TokenFinder sends the raw list of matches. Resolving id collisions is the caller's responsibility.

    # PARENT
        *   AbstractSearcher

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            dataset: List[Coord],
            context: CoordContext,
            context_validator: CoordContextValidator = CoordContextValidator(),
    ) -> SearchResult[List[Coord]]:
        """
        # ACTION:
            1.  If the dataset is null or the wrong type send the exception in the SearchResult.
            2.  If the context fails validation send the exception in the SearchResult. Else, route to the
                search method which matches the context key.
            3.  The search method returns either an empty result or a list of tokens. Any exceptions were caught earlier
                by the search router.
       # PARAMETERS:
            *   dataset (List[Token]):
            *   context: TokenContext
            *   context_validator: TokenContextValidator
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TypeError
            *   TokenNullDatasetException
            *   TokenSearchException
        """
        method = "CoordFinder.find"
        
        # Handle the case that the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordSearchException(
                    message=f"{method}: {CoordSearchException.DEFAULT_MESSAGE}",
                    ex=CoordDatasetNullException(f"{method}: {CoordDatasetNullException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the dataset is of the wrong type.
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordSearchException(
                    message=f"{method}: {CoordSearchException.DEFAULT_MESSAGE}",
                    ex=CoordSearchPayloadTypeException(f"{method}: {CoordSearchPayloadTypeException.DEFAULT_MESSAGE}")
                )
            )
        # handle the case that context fails integrity tests.
        context_validation = context_validator.validate(context)
        if context_validation.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordSearchException(
                    message=f"{method}: {CoordSearchException.DEFAULT_MESSAGE}",
                    ex=context_validation.exception
                )
            )
        # --- Route to the search method which matches the context key. ---#
        
        # Entry point into finding by coord's row.
        if context.row is not None and context.column is None:
            return cls._find_by_row(dataset=dataset, row=context.row)
        # Entry point into finding by coord's column.
        if context.column is not None and context.row is None:
            return cls._find_by_column(dataset=dataset, column=context.column)
        # Entry point into finding by coord's row and column.
        if context.column is not None and context.row is not None:
            return cls._find_by_row_and_column(dataset=dataset, row=context.row, column=context.column)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            CoordSearchException(
                message=f"{method}: {CoordSearchException.DEFAULT_MESSAGE}",
                ex=CoordSearchRouteException(f"{method}: {CoordSearchRouteException.DEFAULT_MESSAGE}")
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
        # RAISES:
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
        # RAISES:
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
        # RAISES:
            None
        """
        method = "CoordFinder._find_by_row_and_column"
        matches = [coord for coord in dataset if coord.row == row and coord.column == column]
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(payload=matches)