# src/chess/team/builder.builder.py

"""
Module: chess.team.builder.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.piece import UniquePieceDataService

from chess.arena.service.exception.schema import ArenaDuplicateSchemaException
from chess.dyad import SchemaAgentPair
from chess.schema import Schema, SchemaLookup
from chess.agent import PlayerAgent, AgentService
from chess.arena import (
    Arena, ArenaAlreadyContainsTemException, ArenaService, ArenaSlotAlreadyOccupiedException,
    ExcessiveTeamsInArenaException
)
from chess.team import (
    AddingDuplicateTeamException, Team, TeamBuildFailedException, TeamContext, TeamInsertionFailedException,
    TeamNotSubmittedArenaRegistrationException
)
from chess.system import (
    Builder, BuildResult, IdentityService, InsertionResult, LoggingLevelRouter, ValidationResult,
    id_emitter
)


class TeamBuilder(Builder[Team]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

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
            schema_owner: SchemaAgentPair,
            id: int = id_emitter.team_id,
            schema_lookup: SchemaLookup = SchemaLookup(),
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
            owner_service: AgentService = AgentService(),
    ) -> BuildResult[Team]:
        """
        # ACTION:
            1.  If any parameters fail their integrity checks send the exception in the BuildResult..
            2.  When all checks pass send create the Team instance and send in the BuildResult.
        # PARAMETERS:
            *   id (int)
            *   owner (PlayerAgent)
            *   team_schema (Schema)
            *   identity_service (IdentityService)
            *   owner_service (AgentService)
            *   schema_validator (TeamSchemaValidator)
        All Services have default values to ensure they are never null.
        # Returns:
            *BuildResult[Team] containing either:
                - On failure: Exception.
                - On success: Team in the payload.
        RAISES:
            *   TeamBuildFailedException
        """
        method = "TeamBuilder.builder"
        try:
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
            schema_validation = schema_lookup.schema_validator.validate(schema_owner.schema)
            if schema_validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    TeamBuildFailedException(
                        message=f"{method}: {TeamBuildFailedException.ERROR_CODE}", ex=schema_validation.exception
                    )
                )
            # Handle the case owner certification fails.
            owner_validation = owner_service.validator.validate(schema_owner.agent)
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
                schema=schema_owner.schema,
                owner=schema_owner.agent,
                roster=UniquePieceDataService(),
                hostages=UniquePieceDataService(),
            )
            
            # Make sure the owning side of the team-owner relationship is set.
            insertion_result = cls._register_team_with_agent(agent=schema_owner.owner, team=team)
            if insertion_result.is_failure:
                return BuildResult.failure(insertion_result.exception)
            
            # Make sure the owning side of the tea-arena relationship is set.
            insertion_result = cls._insert_team_in_arena(arena=arena, team=team)
            if insertion_result.is_failure:
                return BuildResult.failure(insertion_result.exception)
                
            # Send the successfully built and registered Team object inside a BuildResult.
            return BuildResult.success(team)
        
        # Finally return a BuildResult containing any unhandled exception insided an
        # TeamBuildFailedException
        except Exception as ex:
            return BuildResult.failure(
                TeamBuildFailedException(ex=ex, message=f"{method}: {TeamBuildFailedException.DEFAULT_MESSAGE}")
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _certify_arena(
            cls,
            arena: Arena,
            team: Team,
            arena_service: ArenaService = ArenaService()
    ) -> ValidationResult[Arena]:
        """"""
        method = "TeamBuilder._certify_arena"
        # Handle the case arena certification fails.
        arena_validation = arena_service.item_validator.validate(arena)
        if arena_validation.is_failure:
            return ValidationResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}", ex=arena_validation.exception
                )
            )
        # Handle the case that the Arena is full.
        if arena.arena_is_full:
            return ValidationResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}",
                    ex=ExcessiveTeamsInArenaException(f"{method} : {ExcessiveTeamsInArenaException.DEFAULT_MESSAGE}")
                )
            )
        # Test if the team in not relatable to the arena.
        relationship_certification = arena_service.certify_team_arena_relationship(team=team, arena=arena)
        if relationship_certification.exception == TeamNotSubmittedArenaRegistrationException or
            relationship_certification.exception = TeamNotSubmittedArenaRegistrationException
        # Handle the case that the color slot is already assigned.
        if (
                (schema == schema.WHITE and arena.white_team is not None) or
                (schema == schema.BLACK and arena.black_team is not None)
        ):
            return ValidationResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}",
                    ex=ArenaSlotAlreadyOccupiedException(f"{method} : {ArenaSlotAlreadyOccupiedException.DEFAULT_MESSAGE}")
                )
            )
        return ValidationResult.success(arena)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _register_team_with_owner(cls, team: Team, owner: PlayerAgent, ) -> InsertionResult[Team]:
        """
        # ACTION:
            1.  If team does not exist in the owner's team_assignments return the push result. Else,
                send an exception in the InsertionResult.
        # PARAMETERS:
            *   team (Team)
            *   owner (PlayerAgent)
        # Returns:
            *   InsertionResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        RAISES:
            *   AddingDuplicateTeamException
        """
        method = "TeamBuilder._register_team_with_agent"
        # As a concurrency safety check need to handle the case that the team is already registered
        # with the owner
        search = owner.team_assignments.search_teams(context=TeamContext(id=team.id))
        
        # Handle the case the search raised an error.
        if search.is_failure:
            return InsertionResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}", ex=search.exception
                )
            )
        # If the search gives a hit the Team has already been created. Send an error in the InsertionResult.
        if search.is_success:
            return InsertionResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}",
                    ex=AddingDuplicateTeamException(f"{method}: {AddingDuplicateTeamException.DEFAULT_MESSAGE}")
                )
            )
        # Execute the insertion when the search came up empty.
        return owner.team_assignments.add_team(team)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _insert_team_in_arena(cls, arena: Arena, team: Team, arena_service: ArenaService) -> InsertionResult[Team]:
        """
        # ACTION:
        1.  After ensuring the team does not exist in the PlayerAgent's team_assignments push the Team onto the stack.

        # PARAMETERS:
            *   team (Team)
            *   agent (PlayerAgent)

        # Returns:
        InsertionResult[Team] containing either:
            - On success: Team in the payload.
            - On failure: Exception.

        RAISES:
            *   AddingDuplicateTeamException
            *   TeamInsertionFailedException
        """
        method = "TeamBuilder._insert_team_in_arena"
        # As a concurrency safety check need to handle the case that the team is already registered
        # with the owner
        if team in [arena.white_team, arena.black_team]:
            return InsertionResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}",
                    ex=ArenaAlreadyContainsTemException(f"{method}: {ArenaAlreadyContainsTemException.DEFAULT_MESSAGE}")
                )
            )
        search_result = arena_service.team_from_schema(arena, team.schema)
        if search_result.is_failure:
            return InsertionResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        if search_result.is_success and search_result.payload != team:
            return InsertionResult.failure(
                TeamBuildFailedException(
                    message=f"{method}: {TeamBuildFailedException.ERROR_CODE}",
                    ex=ArenaSlotAlreadyOccupiedException(f"{method}: {ArenaAlreadyContainsTemException.DEFAULT_MESSAGE}")
                )
            )
        
        