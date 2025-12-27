# src/chess/arena/service/service.py

"""
Module: chess.arena.service.service
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""


from typing import cast

from chess.arena import Arena, ArenaBuilder, ArenaServiceException, ArenaValidator
from chess.system import EntityService, LoggingLevelRouter, Result, id_emitter
from chess.team import Team, TeamNotInsideArenaException, TeamService, TeamServiceException


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
    def team_inside_arena(
            self,
            team: Team,
            arena: Arena,
            team_service: TeamService = TeamService(),
    ) -> Result[(Team, Arena)]:
        method = "ArenaService.team_inside_arena"
        arena_validation = self.validator.validate(arena)
        if arena_validation.is_failure:
            return Result.failure(
                ArenaServiceException(
                    message=f"{method}: {ArenaServiceException.ERROR_CODE}", ex=arena_validation.exception
                )
            )
        team_validation = team_service.validator.validate(team)
        if team_validation.is_failure:
            return Result.failure(
                ArenaServiceException(
                    message=f"{method}: {ArenaServiceException.ERROR_CODE}", ex=team_validation.exception
                )
            )
        if team.arena != arena:
            return Result.failure(
                ArenaServiceException(
                    message=f"{method}: {ArenaServiceException.ERROR_CODE}",
                    ex=TeamInsideDifferentArenaException(f"{method}: {TeamInsideDifferentArenaException.ERROR_MESSAGE}")
                )
            )
        if team not in [arena.white_team, arena.black_team]:
            return Result.failure(
                TeamServiceException(
                    message=f"{method}: {TeamServiceException.ERROR_CODE}",
                    ex=TeamNotInsideArenaException(f"{method} {TeamNotInsideArenaException.DEFAULT_MESSAGE}")
                )
            )
        return Result.success((team, arena))