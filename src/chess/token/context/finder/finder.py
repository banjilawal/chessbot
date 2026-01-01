# src/chess/token/context/finder/finder.py

"""
Module: chess.token.context.finder.finder
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import List

from chess.rank import Rank
from chess.system import DataFinder, GameColor, LoggingLevelRouter, SearchResult
from chess.team import Team
from chess.token import (
    Token, TokenContext, TokenContextValidator, TokenSearchDatasetNullException, TokenSearchFailedException,
    TokenSearchRouteException
)


class TokenFinder(DataFinder[Token]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Search Token collections for items which match the attribute target specified in the TokenContext parameter.
    2.  Safely forward any errors encountered during a search to the caller.

    # PARENT
        *   Finder

    # PROVIDES:
        *   find: -> SearchResult[List[Token]]

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
        1.  Verify the dataset is not null and contains only Token objects,
        2.  Use context_validator to certify the provided map.
        3.  Context attribute routes the search. Attribute value is the search target.
        4.  The outcome of the search is sent back to the caller in a SearchResult object.

        # PARAMETERS:
            *   dataset (List[Token]):
            *   map: TokenContext
            *   context_validator: TokenContextValidator

        # RETURNS:
        SearchResult[List[Token]] containing either:
            - On success: List[token] in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   TokenNullDatasetException
            *   TokenFinderException
        """
        method = "TokenFinder.find"
        
        # Handle the case that the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenSearchFailedException(
                    message=f"{method}: {TokenSearchFailedException.ERROR_CODE}",
                    ex=TokenSearchDatasetNullException(
                        f"{method}: {TokenSearchDatasetNullException.DEFAULT_MESSAGE}"
                    )
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
    
    # --- Route to the appropriate search method by the context flag. ---#
        
        # Entry point into finding by token's id.
        if context.id is not None:
            return cls._find_by_id(dataset=dataset, id=context.id)
        # Entry point into finding by token's designation.
        if context.name is not None:
            return cls._find_by_designation(dataset=dataset, name=context.designation)
        # Entry point into fiding by token's team.
        if context.team is not None:
            return cls._find_by_team(dataset=dataset, team=context.team)
        # Entry point into searching by toke's rank.
        if context.rank is not None:
            return cls._find_by_rank(dataset=dataset, team=context.rank)
        # Entry point into searching by token's ransom.
        if context.ransom is not None:
            return cls._find_by_ransom(dataset=dataset, ransom=context.ransom)
        # Entry point into searching by token's color.
        if context.ransom is not None:
            return cls._find_by_color(dataset=dataset, ransom=context.color)
            
        # The default path returns failure
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
                    - On failure: Exception.
                    - On success: List[token] in the payload.
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
                    - On failure: Exception.
                    - On success: List[token] in the payload.
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
    def _find_by_team(cls, dataset: List[Token], team: Team) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the Tokens which match the designation.
        # PARAMETERS:
            *   team (Team)
            *   dataset (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On failure: Exception.
                    - On success: List[token] in the payload.
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
                    - On failure: Exception.
                    - On success: List[token] in the payload.
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
                    - On failure: Exception.
                    - On success: List[token] in the payload.
        # RAISES:
            None
        """
        method = "TokenFinder._find_by_ransom"
        matches = [token for token in dataset if token.rank.persona.ransom == ransom]
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
            *   ransom (int)
            *   dataset (List[Token])
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On failure: Exception.
                    - On success: List[token] in the payload.
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