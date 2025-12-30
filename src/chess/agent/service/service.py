# src/chess/agent/service/service.py

"""
Module: chess.agent.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from typing import cast
from unittest import removeResult

from chess.agent.relation import AgentTeamRelationTester
from chess.system import EntityService, InsertionResult, LoggingLevelRouter, Result, id_emitter
from chess.agent import (
    AgentServiceException, PlayerAgent, AgentFactory, AgentValidator,
    TeamBelongsToDifferentOwnerException
)
from chess.team import Team, TeamService
from chess.team.service.data.result import AddingDuplicateTeamException


class AgentService(EntityService[PlayerAgent]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing PlayerAgent microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for PlayerAgent state by providing single entry and exit points to PlayerAgent
        lifecycle.

    # PARENT:
        *   EntityService
    
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See EntityService class for inherited attributes.
    """
    DEFAULT_NAME = "AgentService"
    _team_relation_tester: AgentTeamRelationTester
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: AgentFactory = AgentFactory(),
            validator: AgentValidator = AgentValidator(),
            team_relation_tester: AgentTeamRelationTester = AgentTeamRelationTester(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (AgentFactory)
            *   validator (AgentValidator)

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._team_relation_tester = team_relation_tester
        
    @property
    def builder(self) -> AgentFactory:
        """get AgentBuilder"""
        return cast(AgentFactory, self.entity_builder)
    
    @property
    def validator(self) -> AgentValidator:
        """get AgentValidator"""
        return cast(AgentValidator, self.entity_validator)
    
    @property
    def team_relation_tester(self) -> AgentTeamRelationTester:
        return self._team_relation_tester
    
    def add_team(
            self,
            agent: PlayerAgent,
            team: Team,
            team_service: TeamService = TeamService()
    ) -> InsertionResult[Team]:
        method = "AgentService.add_team"
        relation = self.team_relation_tester.test(
            candidate_primary=agent,
            candidate_secondary=team,
            owner_validator=self.validator,
            team_service=team_service,
        )
        if relation.is_failure:
            return InsertionResult.failure(
                AgentServiceException(
                    message=f"ServiceId:{self.id}, {method}: {AgentServiceException.ERROR_CODE}",
                    ex=relation.exception
                )
            )
        if relation.does_not_exist:
            return InsertionResult.failure(
                AgentServiceException(
                    message=f"ServiceId:{self.id}, {method}: {AgentServiceException.ERROR_CODE}",
                    ex=TeamBelongsToDifferentOwnerException(
                        f"{method}: {TeamBelongsToDifferentOwnerException.DEFAULT_MESSAGE}"
                    )
                )
            )
        if relation.is_success:
            return InsertionResult.failure(
                AgentServiceException(
                    message=f"ServiceId:{self.id}, {method}: {AgentServiceException.ERROR_CODE}",
                    ex=AddingDuplicateTeamException(f"{method}: {AddingDuplicateTeamException.DEFAULT_MESSAGE}")
                )
            )
        return agent.team_assignments.add_team(team=team)

    
    