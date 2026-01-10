# src/chess/team/builder/builder.py

"""
Module: chess.team.builder.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.arena import Arena, ArenaService
from chess.schema import Schema, SchemaService
from chess.token import UniquePieceDataService
from chess.agent import PlayerAgent, AgentService
from chess.team import Team, TeamBuildFailedException
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter, id_emitter



class TeamBuilder(Builder[Team]):
    """
     # ROLE: Builder, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce Team instances whose integrity is guaranteed at creation.
     2.  Manage construction of Team instances that can be used safely by the client.
     3.  Ensure params for Team creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
     None

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            arena: Arena,
            schema: Schema,
            owner: PlayerAgent,
            id: int = id_emitter.team_id,
            arena_service: ArenaService = ArenaService(),
            owner_service: AgentService = AgentService(),
            schema_service: SchemaService = SchemaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Team]:
        """
        # ACTION:
            1.  If any parameters fail their integrity checks send the exception in the BuildResult..
            2.  When all checks pass send create the Team instance and send in the BuildResult.
        # PARAMETERS:
            *   id (int)
            *   arena (Arena)
            *   schema (Schema)
            *   owner (Player)
            *   arena_service (ArenaService)
            *   owner_service (AgentService)
            *   schema_service(TeamSchemaValidator)
            *   identity_service (IdentityService)

        All Services have default values to ensure they are never null.
        # RETURNS:
            *BuildResult[Team] containing either:
                - On failure: Exception.
                - On success: Team in the payload.
        RAISES:
            *   TeamBuildFailedException
        """
        method = "TeamBuilder.builder"
        # Handle the case id certification fails
        id_validation = identity_service.validate_id(id)
        # Return the exception chain on failure.
        if id_validation.is_failure:
            return BuildResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}", ex=id_validation.exception
                )
            )
        # Handle the case schema certification fails.
        schema_validation = schema_service.schema_validator.validate(schema)
        if schema_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}", ex=schema_validation.exception
                )
            )
        # Handle the case owner certification fails.
        owner_validation = owner_service.validator.validate(owner)
        if owner_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}", ex=owner_validation.exception
                )
            )
        # If no errors are detected build the Team object.
        team = Team(
            id=id,
            arena=arena,
            schema=schema,
            owner=owner,
            roster=UniquePieceDataService(),
            hostages=UniquePieceDataService(),
        )
        # Push the team onto the owner's stack.
        insertion_result = owner_service.push_team_to_player(agent=owner, team=team)
        if insertion_result.is_failure:
            # If the push failed return the exception chain.
            return BuildResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}", ex=owner_validation.exception
                )
            )
        # Put the team in the arena.
        insertion_result = arena_service.add_team(arena=arena, team=team)
        if insertion_result.is_failure:
            # If arena entry fails return the exception chain.
            return BuildResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}", ex=owner_validation.exception
                )
            )
        # After the team is registered with its owner and entered the arena send it in the BuildResult.
        return BuildResult(team)