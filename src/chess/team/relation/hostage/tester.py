# src/chess/team/relation/tester.py

"""
Module: chess.team.relation.tester
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""
from typing import cast

from chess.system import LoggingLevelRouter, RelationReport, RelationTester
from chess.team import Team, HostageTokenRelationTestFailedException, TeamContext, TeamValidator
from chess.token import Token, TokenService
from chess.token.context.context import TokenContext
from chess.token.model.combatant.token import CombatantToken
from chess.token.model.king.token import KingToken


class HostageTokenRelationTester(RelationTester[Team, Token]):
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Establish what type of relationship a piece has with team's hostage. Either none, a partial relation or
        completely bidirectional.

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
            candidate_primary: Team,
            candidate_satellite: Token,
            piece_service: TokenService = TokenService(),
            team_validator: TeamValidator = TeamValidator(),
    ) -> RelationReport[Team, Token]:
        """
        # ACTION:
        1.  If either candidate fails its safety certification send the exception chain in the RelationReport. Else,
            cast the candidate_primary to a Team instance; arena and candidate_satellite to Token instance; piece.
        2.  If the piece == team they are not related. Else they are partially related.
        3.  If searching team hostage for the satellite produces an error send the exception chain. If the search
            produced a match send a bidirectional report. Else send a partial relation report.

        # PARAMETERS:
            *   candidate_primary (Team)
            *   candidate_satellite (CombatantToken)
            *   piece_service (PieceService)
            *   team_validator (TeamValidator)

        # RETURN:
            *   RelationReport[Team, Token] containing either:
                - On failure: Exception
                - On partial: Token only
                - On bidirectional: Team and Token
                - On not related: Neither team, token nor exception.

        # RAISES:
            *   HostageTokenRelationTestFailedException
        """
        method = "HostageTokenRelationTester.test"
        # Process the possible team_validation outcomes.
        team_validation = team_validator.validate(candidate_primary)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport(
                HostageTokenRelationTestFailedException(
                    message=f"{method}: {HostageTokenRelationTestFailedException.ERROR_CODE}",
                    ex=team_validation.exception,
                )
            )
        team = cast(Team, team_validation.payload)
        
        # Process the possible piece_validation outcomes.
        piece_validation = piece_service.validator.validate(candidate_satellite)
        if piece_validation.is_failure:
            return RelationReport(
                HostageTokenRelationTestFailedException(
                    message=f"{method}: {HostageTokenRelationTestFailedException.ERROR_CODE}",
                    ex=piece_validation.exception,
                )
            )
        piece = cast(Token, piece_validation.payload)
        
        # If the piece is assigned to it's not a satellite of the hostage list.
        if piece.team == team:
            return RelationReport.not_related()
        
        if piece.team != team:
            if isinstance(piece, KingToken): return RelationReport.not_related()
            if isinstance(piece, CombatantToken):
                piece = cast(CombatantToken, piece)
            if piece.captor is None:
                return RelationReport.not_related()
            hostage_search = team.hostages.search(context=TeamContext(id=piece.id))
            if hostage_search.is_failure:
                # Return the exception chain on failure.
                return RelationReport(
                    HostageTokenRelationTestFailedException(
                        message=f"{method}: {HostageTokenRelationTestFailedException.ERROR_CODE}",
                        ex=hostage_search.exception,
                        )
                    )
            if hostage_search.is_empty:
                return RelationReport.not_related()
        # Deal with the success case.
        return RelationReport.bidirectional(primary=team, satellite=piece)