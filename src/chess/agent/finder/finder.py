# src/chess/agent/finder/finder

"""
Module: chess.agent.finder.finder
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from typing import List

from chess.game import Game
from chess.system import LoggingLevelRouter, Finder, SearchResult
from chess.agent import (
    Agent, AgentContext, AgentContextValidator, AgentFinderException, AgentVariety, HumanAgent,
    MachineAgent, AgentNullDataSetException
)
from chess.team import Team, TeamContext


class AgentFinder(Finder[Agent]):
    """
    # ROLE: Finder
  
    # RESPONSIBILITIES:
    1.  Search AgentDataService or UniqueDataService objects for Agents with an attribute that matches the
        target inside an AgentContext.
    2.  Safely forward any errors encountered during a search to the caller.
    
    # PARENT
        *   Finder
  
    # PROVIDES:
    AgentFinder:
  
    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            data_set: List[Agent],
            context: AgentContext,
            context_validator: AgentContextValidator = AgentContextValidator()
    ) -> SearchResult[List[Agent]]:
        """
        # Action:
        1.  Verify the data_set is not null and contains only Agent objects,
        2.  Use context_validator to certify the provided context.
        3.  Call the finder method which matches the attribute whose flag was raised.
        4.  If the logic does not account for an Agent attribute drop to the try-finally block.

        # Parameters:
            *   data_set (List[Agent]):
            *   context: AgentContext
            *   context_validator: AgentContextValidator

        # Returns:
        SearchResult[List[Agent]] containing either:
                - On success:   List[agent] in the payload.
                - On failure:   Exception.

        # Raises:
            *   TypeError
            *   AgentNullDataSetException
            *   AgentFinderException
        """
        method = "AgentFinder.find"
        try:
            # Don't want to run a search if the data_Set is null.
            if data_set is None:
                return SearchResult.failure(
                    AgentNullDataSetException(f"{method}: {AgentNullDataSetException.DEFAULT_MESSAGE}")
                )
            # certify the context is safe.
            validation_result = context_validator.validate(context)
            if validation_result.is_failure():
                return SearchResult.failure(validation_result.exception)
            
            # After checks are passed pick which finder method to call.
            if context.id is not None:
                return cls._find_by_id(data_set, context.id)
            # Find by name
            if context.name is not None:
                return cls._find_by_name(data_set, context.name)
            # Find by team
            if context.team is not None:
                return cls._find_by_team(data_set, context.team)
            # Find by game
            if context.game is not None:
                return cls._find_by_game(data_set, context.game)
            # Find by agent type (Human or Machine)
            if context.variety is not None:
                return cls._find_by_variety(data_set, context.variety)
            
        # Finally, if some exception is not handled by the checks wrap it inside an AgentFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                AgentFinderException(ex=ex, message="{method}: {AgentFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, data_set: [Agent], id: int) -> SearchResult[List[Agent]]:
        """
        # Action:
        1.  Get the agents whose id matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple unique hits there is a problem.

        # Parameters:
            *   id (int)
            *   data_set (List[Agent])

        # Returns:
        SearchResult[List[Agent]] containing either:
                - On success:   List[agent] in the payload.
                - On failure:   Exception.

        # Raises:
            *   AgentFinderException
        """
        method = "AgentFinder._find_by_id"
        try:
            matches = [agent for agent in data_set if agent.id == id]
            # There should be either no Agents with the id or one and only one Agent will have that id.
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        
        # Finally, if some exception is not handled by the checks wrap it inside an AgentFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                AgentFinderException(ex=ex, message=f"{method}: {AgentFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, data_set: [Agent], name: str) -> SearchResult[List[Agent]]:
        """
        # Action:
        1.  Get the agents whose names are a case-insensitive. match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   name (str)
            *   data_set (List[Agent])

        # Returns:
        SearchResult[List[Agent]] containing either:
                - On success:   List[agent] in the payload.
                - On failure:   Exception.

        # Raises:
            *   AgentFinderException
        """
        method = "AgentFinder._find_by_name"
        try:
            # Names are unique the search should only produce one unique result.
            matches = [agent for agent in data_set if agent.name.upper() == name.upper()]
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
        # Finally, if some exception is not handled by the checks wrap it inside an AgentFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                AgentFinderException(ex=ex, message=f"{method}: {AgentFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_team(cls, data_set: [Agent], team: Team) -> SearchResult[List[Agent]]:
        """
        # Action:
        1.  Get the agent whose team is a match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If multiple agents own the same target there is a problem.

        # Parameters:
            *   team (Team)
            *   data_set (List[Agent])

        # Returns:
        SearchResult[List[Agent]] containing either:
                - On success:   List[agent] in the payload.
                - On failure:   Exception.

        # Raises:
            *   AgentFinderException
        """
        method = "AgentFinder._find_by_team"
        try:
            # Loop through the set and return the first agent who ran the team.
            # If more than one Agent is returned there might be a problem.
            for agent in data_set:
                team_search = agent.team_assignments.search(context=TeamContext(id=team.id))
                if team_search.is_failure():
                    return SearchResult.failure(team_search.exception)
                # Put the first agent that matches inside a List then send the array inside a SearchResult.
                if team_search.is_success():
                    return SearchResult.success(payload=List[team_search.payload])
            return SearchResult.empty()
        
        # Finally, if some exception is not handled by the checks wrap it inside an AgentFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                AgentFinderException(ex=ex, message=f"{method}: {AgentFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_game(cls, data_set: [Agent], game: Game) -> SearchResult[List[Agent]]:
        """
        # Action:
        1.  Get the agent whose game is a match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly two matches are found return a successful SearchResult with the both agents in an array.
        4.  If only one agent is found there is a problem.

        # Parameters:
            *   game(Game)
            *   data_set (List[Agent])

        # Returns:
        SearchResult[List[Agent]] containing either:
                - On success:   List[agent] in the payload.
                - On failure:   Exception.

        # Raises:
            *   AgentFinderException
        """
        method = "AgentFinder._find_by_game"
        try:
            matches = []
            for agent in data_set:
                game_search = agent.games.search(context=GameContext(id=game.id))
                if game_search.is_failure():
                    return SearchResult.failure(game_search.exception)
                if game_search.is_success():
                    matches.append(game_search.payload)
            # Process the different outcomes of the searching loop.
            if len(matches) == 0:
                return SearchResult.empty()
            # There should be two and only two Agents associated with a particular Game.
            # Any other value indicates there's a problem.
            if len(matches) != 2:
                return SearchResult.failure(
                    AgentFinderException(f"{method}: {AgentFinderException.DEFAULT_MESSAGE}")
                )
            # Return success when there are exactly two Agents found.
            
            return SearchResult.success(payload=matches)
        # Finally, if some exception is not handled by the checks wrap it inside an AgentFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                AgentFinderException(ex=ex, message=f"{method}: {AgentFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_variety(cls, data_set: [Agent], variety) -> SearchResult[[Agent]]:
        """
        # Action:
        1.  Get the agents whose names are a agent_variety. match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the finder returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   agent_variety (AgentVariety)
            *   data_set (List[Agent])

        # Returns:
        SearchResult[List[Agent]] containing either:
                - On success:   List[agent] in the payload.
                - On failure:   Exception.

        # Raises:
            *   AgentFinderException
        """
        method = "AgentFinder._find_by_name"
        try:
            matches = []
            # Use the variety to pick which concrete Agent type needs to be found.
            if variety == AgentVariety.MACHINE_AGENT:
                matches = [agent for agent in data_set if isinstance(agent, MachineAgent)]
                
            if variety == AgentVariety.HUMAN_AGENT:
                matches = [agent for agent in data_set if isinstance(agent, HumanAgent)]
            
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an AgentFinderException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                AgentFinderException(ex=ex, message=f"{method}: {AgentFinderException.DEFAULT_MESSAGE}")
            )