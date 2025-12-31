# src/chess/token/context/finder/finder.py

"""
Module: chess.token.context.finder.finder
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import List

from chess.system import DataFinder, LoggingLevelRouter, SearchResult
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
    
        
        # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
        SearchResult.failure(
            TokenSearchRouteException(f"{method}: {TokenSearchRouteException.DEFAULT_MESSAGE}")
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Token], id: int) -> SearchResult[List[Token]]:
        """
        # ACTION:
        1.  Get the Token with the desired id.
        2.  An id search should produce either no hits or one hit only.
        3.  Multiple unique tokens in the result indicate that  a problem.

        # PARAMETERS:
            *   id (int)
            *   dataset (List[Token])

        # RETURNS:
        SearchResult[List[Token]] containing either:
            - On success: List[token] in the payload.
            - On failure: Exception.

        # RAISES:
            *   TokenFinderException
        """
        method = "TokenFinder._find_by_id"
        try:
            # IDs are unique the search should either produce no result or one unique.
            matches = [token for token in dataset if token.id == id]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits. The restriction that: if match_count > 1 ==> Error is relaxed.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, dataset: List[Token], name: str) -> SearchResult[List[Token]]:
        """
        # ACTION:
        1.  Get the Token with the desired designation.
        2.  A designation search should produce either no hits or one hit only.
        3.  Multiple unique tokens in the result indicate that  a problem.

        # PARAMETERS:
            *   name (str)
            *   dataset (List[Token])

        # RETURNS:
        SearchResult[List[Token]] containing either:
            - On success: List[token] in the payload.
            - On failure: Exception.

        # RAISES:
            *   TokenFinderException
        """
        method = "TokenFinder._find_by_name"
        try:
            # Names are unique the search should either produce no result or one unique.
            matches = [ token for token in dataset if token.name.upper() == name.upper()]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits. The restriction that: if match_count > 1 ==> Error is relaxed.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
                
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_team(cls, dataset: List[Token], team: Team) -> SearchResult[List[Token]]:
        """
        # ACTION:
        1.  Get Tokens on the desired team.

        # PARAMETERS:
            *   team (Team)
            *   dataset (List[Token])

        # RETURNS:
        SearchResult[List[Token]] containing either:
            - On success: List[token] in the payload.
            - On failure: Exception.

        # RAISES:
            *   TokenFinderException
        """
        method = "TokenFinder._find_by_team"
        try:
            matches = [token for token in dataset if token.team == team]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_rank(cls, dataset: List[Token], rank: Rank) -> SearchResult[List[Token]]:
        """
        # ACTION:
        1.  Get Tokens of the desired rank.

        # PARAMETERS:
            *   rank (Rank)
            *   dataset (List[Token])

        # RETURNS:
        SearchResult[List[Token]] containing either:
            - On success: List[token] in the payload.
            - On failure: Exception.

        # RAISES:
            *   TokenFinderException
        """
        method = "TokenFinder._find_by_rank"
        try:
            matches = [token for token in dataset if token.rank == rank]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_ransom(cls, dataset: List[Token], ransom: int) -> SearchResult[List[Token]]:
        """
        # ACTION:
        1.  Get Tokens with the desired ransom.

        # PARAMETERS:
            *   ransom (int)
            *   dataset (List[Token])

        # RETURNS:
        SearchResult[List[Token]] containing either:
            - On success: List[token] in the payload.
            - On failure: Exception.

        # RAISES:
            *   TokenFinderException
        """
        method = "TokenFinder._find_by_rank"
        try:
            matches = [token for token in dataset if token.rank.ransom == ransom]
            # Handle the nothing found case.
            if len(matches) == 0:
                return SearchResult.empty()
            # Handle the case with successful hits.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )