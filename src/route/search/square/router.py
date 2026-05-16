# src/route/search/token/orange.py

"""
Module: route.search.token.orange
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from err import SquareSearchException
from model import Board, Coord, Formation, OpeningSquare, Square, SquareState, Token
from model.query import SquareQuery
from result import SearchResult
from route import SearchRouter
from util import LoggingLevelRouter


class SquareSearchRouter(SearchRouter[Square]):
    """
    Role:SearchRouter

    Responsibilities:
    1.  Send bag in a TokenList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.
    
    # LIMITATIONS:
    1.  TokenSearchRouter sends the raw list of matches. Resolving id collisions is the caller's responsibility.

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
            query: SquareQuery,
            query_validator: SquareQueryValidator | None = None,
    ) -> SearchResult[List[Square]]:
            """
            # ACTION:
            1.  If the collider_candidates is null or the wrong type send the exception in the SearchResult.
            2.  If the context fails validation send the exception in the SearchResult. Else, route to the
                search method which matches the context key.
            3.  The search method returns either an empty result or a list of squares. Any exceptions were caught earlier
                by the search router.
           # PARAMETERS:
                *   collider_candidates (List[Square]):
                *   context: SquareContext
                *   context_validator: SquareContextValidator
            # RETURNS:
                *   SearchResult[List[Square]] containing either:
                        - On error: Exception , payload null
                        - On finding a match: List[Tokem] in the payload.
                        - On no matches found: Exception null, payload null
            Raises:
                *   TypeError
                *   SquareNullDatasetException
                *   SquareSearchException
            """
            method = "SquareFinder.find"
            
            if query_validator is None:
                query_validator = SquareQueryValidator()
            
            # Handle the case that, the collider_candidates is null.
            if dataset is None:
                # Send the exception chain on failure.
                return SearchResult.failure(
                    SquareSearchException(
                        msg=f"{method}: {SquareSearchException.ERR_CODE}",
                        ex=SquareSearchDatasetNullException(f"{method}: {SquareSearchDatasetNullException.MSG}")
                    )
                )
            # Handle the case that, collider_candidates is the wrong type
            if not isinstance(dataset, List):
                # Send the exception chain on failure.
                return SearchResult.failure(
                    SquareSearchException(
                        msg=f"{method}: {SquareSearchException.ERR_CODE}",
                        ex=TypeError(f"{method}: Expected List[Square], got {type(dataset).__name__} instead.")
                    )
                )
            
            # --- Route to the search method which matches the context key. ---#
            
            # Entry point into searching by square's id.
            if query.context.id is not None:
                return cls._find_by_id(dataset=query.stack, id=query.context.id)
            
            # Entry point into searching by arena square is playing in.
            if query.context.name is not None:
                return cls._find_by_name(dataset=query.stack, name=query.context.name)
            
            # Entry point into searching by square's board.
            if query.context.board is not None:
                return cls._find_by_board(dataset=query.stack, board=query.context.board)
            
            # Entry point into searching by square's coord.
            if query.context.coord is not None:
                return cls._find_by_coord(dataset=query.stack, coord=query.context.coord)
            
            # Entry point into searching by square's occupant.
            if query.context.occupant is not None:
                return cls._find_by_occupant(dataset=query.stack, occupant=query.context.occupant)
            
            # Entry point into searching by opening square's formation.
            if query.context.formation is not None:
                return cls._find_by_formation(dataset=query.stack, coord=query.context.formation)
            
            # Entry point into searching by opening square's state.
            if query.context.state is not None:
                return cls._find_by_formation(dataset=query.stack, coord=query.context.state)
            
            # The default path is only reached when a context.key does not have a search route. Return
            # the exception chain.
            return SearchResult.failure(
                SquareSearchException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareSearchException.MSG,
                    err_code=SquareSearchException.ERR_CODE,
                    ex=SquareSearchRouteException(f"{method}: {SquareSearchRouteException.ERR_CODE}")
                )
            )
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_id(cls, dataset: List[Square], id: int) -> SearchResult[List[Square]]:
            """
            Find squares which match the id. There should only be one.
            """
            matches = [square for square in dataset if square.id == id]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_name(cls, dataset: List[Square], name: str) -> SearchResult[List[Square]]:
            """
            Find squares which match the name. There should only be one.
            """
            matches = [square for square in dataset if square.name.upper()== name.upper()]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_board(cls, dataset: List[Square], board: Board) -> SearchResult[List[Square]]:
            """
            Find squares which match the board.
            """
            matches = [square for square in dataset if square.board == board]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)
        
        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_coord(cls, dataset: List[Square], coord: Coord) -> SearchResult[List[Square]]:
            """
            Find squares which match the coord. There should only be one.
            """
            matches = [square for square in dataset if square.coord == coord]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)

        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_occupant(cls, dataset: List[Square], occupant: Token) -> SearchResult[List[Square]]:
            """
            Find squares containing the occupant. There should only be one.
            """
            matches = [square for square in dataset if square.occupant == occupant]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)


        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_state(cls, dataset: List[Square], state: SquareState) -> SearchResult[List[Square]]:
            """
            Find squares containing the occupant. There should only be one.
            """
            matches = [square for square in dataset if square.state == state]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)

        @classmethod
        @LoggingLevelRouter.monitor
        def _find_by_formation(
                cls,
                dataset: List[Square],
                formation: Formation
        ) -> SearchResult[List[OpeningSquare]]:
            """
            Find OpeningSquare instances which match the formation. There should only be one.
            """
            matches = [
                square for square in dataset if (
                        isinstance(square, OpeningSquare) and 
                        square.formation == formation
                )
            ]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Only other case
            return SearchResult.success(payload=matches)