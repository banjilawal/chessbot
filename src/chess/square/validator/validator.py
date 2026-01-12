# src/chess/square/validator/validator.py

"""
Module: chess.square.validator
Author: Banji Lawal
Created: 2025-09-11
"""

from typing import Any, cast

from chess.board import Board, BoardService
from chess.coord import CoordService, CoordValidator
from chess.piece import Piece, PieceValidator
from chess.square import (
    InvalidPieceSquareRelationException, PieceInconsistentSquareOccupationException, Square, SquareValidationFailedException,
    NullSquareException, SquareAndPieceMismatchedCoordException
)
from chess.system import IdentityService, Validator, ValidationResult, NameValidator, LoggingLevelRouter, IdValidator


class SquareValidator(Validator[Square]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Square instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Square]:
        """
        # ACTION:
            1.  If the candidate fails existence or type checks send an exception chain in the ValidationResult. Else,
                cast candidate to a Square instance square.
            2.  If the square's name or id fails integrity checks send an exception chain in the ValidationResult.
                Else validate is coord using coord_service.
            3.  If coord fails integrity checks send an exception chain in the ValidationResult. Else validate its
                board using board_service.
            4.  If board fails integrity checks send an exception chain in the ValidationResult. Else return square.
                in the ValidationResult payload.
        # PARAMETERS:
            *   candidate (Any)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   identity_service: (IdentityService)
        # RETURNS:
            *   ValidationResult[Square] containing either:
                - On failure: Exception.
                - On success: Coord in the payload.
        # RAISES:
            * TypeError
            * NullSquareException
            * SquareValidationFailedException
        """
        method = "SquareValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationFailedException(
                    message=f"{method}: {SquareValidationFailedException.ERROR_CODE}",
                    ex=NullSquareException(f"{method}: {NullSquareException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Square):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationFailedException(
                    message=f"{method}: {SquareValidationFailedException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected Square, but, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast candidate to a Square for additional tests ---#
        square = cast(Square, candidate)
        
        # Handle the case square.id or square.name certification fails.
        identity_validation = identity_service.validate_identity(
            id_candidate=square.id,
            name_candidate=square.name
        )
        if identity_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationFailedException(
                    message=f"{method}: {SquareValidationFailedException.ERROR_CODE}",
                    ex=identity_validation.exception
                )
            )
        # Handle the case square.coord is not certified safe.
        coord_validation = coord_service.validator.validate(candidate=square.coord)
        if coord_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationFailedException(
                    message=f"{method}: {SquareValidationFailedException.ERROR_CODE}",
                    ex=coord_validation.exception
                )
            )
        # Handle the case that square.board safety and relation validation fails.
        board_verification = cls._validate_board(square=square, board_service=board_service)
        if board_verification.is_failure:
            # Return the exception chain on failure.
            return ValidationResult(
                SquareValidationFailedException(
                    message=f"{method}: {SquareValidationFailedException.ERROR_CODE}",
                    ex=board_verification.exception
                )
            )
        # On certification successes send the square instance in the ValidationResult.
        return ValidationResult.success(payload=square)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_board(cls, square: Square, board_service: BoardService = BoardService()) -> ValidationResult[Board]:
        """
        # ACTION:
            1.  If square.board is not validated by board_service return validation exception.
            2.  If the square is not board.squares return an exception in the ValidationResult.
            3.  The tests passed. Send square.board in the ValidationResult.
        # PARAMETERS:
            *   square (Square)
            *   board_service (BoardService)
        # RETURNS:
        ValidationResult[Board] containing either:
            - On failure: Exception.
            - On success: Board in the payload.
        # RAISES:
            *   SquareValidationFailedException
        """
        method = "SquareValidator._validate_board"
        # Handle the case square.board certification fails.
        board_square_relation = board_service.board_square_relation_analyzer.analyze(
            candidate_primary=square.board,
            candidate_satellite=square,
        )
        # Handle the case that there is a direct failure of analyzer.
        if board_square_relation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult(
                SquareValidationFailedException(
                    message=f"{method}: {SquareValidationFailedException.ERROR_CODE}",
                    ex=board_square_relation.exception
                )
            )
        # Handle the case that the square belongs to a different board.
        if board_square_relation.does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult(
                SquareValidationFailedException(
                    message=f"{method}: {SquareValidationFailedException.ERROR_CODE}",
                    ex=SquareBelongsToDifferentBoardException(
                        f"{method}: {SquareValidationFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the square has not been added to the board's squares.
        if board_square_relation.partially_exists:
            # Return the exception chain on failure.
            return ValidationResult(
                SquareValidationFailedException(
                    message=f"{method}: {SquareValidationFailedException.ERROR_CODE}",
                    ex=SquareNotSubmitedBoardRegistrationException(
                        f"{method}: {SquareNotSubmitedBoardRegistrationException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # On certification successes send the board back to the validator.
        return ValidationResult.success(payload=square.board)
