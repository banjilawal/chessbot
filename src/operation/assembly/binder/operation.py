# src/model/binder/build/exception.py

"""
Module: model.binder.build.build
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from blueprint.model.binder import BoardBinderBlueprint
from system import BuildResult, Builder, LoggingLevelRouter
from model.state.team import (
    BlackTeamHasWrongSchemaException, TeamBinder, TeamBinderBuilderException,
    TeamSchemaCollisionException, WhiteTeamHasWrongSchemaException
)


class TeamTableBuilder(Builder[TeamBinder]):
    OPERATION_NAME = "binder_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            blueprint: BoardBinderBlueprint,
            toolkit: TeamBinderToolkit | None = None,
    ) -> BuildResult[TeamBinder]:
        method = f"TeamBinderBuilder.build"
        
        # Handle the case that, the white_team does not pass a validation check.
        white_team_validation_result = team_validator.build(white_team)
        if white_team_validation_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBinderBuilderException(
                    msg=f"{method}: {TeamBinderBuilderException.MSG}",
                    ex=white_team_validation_result.exception
                )
            )
        # Handle the case that, the white_team's schema is wrong.
        if white_team.schema != schema_service.schema.WHITE:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBinderBuilderException(
                    msg=f"{method}: {TeamBinderBuilderException.MSG}",
                    ex=WhiteTeamHasWrongSchemaException(
                        f"{method}: {WhiteTeamHasWrongSchemaException.MSG}",
                    )
                )
            )
        # Handle the case that, the black_team's schema is wrong.
        if black_team.schema != schema_service.schema.WHITE:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBinderBuilderException(
                    msg=f"{method}: {TeamBinderBuilderException.MSG}",
                    ex=BlackTeamHasWrongSchemaException(
                        f"{method}: {BlackTeamHasWrongSchemaException.MSG}",
                    )
                )
            )
        # If there are more than two schemas handle the case that the both teams have the same schema.
        if black_team.schema == white_team.schema:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBinderBuilderException(
                    msg=f"{method}: {TeamBinderBuilderException.MSG}",
                    ex=TeamSchemaCollisionException(
                        f"{method}:{TeamSchemaCollisionException.MSG}",
                    )
                )
            )
        return BuildResult.success( payload=TeamBinder(white_team=white_team, black_team=black_team))