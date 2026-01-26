# src/chess/occupant/context/finder/finder.py

"""
Module: chess.occupant.context.finder.finder
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import List

from chess.rank import Rank
from chess.square import Square
from chess.team import Team
from chess.system import DataFinder, GameColor, LoggingLevelRouter, SearchResult
from chess.token import (
    Token, TokenContext, TokenContextValidator, TokenSearchNullDatasetException, TokenSearchFailedException,
    TokenSearchRouteException
)


class TokenFinder(DataFinder[Token]):
    """
    # ROLE: AbstractSearcher

    # RESPONSIBILITIES:
    1.  Send items in a TokenList whose attribute value match the context.key value to the caller.
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
            dataset: List[Token],
            context: TokenContext,
            context_validator: TokenContextValidator = TokenContextValidator()
    ) -> SearchResult[List[Token]]:
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
            *   TokenSearchFailedException
        """
        method = "TokenFinder.find"
        
        # Handle the case that the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenSearchFailedException(
                    message=f"{method}: {TokenSearchFailedException.ERROR_CODE}",
                    ex=TokenSearchNullDatasetException(
                        f"{method}: {TokenSearchNullDatasetException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that dataset is the wrong type
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenSearchFailedException(
                    message=f"{method}: {TokenSearchFailedException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected List[Token], got {type(dataset).__name__} instead.")
                )
            )
        # Handle the case that the context fails validation.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenSearchFailedException(
                    message=f"{method}: {TokenSearchFailedException.ERROR_CODE}",
                    ex=validation_result.exception
                )
            )
    
    # --- Route to the search method which matches the context key. ---#
        
        # Entry point into finding by occupant's id.
        if context.id is not None:
            return cls._find_by_id(dataset=dataset, id=context.id)
        # Entry point into finding by occupant's designation.
        if context.designation is not None:
            return cls._find_by_designation(dataset=dataset, name=context.designation)
        # Entry point into finding by occupant's opening_square.
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
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            TokenSearchFailedException(
                message=f"{method}: {TokenSearchFailedException.ERROR_CODE}",
                ex=TokenSearchRouteException(f"{method}: {TokenSearchRouteException.DEFAULT_MESSAGE}")
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
            *   dataset (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "TokenFinder._find_by_id"
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
            *   dataset (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "TokenFinder._find_by_designation"
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
            *   opening_square (Square)
            *   dataset (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "TokenFinder._find_by_opening_square"
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
            *   dataset (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "TokenFinder._find_by_team"
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
            *   dataset (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "TokenFinder._find_by_rank"
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
            *   dataset (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "TokenFinder._find_by_ransom"
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
            *   dataset (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Tokem] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        method = "TokenFinder._find_by_color"
        matches = [token for token in dataset if token.team.schema.color == color]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)