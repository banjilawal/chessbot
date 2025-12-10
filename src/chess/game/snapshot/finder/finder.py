# src/chess/game/snapshot/finder/finder.py

"""
Module: chess.game.snapshot.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from typing import List

from chess.agent import Agent
from chess.game.snapshot.finder.exception import GameSnapshotFinderException
from chess.system import Finder, LoggingLevelRouter, SearchResult
from chess.game import (
    GameSnapshotContext, GameSnapshotContextValidator, GameTimeline, GameSnapshot, NullGameTimelineException
)
from chess.team import Team


class GameSnapshotFinder(Finder[GameSnapshot]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Search AgentDataService or UniqueDataService objects for Agents with an attribute that matches the
        target inside an GameSnapshotContext.
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
            context: GameSnapshotContext,
            context_validator: GameSnapshotContextValidator = GameSnapshotContextValidator()
    ) -> SearchResult[List[GameSnapshot]]:
        """
        # Action:
        1.  Verify the data_set is not null and contains only GameSnapshot objects,
        2.  Use context_validator to certify the provided context.
        3.  Call the finder method which matches the attribute whose flag was raised.
        4.  If the logic does not account for an Agent attribute drop to the try-finally block.

        # Parameters:
            *   data_set (GameTimeline):
            *   context: GameSnapshotContext
            *   context_validator: GameSnapshotContextValidator

        # Returns:
        SearchResult[List[GameSnapshot]] containing either:
                - On success:   List[gameSnapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TypeError
            *   NullGameTimelineException
            *   GameSnapshotFinderException
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
            if validation_result.is_failure:
                return SearchResult.failure(validation_result.exception)
            
            # After checks are passed pick which finder method to call.
            if context.timestamp is not None:
                return cls._find_by_timestamp(data_set, context.timestamp)
            # Find by agent
            if context.agent is not None:
                return cls._find_by_agent(data_set, context.agent)
            # Find by team
            if context.team is not None:
                return cls._find_by_team(data_set, context.team)
            # Find by exception
            if context.exception is not None:
                return cls._find_by_exception(data_set, context.exception)
        
        # Finally, if some exception is not handled by the checks wrap it inside an GameSnapshotFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                GameSnapshotFinderException(ex=ex, message="{method}: {GameSnapshotFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_timestamp(cls, data_set: GameTimeline, timestamp: id) -> SearchResult[List[GameSnapshot]]:
        """
        # Action:
        1.  Get the agents whose id matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple unique hits there is a problem.

        # Parameters:
            *   id (int)
            *   data_set (List[GameSnapshot])

        # Returns:
        SearchResult[List[GameSnapshot]] containing either:
                - On success:   List[gameSnapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   GameSnapshotFinderException
        """
        method = "GameSnapshotFinder._find_by_timestamp"
        try:
            matches = [snapshot for snapshot in data_set.items if snapshot.timestamp == timestamp]
            # There should be either no Agents with the id or one and only one Agent will have that id.
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        
        # Finally, if some exception is not handled by the checks wrap it inside an GameSnapshotFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                GameSnapshotFinderException(ex=ex, message=f"{method}: {GameSnapshotFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_agent(cls, data_set: GameTimeline, agent: Agent) -> SearchResult[List[GameSnapshot]]:
        """
        # Action:
        1.  Get the agents whose agents are a case-insensitive. match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   agent (Agent)
            *   data_set (GameTimeline)

        # Returns:
        SearchResult[List[GameSnapshot]] containing either:
                - On success:   List[gameSnapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   GameSnapshotFinderException
        """
        method = "GameSnapshotFinder._find_by_team"
        try:
            # Agents are unique the search should only produce one unique result.
            matches = [snapshot for snapshot in data_set.items if agent in snapshot.arena.agents]
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        
        # Finally, if some exception is not handled by the checks wrap it inside an GameSnapshotFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                GameSnapshotFinderException(ex=ex, message=f"{method}: {GameSnapshotFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_team(cls, data_set: GameTimeline, team: Team) -> SearchResult[List[GameSnapshot]]:
        """
        # Action:
        1.  Get the agent whose team is a match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If multiple agents own the same target there is a problem.

        # Parameters:
            *   team (Team)
            *   data_set (List[GameSnapshot])

        # Returns:
        SearchResult[List[GameSnapshot]] containing either:
                - On success:   List[gameSnapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   GameSnapshotFinderException
        """
        method = "GameSnapshotFinder._find_by_team"
        try:
            # Agents are unique the search should only produce one unique result.
            matches = [snapshot for snapshot in data_set.items if team in snapshot.arena.team]
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        
        # Finally, if some exception is not handled by the checks wrap it inside an GameSnapshotFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                GameSnapshotFinderException(ex=ex, message=f"{method}: {GameSnapshotFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_exception(cls, data_set: GameTimeline, exception) -> SearchResult[[Agent]]:
        """
        # Action:
        1.  Get the agents whose agents are a agent_exception. match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   agent_exception (AgentException)
            *   data_set (List[GameSnapshot])

        # Returns:
        SearchResult[List[GameSnapshot]] containing either:
                - On success:   List[gameSnapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   GameSnapshotFinderException
        """
        method = "GameSnapshotFinder._find_by_agent"
        try:
            matches = []
            # Agents are unique the search should only produce one unique result.
            matches = [snapshot for snapshot in data_set.items if snapshot.exception == exception]
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an GameSnapshotFinderException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                GameSnapshotFinderException(ex=ex, message=f"{method}: {GameSnapshotFinderException.DEFAULT_MESSAGE}")
            )