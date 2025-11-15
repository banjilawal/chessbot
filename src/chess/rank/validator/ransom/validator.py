# src/chess/rank/validator/ransom/validator.py

"""
Module: chess.rank.validator.ransom.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple

from chess.rank.validator.ransom.exception import InvalidRankRansomException, RankRansomException
from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.rank import (
    Rank, King, Queen, Bishop, Rook, Knight, Pawn, RankSpec, RankRansomException, NullRankRansomException,
    RankRansomAboveBoundsException, RankRansomBelowBoundsException, KingRansomException, QueenRansomException,
    RookRansomException, BishopRansomException, KnightRansomException, PawnRansomException,
)


class RankRansomValidator(Validator[Rank, int]):
    """
    # ROLE: Validator, Consistency Management

    # RESPONSIBILITIES:
    1.  Tests
    2.  Provides reference to a Piece.

    # PROVIDES:
    Square

    # ATTRIBUTES:
        *   _id (int): unique identifier
        *   _name (str): letter-number combination. Only unique in the Board
        *   _coord (Coord): row-column array indices in Board array.
        *   _occupant (Optional[Piece]): Piece object that might be occupying the Square.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, rank: Rank) -> ValidationResult[Rank, int]:
        """"""
        method = "RankRansomValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankRansomException(
                        f"{method}: {NullRankRansomException.DEFAULT_MESSAGE}"
                    )
                )
                
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected an integer, got {type(candidate).__id__} instead."
                    )
                )
                
            ransom = cast(candidate, int)
            if ransom < 0:
                return ValidationResult.failure(
                    RankRansomBelowBoundsException(
                        f"{method}: {RankRansomBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
                
            if ransom > RankSpec.QUEEN.ransom:
                return ValidationResult.failure(
                    RankRansomAboveBoundsException(
                        f"{method}: {RankRansomAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )

                
            if isinstance(rank, King) and ransom != RankSpec.KING.ransom:
                return ValidationResult.failure(
                    KingRansomException(f"{method}: {KingRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Queen) and ransom != RankSpec.QUEEN.ransom:
                return ValidationResult.failure(
                    QueenRansomException(f"{method}: {QueenRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Bishop) and ransom != RankSpec.BISHOP.ransom:
                return ValidationResult.failure(
                    BishopRansomException(f"{method}: {BishopRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Rook) and ransom != RankSpec.ROOK.rasnom:
                return ValidationResult.failure(
                    RookRansomException(f"{method}: {RookRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Knight) and ransom != RankSpec.KNIGHT.ransom:
                return ValidationResult.failure(
                    KnightRansomException(f"{method}: {KnightRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Pawn) and ransom != RankSpec.PAWN.ransom:
                return ValidationResult.failure(
                    PawnRansomException(f"{method}: {PawnRansomException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(rank, ransom)
        
        except Exception as ex:
            return ValidationResult.failure(
                RankRansomException(
                    f"{method}: {RankRansomException.DEFAULT_MESSAGE}",
                    ex
                )
            )


# src/chess/vector/validator.py

"""
Module: chess.vector.validator
Author: Banji Lawal
Created: 2025-08-26
version: 1.0.0
"""

from typing import Any, cast

from chess.system import ValidationResult, Validator, LONGEST_KNIGHT_LEG_SIZE, LoggingLevelRouter
from chess.vector import (
    Vector, NullVectorException, NullXComponentException, NullYComponentException, VectorBelowBoundsException,
    VectorAboveBoundsException, InvalidVectorException
)


class VectorValidator(Validator[Vector]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Vector, that meets integrity requirements, before
    the candidate is used.

    # PROVIDES:
    ValidationResult[Vector] containing either:
        - On success: Vector in payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Vector]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check if candidate is a Vector.
        3.  Check candidate.x is:
                *   an INT
                *   between -LONGEST_KNIGHT_LEG_SIZE and -LONGEST_KNIGHT_LEG_SIZE exclusive.
        4.  Check candidate.y is:
                *   an INT
                *   between -LONGEST_KNIGHT_LEG_SIZE and -LONGEST_KNIGHT_LEG_SIZE exclusive.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass cast candidate to a Vector instance then return inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any): Object to validate.

        # Returns:
        ValidationResult[Vector] containing either:
            - On success: Vector in payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullVectorException
            *   InvalidVectorException
        """
        method = "VectorValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullVectorException(f"{method}: {NullVectorException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Vector):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an Vector, got {type(candidate).__name__} instead.")
                )
            
            vector = cast(Vector, candidate)
            
            x_component_validation = cls.validate_x_component(x=vector.x)
            if x_component_validation.is_failure():
                return ValidationResult.failure(x_component_validation.exception)
            
            y_component_validation = cls._y_component_validator(y=vector.y)
            if y_component_validation.is_failure():
                return ValidationResult.failure(y_component_validation.exception)
            
            return ValidationResult.success(payload=vector)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidVectorException(f"{method}: {InvalidVectorException.DEFAULT_MESSAGE}", ex)
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_x_component(cls, x_candidate: Any) -> ValidationResult[int]:
        """
        ACTION:
        Check if the x component is a number within the bounds of the vector.

        PARAMETERS:
            *   x_candidate (Any): The object to validate.

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in payload.
            - On failure: Exception.

        RAISES:
            *   TypeError
            *   NullXComponentException
            *   VectorBelowBoundsException
            *   VectorAboveBoundsException
            *   InvalidVectorException
        """
        method = "VectorValidator.validate_x_component"
        
        try:
            if x_candidate is None:
                return ValidationResult.failure(
                    NullXComponentException(f"{method}: {NullXComponentException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(x_candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an int, got {type(x_candidate).__name__} instead.")
                )
            x = cast(int, x_candidate)
            
            if x < -LONGEST_KNIGHT_LEG_SIZE:
                return ValidationResult.failure(
                    VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if x >= LONGEST_KNIGHT_LEG_SIZE:
                return ValidationResult.failure(
                    VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(payload=x)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidVectorException(f"{method}: {InvalidVectorException.DEFAULT_MESSAGE}", ex)
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_y_component(cls, y_candidate: Any) -> ValidationResult[int]:
        """
        ACTION:
        Check if the y component is a number within the bounds of the vector.

        PARAMETERS:
            *   y_candidate (Any): The object to validate.

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in payload.
            - On failure: Exception.

        RAISES:
            *   TypeError
            *   NullYComponentException
            *   VectorBelowBoundsException
            *   VectorAboveBoundsException
            *   InvalidVectorException
        """
        method = "VectorValidator._validate_y_component"
        
        try:
            if y_candidate is None:
                return ValidationResult.failure(
                    NullYComponentException(f"{method}: {NullYComponentException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(y_candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an int, got {type(x).__name__} instead.")
                )
            y = cast(int, y_candidate)
            
            if y < -LONGEST_KNIGHT_LEG_SIZE:
                return ValidationResult.failure(
                    VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if y >= LONGEST_KNIGHT_LEG_SIZE:
                return ValidationResult.failure(
                    VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(payload=y)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidVectorException(f"{method}: {InvalidVectorException.DEFAULT_MESSAGE}", ex)
            )