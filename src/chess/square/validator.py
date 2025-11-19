# src/chess/square/coord_stack_validator.py

"""
Module: chess.square.coord_stack_validator
Author: Banji Lawal
Created: 2025-09-11
"""

from typing import Any, cast

from chess.coord import CoordService, CoordValidator
from chess.piece import Piece, PieceValidator
from chess.square import (
    InvalidPieceSquareRelationException, PieceInconsistentSquareOccupationException, Square, InvalidSquareException,
    NullSquareException, SquareAndPieceMismatchedCoordException
)
from chess.system import IdentityService, Validator, ValidationResult, NameValidator, LoggingLevelRouter, IdValidator


class SquareValidator(Validator[Square]):
    """
    # ROLE: Validation, Verify Data Integrity

    # RESPONSIBILITIES:
    1.  Verifies a candidate is an instance of Square, that meets integrity requirements, before
        the candidate is used.
    2.  Verify an actionable Piece is bound to a Square before the Piece object is used.

    # PROVIDES:
    ValidationResult[Coord] containing either:
        - On success: Coord in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            coord_service: type[CoordService]=CoordService,
            identity_service: type[IdentityService]=IdentityService,
    ) -> ValidationResult[Square]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check if candidate is a Square.
        3.  Run id and name integrity checks with identity_service
        4.  Run coord integrity checks with coord_service.
        5  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass cast candidate to a Square instance, then return inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any): Object to validate.
            *   coord_service (type[CoordService])=CoordService
            *   identity_service: type[IdentityService]=IdentityService
        coord_service and identity_service have default values.

        # Returns:
        ValidationResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        # RAISES:
            * TypeError
            * NullSquareException
            * InvalidSquareException
        """
        method = "SquareValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullSquareException(f"{method}: {NullSquareException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Square):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Square, but got {type(candidate).__name__} instead.")
                )
            
            square = cast(Square, candidate)
            
            identity_validation = identity_service.validate_identity(
                id_candidate=square.id,
                name_candidate=square.name
            )
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            coord_validation = coord_service.validate_as_coord(square.coord)
            if coord_validation.is_failure():
                return ValidationResult.failure(coord_validation.exception)
            
            return ValidationResult.success(payload=square)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSquareException(
                    f"{method}: {InvalidSquareException.DEFAULT_MESSAGE}",
                    ex
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_piece_square_binding(
            cls, 
            square_candidate: Any, 
            piece_candidate: Any,
            piece_validator: type[PieceValidator]=PieceValidator
    ) -> ValidationResult[Square, Piece]:
        """
        # Action:
        Verify there is a relationship between an actionable piece and a square before, they
        are used in conjunction in the system.

        # Parameters:
            * square_candidate (Any): The object to verify is a Square instance.
            * piece_candidate (Any): The object to verify is an active Piece instance.
            * piece_service (type[PieceValidator])=PieceService

        # Returns:
          ValidationResult[(Square, Piece)] containing either:
                - On success: Tuple(Square, Piece) in the payload.
                - On failure: Exception.

        # Raises:
            * SquareAndPieceMismatchedCoordException
            * PieceInconsistentSquareOccupationException
        """
        """
        # ACTION:
        1.  SquareValidator.validate runs integrity checks on square_candidate.
        2.  piece_service verifies piece_candidate is an active piece on the board.
        3.  After casting the candidates into square and piece test square.coord == piece.current_position.
        4.  Test square.occupant == piece.
        5   If any check fails, return the exception inside a ValidationResult.
        6.  When all pass tuple(square, piece) to sender in a ValidationResult.

        # PARAMETERS:
            *   candidate_square (Any): Object to validate as a Square.
            *   candidate_piece (Any): object to validate as an active Piece
            *   piece_service (ype[PieceService])

        # Returns:
        ValidationResult[(Square, Piece)] containing either:
            - On success: tuple(Square, Piece) in the payload.
            - On failure: Exception.

        # RAISES:
            * TypeError
            * NullSquareException
            * InvalidSquareException
        """
        method = "SquareValidator.validate_piece_square_binding"
        
        try:
            square_verification = cls.validate(square_candidate)
            if square_verification.is_failure():
                return ValidationResult.failure(square_verification.exception)
            
            square = cast(Square, square_candidate)
            
            piece_verification = piece_validator.validate_piece_is_actionable(piece_candidate)
            if piece_verification.is_failure():
                return ValidationResult.failure(piece_verification.exception)
            
            piece = cast(Piece, piece_candidate)
            
            if square.coord != piece.current_position:
                return ValidationResult.failure(
                    SquareAndPieceMismatchedCoordException(
                        f"{method} {SquareAndPieceMismatchedCoordException.DEFAULT_MESSAGE}"
                    )
                )
            
            if square.occupant != piece:
                return ValidationResult.failure(
                    PieceInconsistentSquareOccupationException(
                        f"{method} {PieceInconsistentSquareOccupationException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=(square, piece))
            
        except Exception as e:
            return ValidationResult.failure(
                InvalidPieceSquareRelationException(
                    f"{method}: {InvalidPieceSquareRelationException.DEFAULT_MESSAGE}", e
                )
            )