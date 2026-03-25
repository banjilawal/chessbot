# src/logic/token/query/route/route.py

"""
Module: logic.token.query.route.route
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import List

from logic.rank import Rank
from logic.square import Square
from logic.team import Team
from logic.system import DataFinder, GameColor, LoggingLevelRouter, SearchResult
from logic.token import (
    Token, TokenContext, TokenContextValidationProcess, TokenSearchNullDatasetException, TokenSearchException,
    TokenSearchRouteException
)


class TokenSearchRouter(DataFinder[Token]):
    """
    Role:SearchProcess

    Responsibilities:
    1.  Send bag in a TokenList whose attribute value match the query.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.
    
    # LIMITATIONS:
    1.  TokenSearchRouter sends the raw list of matches. Resolving id collisions is the caller's responsibility.

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
            dataset: List[Token],
            context: TokenContext,
            context_validator: TokenContextValidationProcess = TokenContextValidationProcess()
    ) -> SearchResult[List[Token]]:
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
        method = "TokenSearchRouter.find"
        
        # Handle the case that, the collider_candidates is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenSearchException(
                    msg=f"{method}: {TokenSearchException.ERR_CODE}",
                    ex=TokenSearchNullDatasetException(
                        f"{method}: {TokenSearchNullDatasetException.MSG}"
                    )
                )
            )
        # Handle the case that, collider_candidates is the wrong type
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenSearchException(
                    msg=f"{method}: {TokenSearchException.ERR_CODE}",
                    ex=TypeError(f"{method}: Expected List[Token], got {type(dataset).__name__} instead.")
                )
            )
        # Handle the case that, the query fails validation.
        validation_result = context_validator.execute(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenSearchException(
                    msg=f"{method}: {TokenSearchException.ERR_CODE}",
                    ex=validation_result.exception
                )
            )
    
    # --- Route to the search method which matches the query key. ---#
        
        # Entry point into finding by occupant's id.
        if context.id is not None:
            return cls._find_by_id(dataset=dataset, id=context.id)
        # Entry point into finding by occupant's designation.
        if context.designation is not None:
            return cls._find_by_designation(dataset=dataset, name=context.designation)
        # Entry point into finding by occupant's opening_square_name.
        if context.opening_square is not None:
            return cls._find_by_opening_square(dataset=dataset, name=context.opening_square)
        # Entry point into finding by occupant's team.
        if context.team is not None:
            return cls._find_by_team(dataset=dataset, team=context.team)
        # Entry point into searching by toke's rank.
        if context.rank is not None:
            return cls._find_by_rank(dataset=dataset, team=context.rank)
        # Entry point into searching by occupant's ransom.
        if context.ransom is not None:
            return cls._find_by_ransom(dataset=dataset, ransom=context.ransom)
        # Entry point into searching by occupant's color.
        if context.ransom is not None:
            return cls._find_by_color(dataset=dataset, ransom=context.color)
        
        # If a query does not have a search route defined send an exception chain.
        return SearchResult.failure(
            TokenSearchException(
                msg=f"{method}: {TokenSearchException.ERR_CODE}",
                ex=TokenSearchRouteException(f"{method}: {TokenSearchRouteException.MSG}")
            )
        )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Token], id: int) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the Tokens with the desired id.
        # PARAMETERS:
            *   id (int)
            *   collider_candidates (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "TokenSearchRouter._find_by_id"
        matches = [token for token in dataset if token.id == id]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)

    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_designation(cls, dataset: List[Token], designation: str) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the Tokens which match the designation.
        # PARAMETERS:
            *   designation (str)
            *   collider_candidates (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "TokenSearchRouter._find_by_designation"
        matches = [token for token in dataset if token.designation.upper() == designation.upper()]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_opening_square(cls, dataset: List[Token], opening_square: Square) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the Tokens which match the designation.
        # PARAMETERS:
            *   opening_square_name (Square)
            *   collider_candidates (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "TokenSearchRouter._find_by_opening_square"
        matches = [token for token in dataset if token.opening_square == opening_square]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_team(cls, dataset: List[Token], team: Team) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the Tokens which match the designation.
        # PARAMETERS:
            *   team (Team)
            *   collider_candidates (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "TokenSearchRouter._find_by_team"
        matches = [token for token in dataset if token.team == team]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_rank(cls, dataset: List[Token], rank: Rank) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the Tokens which match the rank.
        # PARAMETERS:
            *   rank (Rank)
            *   collider_candidates (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "TokenSearchRouter._find_by_rank"
        matches = [token for token in dataset if token.rank == rank]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_ransom(cls, dataset: List[Token], ransom: int) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the Tokens which match the rank.
        # PARAMETERS:
            *   ransom (int)
            *   collider_candidates (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "TokenSearchRouter._find_by_ransom"
        matches = [token for token in dataset if token.rank.ransom == ransom]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_color(cls, dataset: List[Token], color: GameColor) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the Tokens which match the color.
        # PARAMETERS:
            *   color (int)
            *   collider_candidates (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        Raises:
            None
        """
        method = "TokenSearchRouter._find_by_color"
        matches = [token for token in dataset if token.team.schema.color == color]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)