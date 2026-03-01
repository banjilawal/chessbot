# src/logic/hostage/context/finder/finder.py

"""
Module: logic.hostage.context.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List

from logic.square import Square
from logic.system import DataFinder, LoggingLevelRouter, SearchResult
from logic.hostage import (
    CaptivityContext, CaptivityContextValidator, Hostage, HostageSearchException,
    HostageSearchNullDatasetException, HostageSearchPayloadTypeException,
    HostageSearchRouteException
)
from logic.token import CombatantToken, Token


class HostageFinder(DataFinder[Hostage]):
    """
    # ROLE: SearchWorker

    # RESPONSIBILITIES:
    1.  Send bag in a HostageList whose attribute value match the context.key value to the caller.
    2.  If a search does not complete forward the exception chain to the caller for debugging.

    # LIMITATIONS:
    1.  HostageFinder sends the raw list of matches. Resolving id collisions is the caller's responsibility.

    # PARENT
        *   SearchWorker

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
            dataset: List[Hostage],
            context: CaptivityContext,
            context_validator: CaptivityContextValidator = CaptivityContextValidator()
    ) -> SearchResult[List[Hostage]]:
        """
        # ACTION:
        1.  If the dataset is null or the wrong type send the exception in the SearchResult.
        2.  If the context fails validation send the exception in the SearchResult. Else, route to the 
            search method which matches the context key.
        3.  The search method returns either an empty result or a list of hostages. Any exceptions were caught earlier
            by the search router.
       # PARAMETERS:
            *   dataset (List[Hostage]):
            *   context: CaptivityContext
            *   context_validator: CaptivityContextValidator
        # RETURNS:
            *   SearchResult[List[Hostage]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Hostage] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   HostageSearchPayloadTypeException
            *   HostageNullDatasetException
            *   HostageSearchException
        """
        method = "HostageFinder.find"
        
        # Handle the case that, the dataset is null.
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                HostageSearchException(
                    msg=f"{method}: {HostageSearchException.ERR_CODE}",
                    ex=HostageSearchNullDatasetException(
                        f"{method}: {HostageSearchNullDatasetException.MSG}"
                    )
                )
            )
        # Handle the case that, dataset is the wrong type
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                HostageSearchException(
                    msg=f"{method}: {HostageSearchException.ERR_CODE}",
                    ex=HostageSearchPayloadTypeException(
                        f"{method}: {HostageSearchPayloadTypeException.MSG}"
                    )
                )
            )
        # Handle the case that, the context fails validation.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                HostageSearchException(
                    msg=f"{method}: {HostageSearchException.ERR_CODE}",
                    ex=validation_result.exception
                )
            )
        # --- Route to the search method which matches the context key. ---#
        
        # Entry point into finding by hostage's id.
        if context.id is not None:
            return cls._find_by_id(dataset=dataset, id=context.id)
        # Entry point into finding by the prisoner.
        if context.prisoner is not None:
            return cls._find_by_prisoner(dataset=dataset, prisoner=context.prisoner)
        # Entry point into finding by victor.
        if context.victor is not None:
            return cls._find_by_victor(dataset=dataset, coord=context.victor)
        # Entry point into searching by captured item.
        if context.captured_square is not None:
            return cls._find_by_captured_square(dataset=dataset, coord=context.captured_square)
        
        # If a context does not have a search route defined send an exception chain.
        return SearchResult.failure(
            HostageSearchException(
                msg=f"{method}: {HostageSearchException.ERR_CODE}",
                ex=HostageSearchRouteException(f"{method}: {HostageSearchRouteException.MSG}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Hostage], id: int) -> SearchResult[List[Hostage]]:
        """
        # ACTION:
            1.  Get the Hostages with the desired id.
        # PARAMETERS:
            *   id (int)
            *   dataset (List[Hostage])
        # RETURNS:
            *   SearchResult[List[Hostage]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Hostage] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            None
        """
        matches = [hostage for hostage in dataset if hostage.id == id]
        # Handle the nothing found case.
        if len(matches) == 0:
            return SearchResult.empty()
        # Only other case
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_prisoner(
            cls,
            dataset: List[Hostage],
            prisoner: CombatantToken
    ) -> SearchResult[List[Hostage]]:
        """
        # ACTION:
            1.  Get the Hostages which match the name.
        # PARAMETERS:
            *   name (str)
            *   dataset (List[Hostage])
        # RETURNS:
            *   SearchResult[List[Hostage]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Hostage] in the payload.
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
            dataset: List[Hostage],
            victor: Token
    ) -> SearchResult[List[Hostage]]:
        """
        # ACTION:
            1.  Get the Hostages which match the name.
        # PARAMETERS:
            *   coord (Coord)
            *   dataset (List[Hostage])
        # RETURNS:
            *   SearchResult[List[Hostage]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Hostage] in the payload.
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
            dataset: List[Hostage],
            captured_square: Square
    ) -> SearchResult[List[Hostage]]:
        """
        # ACTION:
            1.  Get the Hostages which match the board.
        # PARAMETERS:
            *   board (Board)
            *   dataset (List[Hostage])
        # RETURNS:
            *   SearchResult[List[Hostage]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Hostage] in the payload.
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