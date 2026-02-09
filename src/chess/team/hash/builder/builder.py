# src/chess/team/hash/builder/builder.py

"""
Module: chess.team.hash.builder.builder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from chess.schema import SchemaService
from chess.system import BuildResult, Builder, LoggingLevelRouter
from chess.team import (
    BlackTeamHasWrongSchemaException, Team, TeamHash, TeamHashBuildFailedException,
    TeamSchemaCollisionException, TeamValidator, WhiteTeamHasWrongSchemaException
)


class TeamHashBuilder(Builder[TeamHash]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            white_team: Team,
            black_team: Team,
            team_validator: TeamValidator = TeamValidator(),
            schema_service: SchemaService = SchemaService(),
    ) -> BuildResult[TeamHash]:
        method = "TeamHashBuilder.build"
        
        # Handle the case that the white_team is not certified as safe.
        white_team_validation_result = team_validator.validate(white_team)
        if white_team_validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TeamHashBuildFailedException(
                    message=f"{method}: {TeamHashBuildFailedException.DEFAULT_MESSAGE}",
                    ex=white_team_validation_result.exception
                )
            )
        # Handle the case that the white_team's schema is wrong.
        if white_team.schema != schema_service.schema.WHITE:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TeamHashBuildFailedException(
                    message=f"{method}: {TeamHashBuildFailedException.DEFAULT_MESSAGE}",
                    ex=WhiteTeamHasWrongSchemaException(
                        f"{method}: {WhiteTeamHasWrongSchemaException.DEFAULT_MESSAGE}",
                    )
                )
            )
        # Handle the case that the black_team's schema is wrong.
        if black_team.schema != schema_service.schema.WHITE:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TeamHashBuildFailedException(
                    message=f"{method}: {TeamHashBuildFailedException.DEFAULT_MESSAGE}",
                    ex=BlackTeamHasWrongSchemaException(
                        f"{method}: {BlackTeamHasWrongSchemaException.DEFAULT_MESSAGE}",
                    )
                )
            )
        # If there are more than two schemas handle the case that the both teams have the same schema.
        if black_team.schema == white_team.schema:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TeamHashBuildFailedException(
                    message=f"{method}: {TeamHashBuildFailedException.DEFAULT_MESSAGE}",
                    ex=TeamSchemaCollisionException(
                        f"{method}:{TeamSchemaCollisionException.DEFAULT_MESSAGE}",
                    )
                )
            )
        return BuildResult.success( payload=TeamHash(white_team=white_team, black_team=black_team))