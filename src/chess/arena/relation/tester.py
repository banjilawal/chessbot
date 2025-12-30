# src/chess/arena/relation/tester.py

"""
Module: chess.arena.relation.tester
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.team import Team, TeamService
from chess.system import LoggingLevelRouter, RelationReport, RelationTester
from chess.arena import (
    Arena, ArenaSlotAlreadyOccupiedException, ArenaValidator, ArenaTeamRelationTestFailedException,
    TeamPlayingDifferentArenaException
)


class ArenaTeamRelationTester(RelationTester[Arena, Team]):
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Test if whether an arena-team tuple have either none, partial, or fully bidirectional relation between them.
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
    def test(
            cls,
            candidate_primary: Arena,
            candidate_satellite: Team,
            arena_validator: ArenaValidator = ArenaValidator(),
            team_service: TeamService = TeamService(),
    ) -> RelationReport[Arena, Team]:
        """
        # ACTION:
        1.  If either candidate fails its safety certification send the exception chain in the RelationReport. Else,
            cast the candidate_primary to arena instance; arena and candidate_satellite to Team instance; team.
        2.  If the team.owner != owner they are not related. Else they are partially related.
        3.  If searching owner's teams for the satellite produces an error send the exception chain. If the search
            produced aa match send a bidirectional report. Else send a partial relation report.

        # PARAMETERS:
            *   candidate_primary (Arena)
            *   candidate_satellite (Team)
            *   arena_validator (ArenaValidator)
            *   team_service (TeamService)

        # RETURN:
        RelationTest[Arena, Team] containing either
            *   No relation:
            *   On error: an Exception

        # RAISES:
            *   ArenaValidationFailedException
        """
        method = "ArenaService.certify_team_arena_relationship"
        # Process the possible arena_validation outcomes.
        arena_validation = arena_validator.validate(candidate_primary)
        if arena_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                ArenaTeamRelationTestFailedException(
                    message=f"{method}: {ArenaTeamRelationTestFailedException.ERROR_CODE}",
                    ex=arena_validation.exception
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        arena = cast(Arena, candidate_primary)
        
        # Process the possible team_validation outcomes.
        team_validation = team_service.validator.validate(candidate_satellite)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                ArenaTeamRelationTestFailedException(
                    message=f"{method}: {ArenaTeamRelationTestFailedException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        team = cast(Team, team_validation.payload)
        
        # If the team is assigned to a different arena it's not a satellite of the area. They are not related.
        if arena != team.arena:
            return RelationReport.not_related()
        
        # The two paths left are: processing the black satellite or the white one.
        
        # When the black satellite has not registered with the arena the relation is partial.
        if team.schema.BLACK:
            if arena.black_team is None:
                return RelationReport.partial(satellite=team)
            # When the black satellite has occupied its slot the relation is bidirectional.
            if arena.black_team == team:
                return RelationReport.bidirectional(primary=arena, satellite=team)
            # If the black slot is occupied by some other team an error has occurred. Return the exception chain.
            return RelationReport.failure(
                ArenaTeamRelationTestFailedException(
                    message=f"{method}: {ArenaTeamRelationTestFailedException.ERROR_CODE}",
                    ex=TeamPlayingDifferentArenaException(
                        f"{method}: {ArenaSlotAlreadyOccupiedException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        # When the white team has not registered with the arena the relation is partial.
        if arena.white_team is None:
            return RelationReport.partial(satellite=team)
        # When the white team has occupied its slot the relation is bidirectional.
        if arena.white_team == team:
            return RelationReport.bidirectional(primary=arena, satellite=team)
        # If the white slot is occupied by some other team an error has occurred. Return the exception chain.
        return RelationReport.failure(
            ArenaTeamRelationTestFailedException(
                message=f"{method}: {ArenaTeamRelationTestFailedException.ERROR_CODE}",
                ex=TeamPlayingDifferentArenaException(f"{method}: {ArenaSlotAlreadyOccupiedException.DEFAULT_MESSAGE}")
            )
        )