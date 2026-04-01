# src/logic/token/database/search/route/model/router.py

"""
Module: logic.token.database.search.route.model.router
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.rank import Rank
from logic.team import Team
from logic.system import GameColor, LoggingLevelRouter, SearchResult, StackSearchRouter
from logic.token import (
    Token, TokenContext, TokenQueryParamsValidator, MissingTokenSearchRouteException,
    TokenSearchRouterException
)


class TokenSearchRouter(StackSearchRouter[Token]):
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
            dataset: List[Token],
            context: TokenContext,
            params_validator: TokenQueryParamsValidator = TokenQueryParamsValidator(),
    ) -> SearchResult[List[Token]]:
        """
        Find tokens whith an attribute that fits the context.
        
        Action:
            1.  Send an exception chain in the SearchResult if either:
                    -   The params check fails.
                    -   There is no search logic for the context
            2.  Otherwise, send the success result.
        Args:
            dataset: List[Token],
            context: TokenContext,
            params_validator: TokenQueryParamsValidator
        Returns:
            SearchResult[List[Token]]
        Raises:
            TokenSearchRouterException
            MissingTokenSearchRouteException
        """
        method = f"{cls.__name__}.route"

        # Handle the case that, a routing param does not pass a check.
        validation_result = params_validator.validate(
            context=context,
            dataset=dataset,
        )
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                TokenSearchRouterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenSearchRouterException.MSG,
                    err_code=TokenSearchRouterException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
    # --- Route to the search method which matches the query key. ---#
        
        # Entry point into finding by occupant's id.
        if context.id is not None:
            return cls._find_by_id(
                dataset=dataset,
                id=context.id
            )
        # Entry point into finding by occupant's designation.
        if context.designation is not None:
            return cls._find_by_designation(
                dataset=dataset,
                name=context.designation
            )
        # Entry point into finding by occupant's opening_square_name_name.
        if context.opening_square_name is not None:
            return cls._find_by_opening_square_name(
                dataset=dataset,
                name=context.opening_square_name
            )
        # Entry point into finding by occupant's team.
        if context.team is not None:
            return cls._find_by_team(
                dataset=dataset,
                team=context.team
            )
        # Entry point into searching by toke's rank.
        if context.rank is not None:
            return cls._find_by_rank(
                dataset=dataset,
                team=context.rank
            )
        # Entry point into searching by occupant's ransom.
        if context.ransom is not None:
            return cls._find_by_ransom(
                dataset=dataset,
                ransom=context.ransom
            )
        # Entry point into searching by occupant's color.
        if context.ransom is not None:
            return cls._find_by_color(
                dataset=dataset,
                ransom=context.color
            )
        # If a query does not have a search route defined send an exception chain.
        return SearchResult.failure(
            TokenSearchRouterException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=TokenSearchRouterException.MSG,
                err_code=TokenSearchRouterException.ERR_CODE,
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
            dataset: List[Token],
            id: int
    ) -> SearchResult[List[Token]]:
        """
        Search the dataset by a token id
            1.  Get the Tokens with the desired id.
        Args::
            id: int
            dataset: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises:
        """
        matches = [token for token in dataset if token.id == id]
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
        Search the dataset by a token id
        
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
            dataset: List[Token],
            opening_square_name: str
    ) -> SearchResult[List[Token]]:
        """
        Search the dataset by a opening square's name'

        Args:
            opening_square_name: str
            dataset: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in dataset if
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
            dataset: List[Token],
            team: Team
    ) -> SearchResult[List[Token]]:
        """
        Search the dataset by a team.

        Args:
            team: Team
            dataset: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in dataset if token.team == team
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
            dataset: List[Token],
            rank: Rank
    ) -> SearchResult[List[Token]]:
        """
        Search the dataset by a rank.

        Args:
            rank: Rank
            dataset: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in dataset if token.rank == rank
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
        Search the dataset by a random.

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
            dataset: List[Token],
            color: GameColor
    ) -> SearchResult[List[Token]]:
        """
        Search the dataset by a random.

        Args:
            color: GameColor
            dataset: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises
        """
        matches = [
            token for token in dataset if token.team.schema.color == color
        ]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)