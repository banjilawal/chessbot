# src/chess/game/finder/finder

"""
Module: chess.game.finder.finder
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""



from typing import List

from chess.agent import PlayerAgent
from chess.game.finder import GameFinderException
from chess.system import LoggingLevelRouter, Finder, SearchResult
from chess.game import (
    Game, GameContext, GameContextValidator, GameNullDataSetException, GameDataServiceNullException
)


class GameFinder(Finder[Game]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Search Game collections for items which match the attribute target specified in the GameContext parameter.
    2.  Safely forward any errors encountered during a search to the caller.

    # PARENT:
        *   Finder

    # PROVIDES:
        *   GameFinder:

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            data_set: List[Game],
            context: GameContext,
            context_validator: GameContextValidator = GameContextValidator()
    ) -> SearchResult[List[Game]]:
        """
        # Action:
        1.  Verify the data_set is not null and contains only Game objects,
        2.  Use context_validator to certify the provided context.
        3.  Context attribute routes the search. Attribute value is the search target.
        4.  The outcome of the search is sent back to the caller in a SearchResult object.

        # Parameters:
            *   data_set (List[Game]):
            *   context: GameContext
            *   context_validator: GameContextValidator

        # Returns:
        SearchResult[List[Game]] containing either:
            - On success:   List[game] in the payload.
            - On failure:   Exception.

        # Raises:
            *   TypeError
            *   GameNullDataSetException
            *   GameFinderException
        """
        method = "GameFinder.find"
        try:
            # Don't want to run a search if the data_Set is null.
            if data_set is None:
                return SearchResult.failure(
                    GameDataServiceNullException(f"{method}: {GameNullDataSetException.DEFAULT_MESSAGE}")
                )
            # certify the context is safe.
            validation_result = context_validator.validate(context)
            if validation_result.is_failure():
                return SearchResult.failure(validation_result.exception)
            # After context is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by game id.
            if context.id is not None:
                return cls._find_by_id(data_set, context.id)
            # Entry point into searching by game player.
            if context.agent is not None:
                return cls._find_by_agent(data_set, context.agent)
        # Finally, if some exception is not handled by the checks wrap it inside an GameFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                GameFinderException(ex=ex, message="{method}: {GameFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, data_set: List[Game], id: int) -> SearchResult[List[Game]]:
        """
        # Action:
        1.  Get the Game with the matching id.
        2.  If no match is found return an exception.
        3.  An id search should produce either no hits or one hit only.
        4.  Multiple unique agents in the result indicates a problem.

        # Parameters:
            *   id (int)
            *   data_set (List[Game])

        # Returns:
        SearchResult[List[Game]] containing either:
            - On success: List[Game] in the payload.
            - On failure: Exception.

        # Raises:
            *   AgentFinderException
        """
        method = "GameFinder._find_by_id"
        try:
            matches = [game for game in data_set if game.id == id]
            # There should be either no Games with the id or one and only one Game will have that id.
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        # Finally, if some exception is not handled by the checks wrap it inside an GameFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                GameFinderException(ex=ex, message=f"{method}: {GameFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_agent(cls, data_set: [Game], agent: PlayerAgent) -> SearchResult[List[Game]]:
        """
        # Action:
        1.  Get the Game with the matching player-player_agent.
        2.  If no match is found return an exception.
        3.  An id search should produce either no hits or one hit only.

        # Parameters:
            *   player_agent (PlayerAgent)
            *   data_set (List[PlayerAgent])

        # Returns:
        SearchResult[List[Game]] containing either:
            - On success: List[Game] in the payload.
            - On failure: Exception.

        # Raises:
            *   AgentFinderException
        """
        method = "GameFinder._find_by_agent"
        try:
            matches = [game for game in data_set if agent in game.agents]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        # Finally, if some exception is not handled by the checks wrap it inside an GameFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                GameFinderException(ex=ex, message=f"{method}: {GameFinderException.DEFAULT_MESSAGE}")
            )