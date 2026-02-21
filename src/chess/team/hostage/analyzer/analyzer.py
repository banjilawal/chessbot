# src/chess/team/prisoner/analyzer.py

"""
Module: chess.team.prisoner.analyzer
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import cast

from chess.token import Token, TokenService, CombatantToken, KingToken
from chess.system import LoggingLevelRouter, RelationReport, RelationAnalyzer
from chess.team import Team, HostageAnalysisException, TeamContext, TeamValidator


class HostageRelationAnalyzer(RelationAnalyzer[Team, Token]):
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Establish what type of relationship a piece has with team's prisoner. Either none, a partial relation or
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
    def analyze(
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
            2.  If the piece == team they are not related. Else they are partially related.
            3.  If searching team prisoner for the satellite produces an error send the exception chain. If the
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
                - On not related: Neither team, occupant nor exception.
        # RAISES:
            *   HostageAnalysisException
        """
        method = "HostageRelationAnalyzer.test"
        
        # Process the possible team_validation outcomes.
        team_validation = team_validator.validate(candidate_primary)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport(
                HostageAnalysisException(
                    message=f"{method}: {HostageAnalysisException.ERROR_CODE}",
                    ex=team_validation.exception,
                )
            )
        team = cast(Team, team_validation.payload)
        
        # Process the possible piece_validation outcomes.
        piece_validation = piece_service.validator.validate(candidate_satellite)
        if piece_validation.is_failure:
            return RelationReport(
                HostageAnalysisException(
                    message=f"{method}: {HostageAnalysisException.ERROR_CODE}",
                    ex=piece_validation.exception,
                )
            )
        piece = cast(Token, piece_validation.payload)
        # Kings, tokens set to the team, and free enemies are not related to the prisoner list.
        if (
                isinstance(piece, KingToken) or
                piece.team == team or
                (piece.team != team and cast(CombatantToken, piece).captor is None)
        ):
            return RelationReport.not_related()
        
        # At this point a piece can only be a captured combatant. The possible relations are unregistered
        # occupant or fully bidirectional. This can only be resolved with a search.
        hostage_search = team.hostages.search(context=TeamContext(id=piece.id))
        if hostage_search.is_failure:
            # Return the exception chain on failure.
            return RelationReport(
                HostageAnalysisException(
                    message=f"{method}: {HostageAnalysisException.ERROR_CODE}",
                    ex=hostage_search.exception,
                    )
                )
        # On the empty search the occupant has not been added to the prisoner list.
        if hostage_search.is_empty:
            return RelationReport.partial(satellite=piece)
        # All other paths in the test chain have been exhausted. The team.hostages-occupant tuple is fully bidirectional.
        return RelationReport.bidirectional(primary=team, satellite=piece)