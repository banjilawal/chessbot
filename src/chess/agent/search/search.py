# src/chess/agent/searcher/searcher

"""
Module: chess.agent.searcher.searcher
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from typing import List

from chess.system import LoggingLevelRouter, Search, SearchResult
from chess.agent import (
    Agent, AgentContext, AgentContextValidator, AgentSearchException, AgentVariety, HumanAgent,
    MachineAgent, AgentNullDataSetException
)



class AgentSearcher(Search[Agent]):
    """
    # ROLE: Search
  
    # RESPONSIBILITIES:
    1.  Search an Agent.agent_assignments for items whose attribute matches the value in
        AgentsSearchContext function param.
  
    # PROVIDES:
    AgentSearcher:
  
    # ATTRIBUTES:
    None
    
    # CONSTRUCTOR:
    Default Constructor
  
    # CLASS METHODS:
        ## searcher signature:
                def searcher(
                        cls,
                        data_set: List[Agent],
                        search_context: AgentSearchContext
                ) -> SearchResult[List[Agent]]:
                
    # INSTANCE METHODS:
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
        method = "AgentSearcher.find"
        try:
            validation_result = context_validator.validate(context)
            if validation_result.is_failure():
                return SearchResult.failure(validation_result.exception)
            
            if data_set is None:
                return SearchResult.failure(
                    AgentNullDataSetException(
                        f"{method}: "
                        f"{AgentNullDataSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if context.id is not None:
                return cls._find_by_id(data_set, context.id)
            
            if context.name is not None:
                return cls._find_by_name(data_set, context.name)
            
            if context.variety is not None:
                return cls._find_by_variety(data_set, context.variety)
        except Exception as ex:
            return SearchResult.failure(
                AgentSearchException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{AgentSearchException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, data_set: List[Agent], id: int) -> SearchResult[List[Agent]]:
        """
        # Action:
        1.  Get the agents whose id matched the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the searcher returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   id (int):              Target color to searcher for.

            *   data_owner (Agent):     Provides the Agent objects to searcher.

        # Returns:
        SearchResult[List[Agent]] containing either:
                - On success:   List[agent] in the payload.
                - On failure:   Exception.

        # Raises:
            *   AgentSearchException
        """
        method = "AgentSearcher._find_by_id"
        
        try:
            matches = [agent for agent in data_set if agent.id == id]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                AgentSearchException(
                    f"{method}: {AgentSearchException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, data_set: List[Agent], name: str) -> SearchResult[List[Agent]]:
        """
        # Action:
        1.  Get the agents whose names are a case-insensitive. match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the searcher returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   name (str)
            *   data_set (List[Agent])

        # Returns:
        SearchResult[List[Agent]] containing either:
                - On success:   List[agent] in the payload.
                - On failure:   Exception.

        # Raises:
            *   AgentSearchException
        """
        method = "AgentSearcher._find_by_name"
        
        try:
            matches = [agent for agent in data_set if agent.name.upper() == name.upper()]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                AgentSearchException(
                    ex=ex,
                    message=f"{method}: {AgentSearchException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_variety(cls, data_set: List[Agent], variety) -> SearchResult[List[Agent]]:
        """
        # Action:
        1.  Get the agents whose names are a agent_variety. match for the target.
        2.  If no matches are found return an empty SearchResult.
        3.  If exactly one match is found return a successful SearchResult with the single item in an array.
        4.  If the searcher returns multiple hits call _resolve_matching_ids.

        # Parameters:
            *   agent_variety (AgentVariety)
            *   data_set (List[Agent])

        # Returns:
        SearchResult[List[Agent]] containing either:
                - On success:   List[agent] in the payload.
                - On failure:   Exception.

        # Raises:
            *   AgentSearchException
        """
        method = "AgentSearcher._find_by_name"
        
        try:
            matches = []
            
            if variety == AgentVariety.MACHINE_AGENT:
                matches = [agent for agent in data_set if isinstance(agent, MachineAgent)]
            
            if variety == AgentVariety.HUMAN_AGENT:
                matches = [agent for agent in data_set if isinstance(agent, HumanAgent)]
            
            if len(matches) == 0:
                return SearchResult.empty()
            elif len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                AgentSearchException(
                    ex=ex,
                    message=f"{method}: {AgentSearchException.DEFAULT_MESSAGE}"
                )
            )