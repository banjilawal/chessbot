# src/chess/game/finder/finder

"""
Module: chess.game.finder.finder
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""



from typing import List

from chess.agent import PlayerAgent
from chess.game import Game, GameContext, GameContextValidator
from chess.system import (
    DataFinder, UnhandledRouteException, LoggingLevelRouter, SearchFailedException, SearchResult
)



class GameFinder(DataFinder[Game]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Search Game collections for items which match the attribute target specified in the GameContext parameter.
    2.  Safely forward any errors encountered during a search to the caller.

    # PARENT:
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
            dataset: List[Game],
            context: GameContext,
            context_validator: GameContextValidator = GameContextValidator()
    ) -> SearchResult[List[Game]]:
        """
        # Action:
        1.  Verify the dataset is not null and contains only Game objects,
        2.  Use context_validator to certify the provided map.
        3.  Context attribute routes the search. Attribute value is the search target.
        4.  The outcome of the search is sent back to the caller in a SearchResult object.

        # Parameters:
            *   dataset (List[Game]):
            *   map: GameContext
            *   context_validator: GameContextValidator

        # Returns:
        SearchResult[List[Game]] containing either:
            - On finding a match: List[Game] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   TypeError
            *   GameNullDatasetException
            *   GameFinderOperationFailedException
        """
        method = "GameFinder.find"
        try:
            # Don't want to run a search if the dataset is null.
            if dataset is None:
                return SearchResult.failure(
                    GameSearchDatasetNullException(f"{method}: {GameSearchDatasetNullException.DEFAULT_MESSAGE}")
                )
            # certify the map is safe.
            validation_result = context_validator.validate(context)
            if validation_result.is_failure:
                return SearchResult.failure(validation_result.exception)
            # After map is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by game id.
            if context.id is not None:
                return cls._find_by_id(dataset, context.id)
            # Entry point into searching by game player.
            if context.agent is not None:
                return cls._find_by_agent(dataset, context.agent)
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            SearchResult.failure(
                UnhandledRouteException(f"{method}: {UnhandledRouteException.DEFAULT_MESSAGE}")
            )
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: List[Game], id: int) -> SearchResult[List[Game]]:
        """
        # Action:
        1.  Get the Game with the matching id.
        2.  If no match is found return an exception.
        3.  An id search should produce either no hits or one hit only.
        4.  Multiple unique agents in the result indicate that  a problem.

        # Parameters:
            *   id (int)
            *   dataset (List[Game])

        # Returns:
        SearchResult[List[Game]] containing either:
            - On finding a match: List[Game] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   GameFinderOperationFailedException
        """
        method = "GameFinder._find_by_id"
        try:
            matches = [game for game in dataset if game.id == id]
            # There should be either no Games with the id or one and only one Game will have that id.
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
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
    def _find_by_agent(cls, dataset: [Game], agent: PlayerAgent) -> SearchResult[List[Game]]:
        """
        # Action:
        1.  Get the Game with the matching player-player_agent.
        2.  If no match is found return an exception.
        3.  An id search should produce either no hits or one hit only.

        # Parameters:
            *   player_agent (PlayerAgent)
            *   dataset (List[PlayerAgent])

        # Returns:
        SearchResult[List[Game]] containing either:
            - On finding a match: List[Game] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # Raises:
            *   GameFinderOperationFailedException
        """
        method = "GameFinder._find_by_agent"
        try:
            matches = [game for game in dataset if agent in game.agents]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )