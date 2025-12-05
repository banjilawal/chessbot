# src/chess/square/validator/validator.py

"""
Module: chess.square.validator.validator
Author: Banji Lawal
Created: 2025-09-11
"""

from typing import Any, cast

from chess.board import BoardIntegrityService
from chess.coord import CoordIntegrityService, CoordValidator
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
    
    # CONSTRUCTOR:
    Default Constructor
    
    # CLASS METHODS:
           validate(
                candidate: Any, board_service: BoardIntegrityService, coord_service: CoordIntegrityService,
                identity_service: IdentityService
            ) -> ValidationResult[Square]:
            
           verify_agent_has_registered_team(
                team_candidate: Any, agent_candidate: Any, agent_certifier: AgentIntegrityService,
                team_context_service: TeamContextService,
            ) -> ValidationResult[(Team, Agent)]:
            
           verify_team_and_game_relationship(
                team_candidate: Any, game_candidate: Any, game_service: GameService
            ) -> ValidationResult[(Team, Game)]:
    
    # INSTANCE METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            board_service: BoardIntegrityService = BoardIntegrityService(),
            coord_service: CoordIntegrityService = CoordIntegrityService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Square]:
        """
        # ACTION:
        1.  Check candidate is not validation.
        2.  Check if candidate is a Square.
        3.  Run id and name integrity checks with identity_service
        4.  Run target integrity checks with coord_service.
        5  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass cast candidate to a Square instance, then return inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any): Object to validate.
            *   coord_service (CoordIntegrityService)
            *   identity_service: (IdentityService)
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
            # Make sure its not null first.
            if candidate is None:
                return ValidationResult.failure(
                    NullSquareException(f"{method}: {NullSquareException.DEFAULT_MESSAGE}")
                )
            # Verify candidate is a Square instance
            if not isinstance(candidate, Square):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Square, but got {type(candidate).__name__} instead.")
                )
            square = cast(Square, candidate)
            
            # Verify the Square.id and Square.name
            identity_validation = identity_service.validate_identity(
                id_candidate=square.id,
                name_candidate=square.name
            )
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            # Verify the Square.coord
            coord_validation = coord_service.item_validator.validate(candidate=square.coord)
            if coord_validation.is_failure():
                return ValidationResult.failure(coord_validation.exception)
            # Ensure the Square is registered with a Board.
            board_validation = board_service.item_validator.validate(square.board)
            if board_validation.is_failure():
                return ValidationResult.failure(board_validation.exception)
            # If no errors are detected return the successfully validated Square instance.
            return ValidationResult.success(payload=square)
            
            # Finally, if there is an unhandled exception Wrap a InvalidSquareException around it
            # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSquareException(ex=ex, message=f"{method}: {InvalidSquareException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_piece_square_binding(
            cls,
            square_candidate: Any,
            piece_candidate: Any,
            piece_validator: type[PieceValidator] = PieceValidator
    ) -> ValidationResult[Square, Piece]:
        """
        # Action:
        Verify there is a relationship between an actionable piece and a square before, they
        are used in conjunction in the system.

        # Parameters:
            * square_candidate (Any): The object to verify is a Square instance.
            * piece_candidate (Any): The object to verify is an disabled Piece instance.
            * piece_service (type[PieceValidator])=PieceIntegrityService

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
        2.  piece_service verifies piece_candidate is an disabled piece on the board.
        3.  After casting the candidates into square and piece test square.target == piece.current_position.
        4.  Test square.occupant == piece.
        5   If any check fails, return the exception inside a ValidationResult.
        6.  When all pass tuple(square, piece) to sender in a ValidationResult.

        # PARAMETERS:
            *   candidate_square (Any): Object to validate as a Square.
            *   candidate_piece (Any): object to validate as an disabled Piece
            *   piece_service (ype[PieceIntegrityService])

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
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPieceSquareRelationException(
                    ex=ex, message=f"{method}: {InvalidPieceSquareRelationException.DEFAULT_MESSAGE}"
                )
            )
