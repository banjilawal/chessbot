# src/chess/hostage/context/finder/finder.py

"""
Module: chess.hostage.context.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List

from chess.square import Square
from chess.system import DataFinder, LoggingLevelRouter, SearchResult
from chess.hostage import (
    CaptivityContext, CaptivityContextValidator, HostageManifest,
    HostageManifestSearchFailedException, HostageManifestSearchNullDatasetException,
    HostageManifestSearchPayloadTypeException, HostageManifestSearchRouteException
)
from chess.token import CombatantToken, Token


class HostageManifestFinder(DataFinder[HostageManifest]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Send items in a HostageManifestList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.

    # LIMITATIONS:
    1.  HostageManifestFinder sends the raw list of matches. Resolving id collisions is the caller's responsibility.

    # PARENT
        *   Finder

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
            dataset: List[HostageManifest],
            context: CaptivityContext,
            context_validator: CaptivityContextValidator = CaptivityContextValidator()
    ) -> SearchResult[List[HostageManifest]]:
        """
        # ACTION:
        1.  If the dataset is null or the wrong type send the exception in the SearchResult.
        2.  If the context fails validation send the exception in the SearchResult. Else, route to the 
            search method which matches the context key.
        3.  The search method returns either an empty result or a list of hostageManifests. Any exceptions were caught earlier
            by the search router.
       # PARAMETERS:
            *   dataset (List[HostageManifest]):
            *   context: CaptivityContext
            *   context_validator: CaptivityContextValidator
        # RETURNS:
            *   SearchResult[List[HostageManifest]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[HostageManifest] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   HostageManifestSearchPayloadTypeException
            *   HostageManifestNullDatasetException
            *   HostageManifestSearchFailedException
        """
        method = "HostageManifestFinder.find"
        
        # Handle the case that the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                HostageManifestSearchFailedException(
                    message=f"{method}: {HostageManifestSearchFailedException.ERROR_CODE}",
                    ex=HostageManifestSearchNullDatasetException(
                        f"{method}: {HostageManifestSearchNullDatasetException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that dataset is the wrong type
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                HostageManifestSearchFailedException(
                    message=f"{method}: {HostageManifestSearchFailedException.ERROR_CODE}",
                    ex=HostageManifestSearchPayloadTypeException(
                        f"{method}: {HostageManifestSearchPayloadTypeException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the context fails validation.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                HostageManifestSearchFailedException(
                    message=f"{method}: {HostageManifestSearchFailedException.ERROR_CODE}",
                    ex=validation_result.exception
                )
            )
        # --- Route to the search method which matches the context key. ---#
        
        # Entry point into finding by hostageManifest's id.
        if context.id is not None:
            return cls._find_by_id(dataset=dataset, id=context.id)
        # Entry point into finding by the prisoner.
        if context.prisoner is not None:
            return cls._find_by_prisoner(dataset=dataset, prisoner=context.prisoner)
        # Entry point into finding by victor.
        if context.victor is not None:
            return cls._find_by_victor(dataset=dataset, coord=context.victor)
        # Entry point into searching by captured square.
        if context.captured_square is not None:
            return cls._find_by_captured_square(dataset=dataset, coord=context.captured_square)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            HostageManifestSearchFailedException(
                message=f"{method}: {HostageManifestSearchFailedException.ERROR_CODE}",
                ex=HostageManifestSearchRouteException(f"{method}: {HostageManifestSearchRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[HostageManifest], id: int) -> SearchResult[List[HostageManifest]]:
        """
        # ACTION:
            1.  Get the HostageManifests with the desired id.
        # PARAMETERS:
            *   id (int)
            *   dataset (List[HostageManifest])
        # RETURNS:
            *   SearchResult[List[HostageManifest]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[HostageManifest] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [hostageManifest for hostageManifest in dataset if hostageManifest.id == id]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_prisoner(
            cls,
            dataset: List[HostageManifest],
            prisoner: CombatantToken
    ) -> SearchResult[List[HostageManifest]]:
        """
        # ACTION:
            1.  Get the HostageManifests which match the name.
        # PARAMETERS:
            *   name (str)
            *   dataset (List[HostageManifest])
        # RETURNS:
            *   SearchResult[List[HostageManifest]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[HostageManifest] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [manifest for manifest in dataset if manifest.prisoner == prisoner]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_victor(
            cls,
            dataset: List[HostageManifest],
            victor: Token
    ) -> SearchResult[List[HostageManifest]]:
        """
        # ACTION:
            1.  Get the HostageManifests which match the name.
        # PARAMETERS:
            *   coord (Coord)
            *   dataset (List[HostageManifest])
        # RETURNS:
            *   SearchResult[List[HostageManifest]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[HostageManifest] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [manifest for manifest in dataset if manifest.victor == victor]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_captured_square(
            cls,
            dataset: List[HostageManifest],
            captured_square: Square
    ) -> SearchResult[List[HostageManifest]]:
        """
        # ACTION:
            1.  Get the HostageManifests which match the board.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[HostageManifest])
        # RETURNS:
            *   SearchResult[List[HostageManifest]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[HostageManifest] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [manifest for manifest in dataset if manifest.captured_square == captured_square]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)