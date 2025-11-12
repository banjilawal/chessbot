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
    def validate(cls, candidate: Any) -> ValidationResult[Square]:
        """
        # Action:
        Ensures the candidate is a Square that meets the minimum requirements for use in the system.
    
        # Parameters:
          * candidate (Any): Object to verify is a Square.
    
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
            
            id_validation = IdValidator.validate(square.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            name_validation = NameValidator.validate(square.name)
            if name_validation.is_failure:
                return ValidationResult.failure(name_validation.exception)
            
            coord_validation = CoordValidator.validate(square.coord)
            if not coord_validation.is_success():
                return ValidationResult.failure(coord_validation.exception)
            
            return ValidationResult.success(payload=square)
        
        except Exception as e:
            return ValidationResult.failure(
                InvalidSquareException(f"{method}: {InvalidSquareException.DEFAULT_MESSAGE}", e)
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_piece_relates_to_square(
            cls, 
            square_candidate: Any, 
            piece_candidate: Any,
            piece_validator: PieceValidator = PieceValidator
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
            square_validation = cls.validate(square_candidate)
            if not square_validation.is_failure():
                return ValidationResult.failure(square_validation.exception)
            
            square = cast(Square, square_candidate)
            
            active_piece_validation = piece_validator.verify_active_piece(piece_candidate)
            if not active_piece_validation.is_failure():
                return ValidationResult.failure(active_piece_validation.exception)
            
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
                InvalidSquareException(f"{method}: {InvalidSquareException.DEFAULT_MESSAGE}", e)
            )
