# src/chess/board/validator/validator.py

"""
Module: chess.board.validator.validator
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from typing import Any, cast

from chess.arena import Arena, ArenaService
from chess.board import (
    Board, BoardNotSubmittedArenaRegistrationException, BoardOwnedByDifferentArenaException, NullBoardException,
    BoardValidationFailedException,
)
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult


class BoardValidator(Validator[Board]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Board instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
        * BoardValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls, candidate: Any,
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Board]:
        """
        # ACTION:
            1.  If the candidate fails existence or type checks send an exception chain in the ValidationResult. Else,
                cast candidate to a Board instance board.
            2.  If the board's name or id fails integrity checks send an exception chain in the ValidationResult.
                Else validate is board using arena_service.
            3.  If the board's arena fails integrity checks send an exception chain in the ValidationResult. 
                Else, the board has been successfully validated. Send it in the ValidationResult's payload.
        # PARAMETERS:
            *   candidate (Any)
            *   arena_service (ArenaService)
            *   identity_service: (IdentityService)
        # RETURNS:
            *   ValidationResult[Board] containing either:
                    - On failure: Exception.
                    - On success: Board in the payload.
        # RAISES:
            *   TypeError
            *   NullBoardException
            *   BoardValidationFailedException
        """
        method = "BoardValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationFailedException(
                    message=f"{method}: {BoardValidationFailedException.ERROR_CODE}",
                    ex=NullBoardException(f"{method}: {NullBoardException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Board):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationFailedException(
                    message=f"{method}: {BoardValidationFailedException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected Board, but, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast candidate to a Board for additional tests. ---#
        board = cast(Board, candidate)
        
        # Handle the case board.id or board.name certification fails.
        identity_validation = identity_service.validate_identity(
            id_candidate=board.id,
            name_candidate=board.name
        )
        if identity_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationFailedException(
                    message=f"{method}: {BoardValidationFailedException.ERROR_CODE}",
                    ex=identity_validation.exception
                )
            )
        # Handle the case that board.arena integrity verification and the arena-board relation fails.
        arena_verification = cls._validate_arena(board=board, arena_service=arena_service)
        if arena_verification.is_failure:
            # Return the exception chain on failure.
            return ValidationResult(
                BoardValidationFailedException(
                    message=f"{method}: {BoardValidationFailedException.ERROR_CODE}",
                    ex=arena_verification.exception
                )
            )
        # --- On certification successes send the board instance in the ValidationResult. ---#
        return ValidationResult.success(payload=board)
                    
    @ classmethod
    @ LoggingLevelRouter.monitor
    def _validate_arena(cls, board: Board, arena_service: ArenaService = ArenaService() ) -> ValidationResult[Arena]:
        """
        # ACTION:
            1.  If board.arena is not validated by arena_service send an exception chain in the ValidationResult.
            2.  If the board is not board.arena send an exception chain in the ValidationResult. Else, board.arena
                has been successfully validated. Send it in the ValidationResult's payload.
        # PARAMETERS:
            *   board (Board)
            *   arena_service (ArenaService)
        # RETURNS:
        ValidationResult[Arena] containing either:
            - On failure: Exception.
            - On success: Area in the payload.
        # RAISES:
        *   BoardValidationFailedException
        """
        
        method = "BoardValidator._validate_arena"
        
        relation_analysis = arena_service.relation_analysis_analyzer.analyze(
            candidate_primary=board.arena,
            candidate_satellite=board,
        )
        # Handle the case that there is a direct failure of analyzer.
        if relation_analysis.is_failure:
            # Return the exception chain on failure.
            return ValidationResult(
                BoardValidationFailedException(
                    message=f"{method}: {BoardValidationFailedException.ERROR_CODE}",
                    ex=relation_analysis.exception
                )
            )
        # Handle the case that the board belongs to a different board.
        if relation_analysis.does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult(
                BoardValidationFailedException(
                    message=f"{method}: {BoardValidationFailedException.ERROR_CODE}",
                    ex=BoardOwnedByDifferentArenaException(
                        f"{method}: {BoardOwnedByDifferentArenaException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the board has not been added to the board's boards.
        if relation_analysis.partially_exists:
            # Return the exception chain on failure.
            return ValidationResult(
                BoardValidationFailedException(
                    message=f"{method}: {BoardValidationFailedException.ERROR_CODE}",
                    ex=BoardNotSubmittedArenaRegistrationException(
                        f"{method}: {BoardNotSubmittedArenaRegistrationException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # On certification successes send the board back to the validator.
        return ValidationResult.success(payload=board.arena)
