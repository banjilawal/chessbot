# src/chess/agent/relation/tester.py

"""
Module: chess.agent.relation.tester
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.agent.relation import OwnerTeamRelationTestFailedException
from chess.team import Team, TeamContext, TeamService
from chess.system import LoggingLevelRouter, RelationReport, RelationTester
from chess.agent import (
    AgentValidator, PlayerAgent
)


class AgentTeamRelationTester(RelationTester[PlayerAgent, Team]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def test(
            cls,
            candidate_primary: PlayerAgent,
            candidate_satellite: Team,
            owner_validator: AgentValidator = AgentValidator(),
            team_service: TeamService = TeamService(),
    ) -> RelationReport[PlayerAgent, Team]:
        method = "AgentService.certify_team_agent_relationship"
        # Handle the case that the agent is not safe.
        owner_validation = owner_validator.validate(candidate_primary)
        if owner_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                OwnerTeamRelationTestFailedException(
                    message=f"{method}: {OwnerTeamRelationTestFailedException.ERROR_CODE}",
                    ex=owner_validation.exception
                )
            )
        owner = cast(PlayerAgent, candidate_primary)
        
        # Handle the case that the team is not safe.
        team_validation = team_service.validator.validate(candidate_satellite)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                OwnerTeamRelationTestFailedException(
                    message=f"{method}: {OwnerTeamRelationTestFailedException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        team = cast(Team, candidate_satellite)
        
        # Handle the case that the team should be playing a different agent.
        if owner != team.owner:
            return RelationReport.not_related()
        
        search = owner.team_assignments.search_teams(context=TeamContext(id=team.id))
        if search.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                OwnerTeamRelationTestFailedException(
                    message=f"{method}: {OwnerTeamRelationTestFailedException.ERROR_CODE}",
                    ex=search.exception
                )
            )
        if search.is_empty:
            return RelationReport.partial(satellite=team)
        return RelationReport.bidirectional(primary=owner, satellite=team)