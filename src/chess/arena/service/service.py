# src/chess/arena/service/service.py

"""
Module: chess.arena.service.service
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""


from typing import cast

from chess.arena import (
    Arena, ArenaAlreadyContainsTemException, ArenaBuilder, ArenaIsFullException, ArenaServiceException,
    ArenaSlotAlreadyOccupiedException, ArenaValidator,
    TeamPlayingDifferentArenaException
)
from chess.schema import Schema, SchemaService
from chess.system import EntityService, InsertionResult, LoggingLevelRouter, Result, SearchResult, id_emitter
from chess.team import Team, TeamNotSubmittedArenaRegistrationException, TeamService, TeamServiceException


class ArenaService(EntityService[Arena]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Arena microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Arena state.
    4.  Single entry and entry points to Arena lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "ArenaService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: ArenaBuilder = ArenaBuilder(),
            validator: ArenaValidator = ArenaValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (ArenaFactory)
            *   validator (ArenaValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> ArenaBuilder:
        """get ArenaBuilder"""
        return cast(ArenaBuilder, self.entity_builder)
    
    @property
    def validator(self) -> ArenaValidator:
        """get ArenaValidator"""
        return cast(ArenaValidator, self.entity_validator)
    
    
    @LoggingLevelRouter.monitor
    def add_team(self, arena: Arena, team: Team, team_service: TeamService = ()) -> InsertionResult[Team]:
        method = "ArenaService.add_team"
        # Handle the case that the arena is not safe.
        arena_validation = self.validator.validate(arena)
        if arena_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=arena_validation.exception
                )
            )
        # Handle the case that the arena is full.
        if arena.arena_is_full:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=ArenaIsFullException(f"{method}: {ArenaIsFullException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the team is not safe.
        team_validation = team_service.validator.validate(team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        # Handle the case that the team should be playing a different arena.
        if arena != team.arena:
            # Return the exception chain.
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=TeamPlayingDifferentArenaException(
                        f"{method}: {TeamPlayingDifferentArenaException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the team is already in the arena.
        if team in [arena.white_team, arena.black_team]:
            # Return the exception chain.
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=ArenaAlreadyContainsTemException(
                        f"{method}: {ArenaAlreadyContainsTemException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the color slot was already assigned to a different team.
        if (team.schema == Schema.WHITE and arena.white_team_is_assigned) or (
                team.schema == Schema.BLACK and arena.black_team_is_assigned):
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=TeamPlayingDifferentArenaException(
                        f"{method}: {ArenaSlotAlreadyOccupiedException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case of adding the team if its schema is black. Doing them separately avoids concurrency problems
        if team.schema == Schema.BLACK:
            if arena.black_team_is_assigned:
                return InsertionResult.failure(
                    ArenaServiceException(
                        message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                        ex=TeamPlayingDifferentArenaException(
                            f"{method}: {ArenaSlotAlreadyOccupiedException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            arena.black_team = team
            return InsertionResult.success(payload=team)
        # Handle the case of adding the team if its schema is white.
        if team.schema == Schema.WHITE:
            if arena.white_team_is_assigned:
                return InsertionResult.failure(
                    ArenaServiceException(
                        message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                        ex=TeamPlayingDifferentArenaException(
                            f"{method}: {ArenaSlotAlreadyOccupiedException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            arena.white_team = team
            return InsertionResult.success(payload=team)
        
        # Handle the case of adding the team if its schema is white. Doing them separately manages concurrency.
        if team.schema == Schema.WHITE and arena.white_team_is_assigned:
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=TeamPlayingDifferentArenaException(
                        f"{method}: {ArenaSlotAlreadyOccupiedException.DEFAULT_MESSAGE}"
                    )
                )
            )
        else:
            arena.black_team = team
            return InsertionResult.success(payload=team)
        return
        
            
            
    def team_from_schema(
            self,
            arena: Arena,
            schema: Schema,
            schema_service: SchemaService = SchemaService()
    ) -> SearchResult[Team]:
        """"""
        method = "ArenaService.team_from_schema"
        arena_validation = self.validator.validate(arena)
        if arena_validation.is_failure:
            return SearchResult.failure(
                ArenaServiceException(
                    message=f"{method}: {ArenaServiceException.ERROR_CODE}", ex=arena_validation.exception
                )
            )
        schema_validation = schema_service.schema_validator.validate(schema)
        if schema_validation.is_failure:
            return SearchResult.failure(
                ArenaServiceException(
                    message=f"{method}: {ArenaServiceException.ERROR_CODE}", ex=schema_validation.exception
                )
            )
        if self._white_team is not None and schema == self._white_team.schema:
            return SearchResult.success(payload=[self._white_team])
        if self._black_team is not None and schema == self._black_team.schema:
            return SearchResult.success(payload=[self._black_team])
        return SearchResult.empty()
    
    @LoggingLevelRouter.monitor
    def certify_team_arena_relationship(
            self,
            team: Team,
            arena: Arena,
            team_service: TeamService = TeamService(),
    ) -> Result[(Team, Arena)]:
        """
        # ACTION:
            1.  If either the team or arena fail their integrity checks send the exception in the Result.
            2.  If the team belongs in a different arena send the exception in the Result.
            3.  If the team is not occupying a slot inside its arena send the exception in the Result.
            2.  When all checks pass send the (Arena, Team) tuple in the Result.
        # PARAMETERS:
            *   team (Team)
            *   arena (Arena)
            *   team_service (TeamService)
        All Services have default values to ensure they are never null.
        # Returns:
            *   Result[Team] containing either:
                    - On failure: Exception.
                    - On success: (Arena, Team) in the payload.
        RAISES:
            *   ArenaServiceException
            *   TeamPlayingDifferentArenaException
            *   TeamNotSubmittedArenaRegistrationException
        """
        method = "ArenaService.certify_team_arena_relationship"
        # Handle the case that the arena is not safe.
        arena_validation = self.validator.validate(arena)
        if arena_validation.is_failure:
            # Return the exception chain on failure.
            return Result.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=arena_validation.exception
                )
            )
        # Handle the case that the team is not safe.
        team_validation = team_service.validator.validate(team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return Result.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        # Handle the case that the team should be playing a different arena.
        if arena != team.arena:
            # Return the exception chain.
            return Result.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=TeamPlayingDifferentArenaException(
                        f"{method}: {TeamPlayingDifferentArenaException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the team has not occupied its slot.
        if team not in [arena.white_team, arena.black_team]:
            # Return the exception chain.
            return Result.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=TeamNotSubmittedArenaRegistrationException(
                        f"{method}: {TeamNotSubmittedArenaRegistrationException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # On certification success return the related items in the result.
        return Result.success((team, arena))
    

    
    @LoggingLevelRouter.monitor
    def adding_team_precheck(
            self,
            team: Team,
            arena: Arena,
            team_service: TeamService = TeamService(),
    ) -> Result[(Team, Arena)]:
        method = "ArenaService.team_inside_arena"





        return Result.success((team, arena))