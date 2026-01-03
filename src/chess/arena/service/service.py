# src/chess/arena/service/service.py

"""
Module: chess.arena.service.service
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""


from typing import cast

from chess.arena import (
    Arena, ArenaAlreadyContainsTeamException, ArenaBuilder, ArenaServiceException,
    ArenaTeamRelationAnalyzer, ArenaValidator, ChangingArenaTeamBlockedException, TeamPlayingDifferentArenaException
)
from chess.schema import Schema, SchemaService
from chess.system import EntityService, InsertionResult, LoggingLevelRouter, Result, SearchResult, id_emitter
from chess.team import Team, TeamService


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
    _arena_team_relation_analyzer: ArenaTeamRelationAnalyzer
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: ArenaBuilder = ArenaBuilder(),
            validator: ArenaValidator = ArenaValidator(),
            team_relation_tester: ArenaTeamRelationAnalyzer = ArenaTeamRelationAnalyzer(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (ArenaFactory)
            *   validator (ArenaValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._arena_team_relation_analyzer = team_relation_tester
    
    @property
    def builder(self) -> ArenaBuilder:
        """get ArenaBuilder"""
        return cast(ArenaBuilder, self.entity_builder)
    
    @property
    def validator(self) -> ArenaValidator:
        """get ArenaValidator"""
        return cast(ArenaValidator, self.entity_validator)
    
    @property
    def arena_team_relation_analyzer(self) -> ArenaTeamRelationAnalyzer:
        return self._arena_team_relation_analyzer
    
    
    @LoggingLevelRouter.monitor
    def add_team(self, arena: Arena, team: Team, team_service: TeamService = ()) -> InsertionResult[Team]:
        method = "ArenaService.add_team"
        relation = self._arena_team_relation_analyzer.analyze(
            candidate_primary=arena,
            candidate_satellite=team,
            arena_validator=self.validator,
            team_service=team_service,
        )
        # Handle the case that one of the parties fails validation.
        if relation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=relation.exception
                )
            )
        # Handle the case that the team should be playing a different arena.
        if relation.does_not_exist:
            # Return the exception chain.
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=TeamPlayingDifferentArenaException(
                        f"{method}: {TeamPlayingDifferentArenaException.DEFAULT_MESSAGE}"
                    )
                )
            )
        if relation.fully_exists:
            # Return the exception chain.
            return InsertionResult.failure(
                ArenaServiceException(
                    message=f"ServiceId:{self.id} {method}: {ArenaServiceException.ERROR_CODE}",
                    ex=ArenaAlreadyContainsTeamException(
                        f"{method}: {ArenaAlreadyContainsTeamException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Can add if the relation partially exists.
        if team.schema.BLACK and not arena.black_team_is_assigned:
            arena.black_team = team
            return InsertionResult.success(arena.black_team)
        if team.schema.WHITE and not arena.white_team_is_assigned:
            return InsertionResult.success(arena.white_team)
        return InsertionResult.failure(
            ArenaServiceException(
                message=f"ServiceId:{self.id}, {method}: {ArenaServiceException.ERROR_CODE}",
                ex=ChangingArenaTeamBlockedException(f"{method}: {ChangingArenaTeamBlockedException.DEFAULT_MESSAGE}")
            )
        )
        
            
            
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
        # RETURNS:
            *   Result[Team] containing either:
                    - On failure: Exception.
                    - On success: (Arena, Team) in the payload.
        RAISES:
            *   ArenaServiceException
            *   TeamPlayingDifferentArenaException
            *   TeamNotSubmittedArenaRegistrationException
        """

    

    
    @LoggingLevelRouter.monitor
    def adding_team_precheck(
            self,
            team: Team,
            arena: Arena,
            team_service: TeamService = TeamService(),
    ) -> Result[(Team, Arena)]:
        method = "ArenaService.team_inside_arena"





        return Result.success((team, arena))