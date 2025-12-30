# src/chess/team/relation/roster/tester.py

"""
Module: chess.team.relation.roster.tester
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import cast

from chess.token import Token, TokenService, TokenContext
from chess.system import LoggingLevelRouter, RelationReport, RelationTester
from chess.team import Team, RosterRelationTestFailedException, TeamValidator


class RosterRelationTester(RelationTester[Team, Token]):
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Establish what type of relationship a piece has with team's roster. Either none, a partial relation or
        completely bidirectional.

    # PARENT:
        *   RelationAnalyzer

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
            candidate_primary: Team,
            candidate_satellite: Token,
            piece_service: TokenService = TokenService(),
            team_validator: TeamValidator = TeamValidator(),
    ) -> RelationReport[Team, Token]:
        """
        # ACTION:
            1.  If either candidate fails its safety certification send the exception chain in the RelationReport.
                Else, cast the candidate_primary to a Team instance; arena and candidate_satellite to Token
                instance; piece.
            2.  If the piece.team != team they are not related. Else they are partially related.
            3.  If searching team roster for the satellite produces an error send the exception chain. If the
                search produced a match send a bidirectional report. Else send a partial relation report.
        # PARAMETERS:
            *   candidate_primary (Team)
            *   candidate_satellite (Token)
            *   piece_service (PieceService)
            *   team_validator (TeamValidator)
        # RETURN:
            *   RelationReport[Team, Token] containing either:
                - On failure: Exception
                - On partial: Token only
                - On bidirectional: Team and Token
                - On not related: Neither team, token nor exception.
        # RAISES:
            *   RosterRelationTestFailedException
        """
        method = "RosterRelationTester.test"
        
        # Process the possible team_validation outcomes.
        team_validation = team_validator.validate(candidate_primary)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport(
                RosterRelationTestFailedException(
                    message=f"{method}: {RosterRelationTestFailedException.ERROR_CODE}",
                    ex=team_validation.exception,
                )
            )
        team = cast(Team, team_validation.payload)
        
        # Process the possible piece_validation outcomes.
        piece_validation = piece_service.validator.validate(candidate_satellite)
        if piece_validation.is_failure:
            return RelationReport(
                RosterRelationTestFailedException(
                    message=f"{method}: {RosterRelationTestFailedException.ERROR_CODE}",
                    ex=piece_validation.exception,
                )
            )
        piece = cast(Token, piece_validation.payload)
        
        # If the piece is assigned to a different team it's not a satellite of the current item. They are not related.
        if piece.team != team:
            return RelationReport.not_related()
        
        # Search the roster to decide find out if the piece has a full or partial bidirectional relation to the roster.
        member_search = team.roster.search(context=TokenContext(id=piece.id))
        if member_search.is_failure:
            # Return the exception chain on failure.
            return RelationReport(
                RosterRelationTestFailedException(
                    message=f"{method}: {RosterRelationTestFailedException.ERROR_CODE}",
                    ex=member_search.exception,
                )
            )
        # On the empty search the token has not been added to the roster list.
        if member_search.is_empty:
            return RelationReport.partial(satellite=piece)
        # All other paths in the test chain have been exhausted. The roster-token tuple is fully bidirectional.
        return RelationReport.bidirectional(primary=team, satellite=piece)