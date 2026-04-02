# src/logic/token/database/search/route/router.py

"""
Module: logic.token.database.search.route.router
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.rank import Rank
from logic.team import Team
from logic.system import GameColor, LoggingLevelRouter, SearchResult, SearchRouter
from logic.token import MissingTokenSearchRouteException, Token, TokenQuery, TokenQueryValidator, TokenSearchException


class TokenSearchRouter(SearchRouter[Token]):
    """
    Role:SearchRouter

    Responsibilities:
    1.  Send bag in a TokenList whose attribute value match the query.key value to the caller.
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
            query_validator:TokenQueryValidator = TokenQueryValidator(),
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

        # Handle the case that, the query does not pass a test.
        validation_result = query_validator.validate(query)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                TokenSearchException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenSearchException.OP,
                    msg=TokenSearchException.MSG,
                    err_code=TokenSearchException.ERR_CODE,
                    rslt_type=TokenSearchException.RSLT_TYPE,
                    ex=validation_result.exception
                )
            )
    # --- Route to the search method which matches the query key. ---#
        
        # token.id search entry point.
        if query.context.id is not None:
            return cls._find_by_id(
                stack=query.stack,
                id=query.context.id
            )
        # token.designation search entry point
        if query.context.designation is not None:
            return cls._find_by_designation(
                dataset=query.stack,
                stack=query.context.designation
            )
        # token.opening_square_name search entry point.
        if query.context.opening_square_name is not None:
            return cls._find_by_opening_square_name(
                stack=query.stack,
                name=query.context.opening_square_name
            )
        # token.team search entry point.
        if query.context.team is not None:
            return cls._find_by_team(
                stack=query.stack,
                team=query.context.team
            )
        # token.rank search entry point.
        if query.context.rank is not None:
            return cls._find_by_rank(
                stack=query.stack,
                team=query.context.rank
            )
        # token.ransom search entry point.
        if query.context.ransom is not None:
            return cls._find_by_ransom(
                stack=query.stack,
                ransom=query.context.ransom
            )
        # token.color search entry point.
        if query.context.ransom is not None:
            return cls._find_by_color(
                stack=query.stack,
                ransom=query.context.color
            )
        # Handle the case that, there is no search path for the query context..
        return SearchResult.failure(
            TokenSearchException(
                mthd=method,
                title=cls.__name__,
                op=TokenSearchException.OP,
                msg=TokenSearchException.MSG,
                err_code=TokenSearchException.ERR_CODE,
                rslt_type=TokenSearchException.RSLT_TYPE,
                ex=MissingTokenSearchRouteException(
                    msg=MissingTokenSearchRouteException.MSG,
                    err_code=MissingTokenSearchRouteException.ERR_CODE,
                )
            )
        )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(
            cls,
            stack: List[Token],
            id: int
    ) -> SearchResult[List[Token]]:
        """
        Search the stack by a token id
        
            1.  Get the Tokens with the desired id.
        Args:
            id: int
            stack: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises:
        """
        matches = [token for token in stack if token.id == id]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(matches)

    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_designation(
            cls,
            dataset: List[Token],
            designation: str
    ) -> SearchResult[List[Token]]:
        """
        Search the stack by a token id
        
        Args:
            designation: str
            dataset: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in dataset if
                (token.designation.upper() == designation.upper())
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_opening_square_name(
            cls,
            stack: List[Token],
            opening_square_name: str
    ) -> SearchResult[List[Token]]:
        """
        Search the stack by a opening square's stack'

        Args:
            opening_square_name: str
            stack: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in stack if
                (token.opening_square_name.upper() == opening_square_name.upper())
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_team(
            cls,
            stack: List[Token],
            team: Team
    ) -> SearchResult[List[Token]]:
        """
        Search the stack by a team.

        Args:
            team: Team
            stack: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in stack if token.team == team
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_rank(
            cls,
            stack: List[Token],
            rank: Rank
    ) -> SearchResult[List[Token]]:
        """
        Search the stack by a rank.

        Args:
            rank: Rank
            stack: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in stack if token.rank == rank
        ]
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
        Search the stack by a random.

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
        Search the stack by a random.

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