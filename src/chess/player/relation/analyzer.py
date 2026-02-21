# src/chess/owner/relation/tester.py

"""
Module: chess.owner.relation.tester
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.player import Player, PlayerValidator
from chess.player.relation import PlayerTeamAnalysisException
from chess.team import Team, TeamContext, TeamService
from chess.system import LoggingLevelRouter, RelationReport, RelationAnalyzer



class PlayerTeamRelationAnalyzer(RelationAnalyzer[Player, Team]):
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Test if whether an owner-team tuple have either none, partial, or fully bidirectional relation between them.
    2.  If the testing was not completed send an exception chain to the caller.

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
            candidate_satellite: Team,
            candidate_primary: Player,
            team_service: TeamService = TeamService(),
            player_validator: PlayerValidator = PlayerValidator(),
    ) -> RelationReport[Player, Team]:
        """
        # ACTION:
        1.  If either candidate fails its safety certification send the exception chain in the RelationReport. Else,
            cast the candidate_primary to owner instance; owner and candidate_satellite to Team instance; team.
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
        method = "PlayerService.analyze"
        
        # Handle the case that owner validation fails.
        player_validation = player_validator.validate(candidate_primary)
        if player_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                PlayerTeamAnalysisException(
                    message=f"{method}: {PlayerTeamAnalysisException.ERROR_CODE}",
                    ex=player_validation.exception
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary ue validation.payload for the cast.
        player = cast(Player, player_validation.payload)
        
        # Handle the case that team validation fails.
        team_validation = player.teams.integrity_service.validator.validate(candidate_satellite)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                PlayerTeamAnalysisException(
                    message=f"{method}: {PlayerTeamAnalysisException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        # Just incase things aren't Liskovian on the candidate_satellite ue validation.payload for the cast.
        team = cast(Team, team_validation.payload)
        
        # If the team belongs to a different owner it's not a satellite of the owner. They are not related.
        if player != team.owner:
            return RelationReport.not_related()
        
        # For complete coverage and certainty search the assignments not just the current_team.
        search_result = player.teams.search_teams(context=TeamContext(id=team.id))
        if search_result.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                PlayerTeamAnalysisException(
                    message=f"{method}: {PlayerTeamAnalysisException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # If the team was not found the bidirectional relationship has not been fully completed.
        if search_result.is_empty:
            return RelationReport.partial(satellite=team)
        # All other paths in the test chain have been exhausted. The owner-team tuple is fully bidirectional.
        return RelationReport.bidirectional(primary=player, satellite=team)