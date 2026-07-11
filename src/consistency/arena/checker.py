# src/logic/arena/consistency/consistency.py

"""
Module: logic.arena.validation
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from typing import Any, cast

from logic.board import BoardService
from logic.team import Team, UniqueTeamDataService
from logic.arena import Arena, ArenaConsistencyCheckerException, NullArenaException, ArenaTeamsInArenaException
from system import (
    IdentityService, LoggingLevelRouter, SearchResult, ServiceConsistency, ValidationResult,
    Consistency
)



class ArenaConsistencyChecker(ConsistencyChecker[Arena]):
    """
    Role:Validation, Data Integrity And Reliability Guarantor

    Responsibilities:
    1.  Produce Arena instances whose integrity is guaranteed at creation.
    2.  Manage construction of Arena instances that can be used safely by the client.
    3.  Ensure params for Arena creation have met the application's safety contract.
    4.  Return an exception to the client if a Validation resource does not satisfy integrity requirements.

    Super Class:
        *   Validation

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    OPERATION_NAME = "arena_consistency"
    
    @classmethod
    def validate(
            cls,
            candidate: Any,
            board_service: BoardService = BoardService(),
            identity_service: IdentityService = IdentityService(),
            service_consistency: ServiceConsistency = ServiceConsistencyChecker(),
    ) -> SearchResult[Arena]:
        """
        # ACTION:
        1.  verify arena_variety is a not-null ArenaVariety object.
        2.  Use arena_variety to pick which Validation method will create the concrete Arena object.

        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   arena_variety (ArenaVariety)
            *   engine_service (Optional[EngineService])

        # RETURN:
        ValidationResult[Arena] containing either:
            - On success: Arena in the payload.
            - On failure: Exception.

        Raises:
            *   ArenaConsistencyCheckerException
        """
        method = "ArenaConsistency.execute"
        try:
            # If rank does not exist no point continuing
            if candidate is None:
                return ValidationResult.failure(
                    NullArenaException(f"{method}: {NullArenaException.MSG}")
                )
            # Handle the case, the rank is not an Arena object.
            if not isinstance(candidate, Arena):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Arena, {type(candidate).__name__} instead.")
                )
            # Cast to an Arena for additional processing.
            arena = cast(Arena, candidate)
            
            # Verify the id is safe.
            id_validation = identity_service.validate_id(candidate=id)
            if id_consistency.failure:
                return ValidationResult.failure(id_consistency.exception)
             
            # Verify the board.
            board_consistency = board_service.run.build(arena.board)
            if board_consistency.failure:
                return ValidationResult.failure(board_consistency.exception)
            
            # Verify the team service exists and is the right type.
            team_service_validation = service_consistency.search_service(arena.team_service)
            if team_service_consistency.failure:
                return ValidationResult.failure(team_service_consistency.exception)
            
            if arena.team_service.size < 2:
                return ValidationResult.failure(
                    NotEnoughTeamsInArenaException(f"{method}: {NotEnoughTeamsInArenaException.MSG}")
                )
            
            if arena.team_service.size > 2:
                return ValidationResult.failure(
                    ArenaTeamsInArenaException(f"{method}: {ArenaTeamsInArenaException.MSG}")
                )
            
            if arena.black_team == arena.white_team:
                return ValidationResult.failure(
                    ArenaTeamDuplicationException(f"{method}: {ArenaTeamDuplicationException.MSG}")
                )
            
            if arena.black_team.schema.color == arena.white_team.schema.color:
                return ValidationResult.failure(
                    ArenaTeamColorCollisionException(f"{method}: {ArenaTeamColorCollisionException.MSG}")
                )
            
            if arena.black_team.model_class == arena.white_team.model_class:
                return ValidationResult.failure(
                    ArenaTeamPlayerCollisionException(f"{method}: {ArenaTeamPlayerCollisionException.MSG}")
                )
            
            # When the checks pass Validation the Arena object.
            return ValidationResult.success(arena)
        
        # The flow should only get here if the logic did not route all the types of concrete Arenas.
        # In that case wrap the unhandled exception inside an ArenaConsistencyCheckerException then, return
        # the exception chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                ArenaConsistencyCheckerException(
                    ex=ex, msg=f"{method}: {ArenaConsistencyCheckerException.MSG}"
                )
            )