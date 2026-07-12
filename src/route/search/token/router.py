# src/route/search/token/orange.py

"""
Module: route.search.token.orange
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from err import TokenSearcherException, TokenSearchRouteException
from model import Coord, HomeSquare, Rank, Team, Token
from model.query import TokenQuery
from result import SearchResult
from route import SearchRouter
from searcher import TokenQueryValidator
from system import LoggingLevelRouter


class TokenSearchRouter(SearchRouter[Token]):
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
            query: TokenQuery,
    ) -> SearchResult[List[Token]]:
        """
        Find tokens whith an attribute that fits the context.
        
        Action:
            1.  Send an exception chain in the SearchResult if either:
                    -   The params check fails.
                    -   There is no search logic for the context
            2.  Otherwise, send the success result.
        Args:
            query: TokenQuery,
            query_validator: TokenQueryValidator,
        Returns:
            SearchResult[List[Token]]
        Raises:
            TokenSearchException
            MissingTokenSearchRouteException
        """
        method = f"{cls.__name__}.route"
        # --- Route to the search method which matches the context key. ---#
        
        # token.id search entry point.
        if query.context.id is not None:
            return cls._find_by_id(
                items=query.token_stack.items,
                id=query.context.id
            )
        # token.designation search entry point
        if query.context.name is not None:
            return cls._find_by_designation(
                items=query.token_stack.items,
                designation=query.context.name
            )
        # token.home_square_name search entry point.
        if query.context.home_square is not None:
            return cls._find_by_home_square_name(
                items=query.token_stack.items,
                home_square=query.context.home_square
            )
        # token.team search entry point.
        if query.context.team is not None:
            return cls._find_by_team(
                items=query.token_stack.items,
                team=query.context.team
            )
        # token.rank search entry point.
        if query.context.rank_level is not None:
            return cls._find_by_rank(
                items=query.token_stack,
                team=query.context.rank_level
            )
        # token.ransom search entry point.
        if query.context.ransom is not None:
            return cls._find_by_ransom(
                items=query.token_stack.items,
                ransom=query.context.ransom
            )
        # token.color search entry point.
        if query.context.ransom is not None:
            return cls._find_by_color(
                items=query.token_stack.items,
                ransom=query.context.color
            )
        # token.current_position search entry point.
        if query.context.ransom is not None:
            return cls._find_by_current_position(
                items=query.token_stack.items,
                ransom=query.context.current_position
            )
        # Handle the case that, there is no search path for the context context..
        return SearchResult.failure(
            TokenSearcherException(
                cls_mthd=method,
                cls_name=cls.__name__,
                op=TokenSearcherException.OP,
                msg=TokenSearcherException.MSG,
                err_code=TokenSearcherException.ERR_CODE,
                mthd_rslt_type=TokenSearcherException.MTHD_RSLT,
                ex=TokenSearchRouteException(
                    msg=TokenSearchRouteException.MSG,
                    err_code=TokenSearchRouteException.ERR_CODE,
                )
            )
        )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(
            cls,
            items: List[Token],
            id: int
    ) -> SearchResult[List[Token]]:
        """
        Search the schema by a token id
        
            1.  Get the Tokens with the desired id.
        Args:
            id: int
            items: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises:
        """
        matches = [token for token in items if token.id == id]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(matches)

    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_designation(
            cls,
            items: List[Token],
            designation: str
    ) -> SearchResult[List[Token]]:
        """
        Search the schema by a token id
        
        Args:
            designation: str
            items: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in items if
                (token.name.upper() == designation.upper())
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_home_square(
            cls,
            items: List[Token],
            home_square: HomeSquare,
    ) -> SearchResult[List[Token]]:
        """
        Search the schema by a opening square's schema'

        Args:
            home_square: OpeningSquare
            items: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [token for token in items if token.home_square == home_square]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_team(
            cls,
            items: List[Token],
            team: Team
    ) -> SearchResult[List[Token]]:
        """
        Search the schema by a team.

        Args:
            team: Team
            items: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [token for token in items if token.team == team]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_rank(
            cls,
            items: List[Token],
            rank: Rank
    ) -> SearchResult[List[Token]]:
        """
        Search the schema by a rank.

        Args:
            rank: Rank
            items: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [token for token in items if token.rank == rank]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_ransom(
            cls,
            dataset: List[Token],
            ransom: int
    ) -> SearchResult[List[Token]]:
        """
        Search the schema by a random.

        Args:
            ransom: int
            dataset: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in dataset if token.rank.persona.ransom == ransom
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_color(
            cls,
            stack: List[Token],
            color: GameColor
    ) -> SearchResult[List[Token]]:
        """
        Search the schema by a random.

        Args:
            color: GameColor
            stack: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in stack if token.team.schema.color == color
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_current_position(
            cls,
            stack: List[Token],
            current_position: Coord
    ) -> SearchResult[List[Token]]:
        """
        Search the schema by a random.

        Args:
            current_position: Coord
            stack: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in stack if token.current_position == current_position
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)