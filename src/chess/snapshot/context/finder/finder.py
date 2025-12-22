# src/chess/snapshot/finder/finder.py

"""
Module: chess.snapshot.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List

from chess.team import Team
from chess.agent import PlayerAgent
from chess.system import Finder, LoggingLevelRouter, SearchFailedException, SearchResult
from chess.snapshot import GameTimeline, NullGameTimelineException, Snapshot, SnapshotContext, SnapshotContextValidator




class SnapshotFinder(Finder[Snapshot]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Search AgentDataService or UniqueDataService objects for Agents with an attribute that matches the
        target inside an SnapshotContext.
    2.  Safely forward any errors encountered during a search to the caller.

    # PARENT:
        *   Finder

    # PROVIDES:
    SnapshotFinder:

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            dataset: GameTimeline,
            context: SnapshotContext,
            context_validator: SnapshotContextValidator = SnapshotContextValidator()
    ) -> SearchResult[List[Snapshot]]:
        """
        # Action:
        1.  Verify the dataset is not null and contains only Snapshot objects,
        2.  Use context_validator to certify the provided map.
        3.  Call the finder method which matches the attribute whose flag was raised.
        4.  If the logic does not account for an PlayerAgent attribute drop to the try-finally block.

        # Parameters:
            *   dataset (GameTimeline):
            *   map: SnapshotContext
            *   context_validator: SnapshotContextValidator

        # Returns:
        SearchResult[List[Snapshot]] containing either:
                - On success:   List[snapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TypeError
            *   NullGameTimelineException
            *   SnapshotFinderException
        """
        method = "SnapshotFinder.find"
        try:
            # Don't want to run a search if the dataset is null.
            if dataset is None:
                return SearchResult.failure(
                    NullGameTimelineException(f"{method}: {NullGameTimelineException.DEFAULT_MESSAGE}")
                )
            # certify the map is safe.
            validation_result = context_validator.validate(context)
            if validation_result.is_failure:
                return SearchResult.failure(validation_result.exception)
            
            # After checks are passed pick which finder method to call.
            if context.timestamp is not None:
                return cls._find_by_timestamp(dataset, context.timestamp)
            # Find by player_agent
            if context.agent is not None:
                return cls._find_by_agent(dataset, context.agent)
            # Find by team
            if context.team is not None:
                return cls._find_by_team(dataset, context.team)
            # Find by exception
            if context.exception is not None:
                return cls._find_by_exception(dataset, context.exception)
        
        # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_timestamp(cls, dataset: GameTimeline, timestamp: id) -> SearchResult[List[Snapshot]]:
        """
        # Action:
        1.  Get the agents whose id matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple unique hits there is a problem.

        # Parameters:
            *   id (int)
            *   dataset (List[Snapshot])

        # Returns:
        SearchResult[List[Snapshot]] containing either:
                - On success:   List[snapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   SnapshotFinderException
        """
        method = "SnapshotFinder._find_by_timestamp"
        try:
            matches = [snapshot for snapshot in dataset.items if snapshot.timestamp == timestamp]
            # There should be either no Agents with the id or one and only one PlayerAgent will have that id.
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
    def _find_by_agent(cls, dataset: GameTimeline, agent: PlayerAgent) -> SearchResult[List[Snapshot]]:
        """
        # Action:
        1.  Get the agents whose agents are a case-insensitive. match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   player_agent (PlayerAgent)
            *   dataset (GameTimeline)

        # Returns:
        SearchResult[List[Snapshot]] containing either:
                - On success:   List[snapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   SnapshotFinderException
        """
        method = "SnapshotFinder._find_by_team"
        try:
            # Agents are unique the search should only produce one unique result.
            matches = [snapshot for snapshot in dataset.items if agent in snapshot.arena.agents]
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
    def _find_by_team(cls, dataset: GameTimeline, team: Team) -> SearchResult[List[Snapshot]]:
        """
        # Action:
        1.  Get the player_agent whose team is a match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If multiple agents own the same target there is a problem.

        # Parameters:
            *   team (Team)
            *   dataset (List[Snapshot])

        # Returns:
        SearchResult[List[Snapshot]] containing either:
                - On success:   List[snapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   SnapshotFinderException
        """
        method = "SnapshotFinder._find_by_team"
        try:
            # Agents are unique the search should only produce one unique result.
            matches = [snapshot for snapshot in dataset.items if team in snapshot.arena.team]
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
    def _find_by_exception(cls, dataset: GameTimeline, exception) -> SearchResult[[PlayerAgent]]:
        """
        # Action:
        1.  Get the agents whose agents are an agent_exception. match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   agent_exception (AgentException)
            *   dataset (List[Snapshot])

        # Returns:
        SearchResult[List[Snapshot]] containing either:
                - On success:   List[snapshot] in the payload.
                - On failure:   Exception.

        # Raises:
            *   SnapshotFinderException
        """
        method = "SnapshotFinder._find_by_agent"
        try:
            matches = []
            # Agents are unique the search should only produce one unique result.
            matches = [snapshot for snapshot in dataset.items if snapshot.exception == exception]
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