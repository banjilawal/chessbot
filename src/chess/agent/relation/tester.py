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
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Test if whether an agent-team tuple have either none, partial, or fully bidirectional relation between them.
    2.  If the testing was not completed send an exception chain to the caller.

    # PARENT:
        *   RelationTester

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def test(
            cls,
            candidate_primary: PlayerAgent,
            candidate_satellite: Team,
            owner_validator: AgentValidator = AgentValidator(),
            team_service: TeamService = TeamService(),
    ) -> RelationReport[PlayerAgent, Team]:
        """
        # ACTION:
        1.  If either candidate fails its safety certification send the exception chain in the RelationReport. Else,
            cast the candidate_primary to agent instance; agent and candidate_satellite to Team instance; team.
        2.  If the team.owner != owner they are not related. Else they are partially related.
        3.  If searching owner's teams for the satellite produces an error send the exception chain. If the search
            produced aa match send a bidirectional report. Else send a partial relation report.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   arena_variety (ArenaVariety)
            *   engine_service (Optional[EngineService])

        # RETURN:
        ValidationResult[Arena] containing either:
            - On success: Arena in the payload.
            - On failure: Exception.

        # RAISES:
            *   ArenaValidationFailedException
        """
        method = "AgentService.certify_team_agent_relationship"
        # Process the possible owner_validation outcomes.
        owner_validation = owner_validator.validate(candidate_primary)
        if owner_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                OwnerTeamRelationTestFailedException(
                    message=f"{method}: {OwnerTeamRelationTestFailedException.ERROR_CODE}",
                    ex=owner_validation.exception
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary ue validation.payload for the cast.
        owner = cast(PlayerAgent, owner_validation.payload)
        
        # Process the possible team_validation outcomes.
        team_validation = team_service.validator.validate(candidate_satellite)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                OwnerTeamRelationTestFailedException(
                    message=f"{method}: {OwnerTeamRelationTestFailedException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        # Just incase things aren't Liskovian on the candidate_satellite ue validation.payload for the cast.
        team = cast(Team, team_validation.payload)
        
        # If the team belongs to a different owner it's not a satellite of the agent. They are not related.
        if owner != team.owner:
            return RelationReport.not_related()
        
        # For complete coverage and certainty search the assignments not just the current_team.
        search = owner.team_assignments.search_teams(context=TeamContext(id=team.id))
        if search.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                OwnerTeamRelationTestFailedException(
                    message=f"{method}: {OwnerTeamRelationTestFailedException.ERROR_CODE}",
                    ex=search.exception
                )
            )
        # If the team was not found the bidirectional relationship has not been fully completed.
        if search.is_empty:
            return RelationReport.partial(satellite=team)
        # All other paths in the test chain have been exhausted. The agent-team tuple is fully bidirectional.
        return RelationReport.bidirectional(primary=owner, satellite=team)