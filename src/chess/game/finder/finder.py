# src/chess/game/finder/finder

"""
Module: chess.game.finder.finder
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from typing import List


from chess.agent import Agent
from chess.game.finder import GameFinderException
from chess.system import LoggingLevelRouter, Finder, SearchResult
from chess.game import (
    GameSnapshotContextt, GameSnapshotContexttValidator, GameSnapshot, GameTimeline, NullGameTimelineException
)



class GameSnapshotFinder(Finder[GameSnapshot]):
    """
    # ROLE: Finder
  
    # RESPONSIBILITIES:
    1.  Search GameDataService or UniqueDataService objects for Games with an attribute that matches the
        target inside an GameSnapshotContextt.
    2.  Safely forward any errors encountered during a search to the caller.
    
    # PARENT
        *   Finder
  
    # PROVIDES:
    GameSnapshotFinder:
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            data_set: GameTimeline,
            context: GameSnapshotContextt,
            context_validator: GameSnapshotContexttValidator = GameSnapshotContexttValidator()
    ) -> SearchResult[List[GameSnapshot]]:
        """
        # Action:
        1.  Verify the data_set is not null and contains only Game objects,
        2.  Use context_validator to certify the provided context.
        3.  Call the finder method which matches the attribute whose flag was raised.
        4.  If the logic does not account for an Game attribute drop to the try-finally block.

        # Parameters:
            *   data_set (List[GameSnapshot]):
            *   context: GameSnapshotContextt
            *   context_validator: GameSnapshotContexttValidator

        # Returns:
        SearchResult[List[GameSnapshot]] containing either:
                - On success:   List[gameSnapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TypeError
            *   NullGameTimelineException
            *   GameFinderException
        """
        method = "GameSnapshotFinder.find"
        try:
            # Don't want to run a search if the data_Set is null.
            if data_set is None:
                return SearchResult.failure(
                    NullGameTimelineException(f"{method}: {NullGameTimelineException.DEFAULT_MESSAGE}")
                )
            # certify the context is safe.
            validation_result = context_validator.validate(context)
            if validation_result.is_failure():
                return SearchResult.failure(validation_result.exception)
            
            # After checks are passed pick which finder method to call.
            if context.id is not None:
                return cls._find_by_id(data_set, context.id)
            
            # Find by agent
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
    def _find_by_timestamp(cls, data_set: GameTimeline, timestamp: int) -> SearchResult[List[GameSnapshot]]:
        """
        # Action:
        1.  Get the games whose id matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple unique hits there is a problem.

        # Parameters:
            *   timestamp (int)
            *   data_set (GameTimeline)

        # Returns:
        SearchResult[List[GameSnapshot]] containing either:
                - On success:   List[gameSnapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   GameFinderException
        """
        method = "GameSnapshotFinder._find_by_timestamp"
        try:
            matches = [snapshot for snapshot in data_set.items if snapshot.timestamp == timestamp]
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
    def _find_by_agent(cls, data_set: GameTimeline, agent: Agent) -> SearchResult[List[GameSnapshot]]:
        """
        # Action:
        1.  Get the game whose agent is a match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If multiple games own the same target there is a problem.

        # Parameters:
            *   agent (Agent)
            *   data_set (GameTimeline)

        # Returns:
        SearchResult[List[GameSnapshot]] containing either:
                - On success:   List[gameSnapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   GameFinderException
        """
        method = "GameSnapshotFinder._find_by_agent"
        try:
            matches = [snapshot for snapshot in data_set.items if agent in snapshot.arena.agents]
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