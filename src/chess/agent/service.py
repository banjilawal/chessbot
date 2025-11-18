# src/chess/agent/service.py

"""
Module: chess.agent.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import List, cast

from chess.engine.service import EngineService
from chess.system import BuildResult, IdentityService, LoggingLevelRouter, SearchResult, ValidationResult
from chess.agent import (
    Agent, AgentBuilder, AgentValidator, HumanAgent, MachineAgent, TeamSearchService,
    TeamStackService
)


class AgentService:
    _agents: List[Agent]
    _builder: AgentBuilder
    _validator: AgentValidator
    _search_service: TeamSearchService
    _identity_service: IdentityService
    
    def __init__(
            self,
            builder: type[AgentBuilder] = AgentBuilder,
            validator: type[AgentValidator] = AgentValidator,
            search_service: TeamSearchService = TeamSearchService(),
            identity_service: IdentityService = IdentityService(),
    ):
        self._agents = []
        self._builder = builder
        self._validator = validator
        self._search_service = search_service
        self._identity_service = identity_service


    @LoggingLevelRouter.monitor
    def build_human_agent(self, id: int, name: str) -> BuildResult[HumanAgent]:
        try:
            agent_build =  self._builder.build(
                id=id,
                name=name,
                identity_service=self._identity_service,
                team_stack_service=TeamStackService()
            )
            if agent_build.is_failure():
                return BuildResult.failure(agent_build.exception)
            
            agent = cast(HumanAgent, agent_build.payload)
            
            if agent in self._agents:
                return BuildResult.failure(
                    CannotAddDuplicatePlayerToAgentServicException(
                        f"{method}: {CannotAddDuplicatePlayerToAgentService.DEFAULT_MESSAGE}"
                    )
                )
            self._agents.append(agent)
            
            return BuildResult.success(agent_build.payload)
        except Exception as ex:
            return BuildResult.failure(ex)
    
    def build_machine_agent(
            self,
            id: int,
            name: str,
            engine_service: EngineService = EngineService()
    ) -> BuildResult[Agent]:
        try:
            agent_build = self._builder.build(
                id=id,
                name=name,
                engine_service=engine_service,
                identity_service=self._identity_service,
                team_stack_service=TeamStackService()
            )
            if agent_build.is_failure():
                return BuildResult.failure(agent_build.exception)
            
            agent = cast(MachineAgent, agent_build.payload)
            
            if agent in self._agents:
                return BuildResult.failure(
                    CannotAddDuplicatePlayerToAgentServicException(
                        f"{method}: {CannotAddDuplicatePlayerToAgentService.DEFAULT_MESSAGE}"
                    )
                )
            
                self._agents.append(agent)
            return BuildResult.success(agent_build.payload)
    
        except Exception as ex:
            return BuildResult.failure(ex)
    
    
    def validate_agent(self, agent: Agent) -> ValidationResult[Agent]:
        return self._validator.validate(agent=agent)
    
    
    def search_for_team(
            self,
            player_agent: Agent,
            search_context: AgentTeamSearchContext
    ) -> SearchResult[List[team]]:
        return self._search_service.search(data_owner=player_agent, search_context=search_context)
