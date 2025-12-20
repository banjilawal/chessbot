# src/chess/arena/validator/number_bounds_validator.py

"""
Module: chess.arena.validator.number_bounds_validator
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""
from typing import Any, cast

from chess.board import BoardService
from chess.team import Team, UniqueTeamDataService
from chess.arena import Arena, ArenaValidationFailedException, NullArenaException, ExcessiveTeamsInArenaException
from chess.system import (
    IdentityService, LoggingLevelRouter, SearchResult, ServiceValidator, ValidationResult,
    Validator
)



class ArenaValidator(Validator[Arena]):
    """
    # ROLE: Validationer, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce Arena instances whose integrity is always guaranteed.
    2.  Manage construction of Arena instances that can be used safely by the client.
    3.  Ensure params for Arena creation have met the application's safety contract.
    4.  Return an exception to the client if a Validation resource does not satisfy integrity requirements.

    # PARENT:
        *   Validationer

    # PROVIDES:
        *   ArenaValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    def validate(
            cls,
            candidate: Any,
            board_service: BoardService = BoardService(),
            identity_service: IdentityService = IdentityService(),
            service_validator: ServiceValidator = ServiceValidator(),
    ) -> SearchResult[Arena]:
        """
        # ACTION:
        1.  verify arena_variety is a not-null ArenaVariety object.
        2.  Use arena_variety to pick which Validationer method will create the concrete Arena object.

        # PARAMETERS:
            *   id (int)
            *   designation (str)
            *   arena_variety (ArenaVariety)
            *   engine_service (Optional[EngineService])

        # Returns:
        ValidationResult[Arena] containing either:
            - On success: Arena in the payload.
            - On failure: Exception.

        # Raises:
            *   ArenaValidationFailedException
        """
        method = "ArenaValidator.validate"
        try:
            # If candidate does not exist no point continuing
            if candidate is None:
                return ValidationResult.failure(
                    NullArenaException(f"{method}: {NullArenaException.DEFAULT_MESSAGE}")
                )
            # Handle the case, the candidate is not an Arena object.
            if not isinstance(candidate, Arena):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Arena, {type(candidate).__name__} instead.")
                )
            # Cast to an Arena for additional processing.
            arena = cast(Arena, candidate)
            
            # Verify the id is safe.
            id_validation = identity_service.validate_id(candidate=id)
            if id_validation.failure:
                return ValidationResult.failure(id_validation.exception)
             
            # Verify the board.
            board_validation = board_service.validator.validate(arena.board)
            if board_validation.failure:
                return ValidationResult.failure(board_validation.exception)
            
            # Verify the team service exists and is the right type.
            team_service_validation = service_validator.validate(arena.team_service)
            if team_service_validation.failure:
                return ValidationResult.failure(team_service_validation.exception)
            
            if arena.team_service.size < 2:
                return ValidationResult.failure(
                    NotEnoughTeamsInArenaException(f"{method}: {NotEnoughTeamsInArenaException.DEFAULT_MESSAGE}")
                )
            
            if arena.team_service.size > 2:
                return ValidationResult.failure(
                    ExcessiveTeamsInArenaException(f"{method}: {ExcessiveTeamsInArenaException.DEFAULT_MESSAGE}")
                )
            
            if arena.black_team == arena.white_team:
                return ValidationResult.failure(
                    ArenaTeamDuplicationException(f"{method}: {ArenaTeamDuplicationException.DEFAULT_MESSAGE}")
                )
            
            if arena.black_team.schema.color == arena.white_team.schema.color:
                return ValidationResult.failure(
                    ArenaTeamColorCollisionException(f"{method}: {ArenaTeamColorCollisionException.DEFAULT_MESSAGE}")
                )
            
            if arena.black_team.player_agent == arena.white_team.player_agent:
                return ValidationResult.failure(
                    ArenaTeamPlayerCollisionException(f"{method}: {ArenaTeamPlayerCollisionException.DEFAULT_MESSAGE}")
                )
            
            # When the checks pass Validation the Arena object.
            return ValidationResult.success(arena)
        
        # The flow should only get here if the logic did not route all the types of concrete Arenas.
        # In that case wrap the unhandled exception inside an ArenaValidationFailedException then, return
        # the exception chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                ArenaValidationFailedException(
                    ex=ex, message=f"{method}: {ArenaValidationFailedException.DEFAULT_MESSAGE}"
                )
            )