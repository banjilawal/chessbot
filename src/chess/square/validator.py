# src/chess/square/validator.py

"""
Module: chess.square.validator
Author: Banji Lawal
Created: 2025-09-28
Updated: 2025-10-10

# SECTION 1 - Purpose:
This module provides a satisfaction of the ChessBot integrity requirement.

# SECTION 2 - Scope:
The module covers minimum verification requirements of Square objects

# SECTION 3 - Limitations:
  1. This module cannot only be used on existing Square instances. Use SquareBuilder for construction.
  2. A Square positively verified by the module may fail stricter requirements other components may have.

# SECTION 4 - Design Considerations and Themes:
  1. A Square must undergo sanity checking before use.
  2. As a fundamental, ubiquitous item consolidating all Square sanity checking into one place avoids repetition
      and inconsistent implementations.
  3. Moving all the verification code into one place creates a highly cohesive component.
  4. The component is loosely coupled to other entities even squares and can be used anywhere.
  5. This module cuts down code, increases understanding an simplicity.

# SECTION 5 - Features Supporting Requirements:
1. Testability: Unit testing the module is easy.
2. Maintainable: The component is easy to maintain.

# SECTION G - Feature Delivery Mechanism:
The order of sanity checks produces early failures. to the most granular

# SECTION 7 - Dependencies:
* From chess.system:
    Validator, ValidationResult, NameValidator, LoggingLevelRouter

* From chess.square:
    Square, InvalidSquareException

* From chess.point:
    Coord, CoordValidator

* From Python abc Library:
    ABC, abstractmethod

* From Python typing Library:
    Generic, TypeVar

# SECTION 8 - Contains:
1. SquareValidator
"""

from typing import Any, cast

from chess.coord import CoordValidator
from chess.piece import Piece, PieceValidator
from chess.square import (
    PieceInconsistentSquareOccupationException, Square, InvalidSquareException,
    NullSquareException, SquareAndPieceMismatchedCoordException
)
from chess.system import Validator, ValidationResult, NameValidator, LoggingLevelRouter, IdValidator


class SquareValidator(Validator[Square]):
    """
    # ROLE: Validation
  
    # RESPONSIBILITIES:
    1. Run sanity checks on a candidate to make sure its a valid Square before use.
    2. Pass results of validator process to client.
  
    # PROVIDES:
    ValidationResult[Square] containing either a verified Square or an Exception.
  
    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            id_validator: type[IdValidator]=IdValidator,
            name_validator: type[NameValidator]=NameValidator,
            coord_validator: type[CoordValidator]=CoordValidator,
    ) -> ValidationResult[Square]:
        """
        # Action:
        Ensures the candidate is a Square that meets the minimum requirements for use in the system.
    
        # Parameters:
          * candidate (Any): Object to verify is a Square.
          * id_validator (type[IdValidator]): Verifies the Square.id property
          * name_validator (type[NameValidator]): Verifies the Square.name property
          * coord_validator (type[CoordValidator]): Verifies the Square.coord property
    
        # Returns:
          ValidationResult[Square] containing either:
                - On success: Square in payload.
                - On failure: Exception.
    
        # Raises:
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
            
            id_verification = id_validator.validate(square.id)
            if id_verification.is_failure():
                return ValidationResult.failure(id_verification.exception)
            
            name_verification = name_validator.validate(square.name)
            if name_verification.is_failure:
                return ValidationResult.failure(name_verification.exception)
            
            coord_verification = coord_validator.validate(square.coord)
            if not coord_verification.is_success():
                return ValidationResult.failure(coord_verification.exception)
            
            return ValidationResult.success(payload=square)
        
        except Exception as e:
            return ValidationResult.failure(
                InvalidSquareException(f"{method}: {InvalidSquareException.DEFAULT_MESSAGE}", e)
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
            * piece_validator (PieceValidator): Validates the piece_candidate.

        # Returns:
          ValidationResult[(Square, Piece)] containing either:
                - On success: Tuple(Square, Piece) in payload.
                - On failure: Exception.

        # Raises:
            * SquareAndPieceMismatchedCoordException
            * PieceInconsistentSquareOccupationException
        """
        method = "SquareValidator.verify_piece_relates_to_square"
        
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
                    f"{method}: {InvalidPieceSquareRealtionException.DEFAULT_MESSAGE}", e
                )
            )
