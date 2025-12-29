# src/chess/team/relation/tester.py

"""
Module: chess.team.relation.tester
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""
from typing import cast

from chess.system import LoggingLevelRouter, RelationReport, RelationTester
from chess.team import Team, TeamMemberRelationTestFailedException, TeamValidator
from chess.token import Token, TokenService
from chess.token.context.context import TokenContext


class TeamMemberRelationTester(RelationTester[Team, Token]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def test(
            cls,
            candidate_primary: Team,
            candidate_satellite: Token,
            team_validator: TeamValidator = TeamValidator(),
            token_service: TokenService = TokenService(),
    ) -> RelationReport[Team, Token]:
        method = "TeamMemberRelationTester.test"
        team_validation = team_validator.validate(candidate_primary)
        if team_validation.is_failure:
            return RelationReport(
                TeamMemberRelationTestFailedException(
                    message=f"{method}: {TeamMemberRelationTestFailedException.ERROR_CODE}",
                    ex=team_validation.exception,
                )
            )
        team = cast(Team, team_validation.payload)
        
        token_validation = token_service.validator.validate(candidate_satellite)
        if token_validation.is_failure:
            return RelationReport(
                TeamMemberRelationTestFailedException(
                    message=f"{method}: {TeamMemberRelationTestFailedException.ERROR_CODE}",
                    ex=token_validation.exception,
                )
            )
        token = cast(Token, token_validation.payload)
        
        if token.team != team:
            return RelationReport.not_related()
        member_search = team.roster.search(context=TokenContext(id=token.id))
        
        if member_search.is_failure:
            return
        return RelationReport((candidate_primary), S(candidate_satellite), team_valiation)