# src/chess/agent/service.py

"""
Module: chess.agent.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""



from chess.system import BuildResult, SearchResult, ValidationResult
from chess.agent.agent import Agent, PlayerAgentBuilder, PlayerAgentValidator, PlayerAgentSearch


class PlayerAgentService:
    _agents: [Agent]
    _builder: PlayerAgentBuilder
    _validator: PlayAgentValidator
    _search: PlayerAgentTeamSearch
    
    def __init__(
            self,
            builder: type[PlayerAgentBuilder]=PlayerAgentBuilder,
            validator: type[PlayerAgentValidator]=PlayerAgentValidator,
            search_service: PlayerAgentSearchService = PlayerAgentSearchService()
    ):
        self._agents = [Agent]
        self._builder = builder
        self._validator = validator
        self._search_service = search_serivce


    def build_agent(
            self,
            id: int,
            name: str,
            agent_category: PlayerAgentCategory
    ) -> BuildResult[Agent]:
        return self._builder.build(id=id, name=name, agent_category=agent_category)
    
    
    def validate_agent(self, agent: Agent) -> ValidationResult[Agent]:
        return self._validator.validate(agent=agent)
    
    
    def search_for_team(
            self,
            player_agent: Agent,
            search_context: AgentTeamSearchContext
    ) -> SearchResult[List[team]]:
        return self._search_service.search(data_owner=player_agent, search_context=search_context)
