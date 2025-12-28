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
    
    @classmethod
    @LoggingLevelRouter.monitor
    def test(
            cls,
            candidate_primary: Arena,
            candidate_satellite: Team,
            arena_validator: ArenaValidator = ArenaValidator(),
            team_service: TeamService = TeamService(),
    ) -> RelationReport[Arena, Team]:
        method = "ArenaService.certify_team_arena_relationship"
        # Handle the case that the arena is not safe.
        arena_validation = arena_validator.validate(candidate_primary)
        if arena_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                ArenaTeamRelationTestFailedException(
                    message=f"{method}: {ArenaTeamRelationTestFailedException.ERROR_CODE}",
                    ex=arena_validation.exception
                )
            )
        arena = cast(Arena, candidate_primary)
        
        # Handle the case that the team is not safe.
        team_validation = team_service.validator.validate(candidate_satellite)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                ArenaTeamRelationTestFailedException(
                    message=f"{method}: {ArenaTeamRelationTestFailedException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        team = cast(Team, candidate_satellite)
        
        # Handle the case that the team should be playing a different arena.
        if arena != team.arena:
            return RelationReport.not_related()
        
        # Find out which slot the team wants to occupy.
        if team.schema.BLACK:
            if arena.black_team is None:
                return RelationReport.partial(satellite=team)
            if arena.black_team == team:
                return RelationReport.bidirectional(primary=arena, satellite=team)
            return RelationReport.failure(
                ArenaTeamRelationTestFailedException(
                    message=f"{method}: {ArenaTeamRelationTestFailedException.ERROR_CODE}",
                    ex=TeamPlayingDifferentArenaException(
                        f"{method}: {ArenaSlotAlreadyOccupiedException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # The default case is for the white team.
        if arena.white_team is None:
            return RelationReport.partial(satellite=team)
        if arena.white_team == team:
            return RelationReport.bidirectional(primary=arena, satellite=team)
        return RelationReport.failure(
            ArenaTeamRelationTestFailedException(
                message=f"{method}: {ArenaTeamRelationTestFailedException.ERROR_CODE}",
                ex=TeamPlayingDifferentArenaException(f"{method}: {ArenaSlotAlreadyOccupiedException.DEFAULT_MESSAGE}")
            )
        )