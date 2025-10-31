# src/chess/rank/validator.py

"""
Module: chess.rank.validator
Author: Banji Lawal
Created: 2025-09-26
version: 1.0.0
"""


from typing import Any, TypeVar, cast

from chess.system import LoggingLevelRouter, ValidationResult, ValidationResult
from chess.system.validate.validator import Validator
from chess.rank import (
    Rank, King, Pawn, Knight, Bishop, Rook, Queen, RankSpec,
    InvalidPawnException,
    InvalidKnightException, InvalidBishopException,
    InvalidRookException, InvalidQueenException,
    NullRankException, InvalidRankException,
    UnRecognizedConcreteRankException, InvalidKingException
)


class RankValidator(Validator[Rank]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Rank]:
        """"""
        method = "Rank.validate"
        try:
            if candidate is None:
                return ValidationResult.failure(NullRankException(f"{method} {NullRankException.DEFAULT_MESSAGE}"))
            
            if not isinstance(candidate, (King, Pawn, Knight, Bishop, Rook, Queen)):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected a Rank subclass, got {type(candidate).__name__}")
                )
            
            if isinstance(candidate, King):
                return RankValidator._validate_king_spec(cast(King, candidate))
            elif isinstance(candidate, Pawn):
                return RankValidator._validate_pawn_spec(cast(Pawn, candidate))
            elif isinstance(candidate, Knight):
                return RankValidator._validate_knight_spec(cast(Knight, candidate))
            elif isinstance(candidate, Bishop):
                return RankValidator._validate_bishop_spec(cast(Bishop, candidate))
            elif isinstance(candidate, Rook):
                return RankValidator._validate_rook_spec(cast(Rook, candidate))
            elif isinstance(candidate, Queen):
                return RankValidator._validate_queen_spec(cast(Queen, candidate))
            else:
                raise UnRecognizedConcreteRankException(
                    f"{method}: {UnRecognizedConcreteRankException.DEFAULT_MESSAGE}"
                )
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    def _validate_king_spec(cls, candidate: King) -> ValidationResult[King]:
        if not (
                candidate.quota == RankSpec.KING.quota and
                candidate.ransom == RankSpec.KING.ransom and
                candidate.quadrants == RankSpec.KING.quadrants and
                candidate.name.upper() == RankSpec.KING.name.upper() and
                candidate.letter.upper() == RankSpec.KING.letter.upper()
        ):
            return ValidationResult.failure(
                InvalidKingException(f"RankValidator.validate: {InvalidKingException.DEFAULT_MESSAGE}")
            )
        return ValidationResult(payload=cast(King, candidate))
    
    @classmethod
    def _validate_pawn_spec(cls, candidate: Pawn) -> ValidationResult[Pawn]:
        if not (
                candidate.quota == RankSpec.PAWN.quota and
                candidate.ransom == RankSpec.PAWN.ransom and
                candidate.quadrants == RankSpec.PAWN.quadrants and
                candidate.name.upper() == RankSpec.PAWN.name.upper() and
                candidate.letter.upper() == RankSpec.PAWN.letter.upper()
        ):
            return ValidationResult.failure(
                InvalidPawnException(f"RankValidator.validate: {InvalidPawnException.DEFAULT_MESSAGE}")
            )
        return ValidationResult(payload=cast(Pawn, candidate))
    
    @classmethod
    def _validate_bishop_spec(cls, candidate: Bishop) -> ValidationResult[Bishop]:
        if not (
                candidate.quota == RankSpec.BISHOP.quota and
                candidate.ransom == RankSpec.BISHOP.ransom and
                candidate.quadrants == RankSpec.BISHOP.quadrants and
                candidate.name.upper() == RankSpec.BISHOP.name.upper() and
                candidate.letter.upper() == RankSpec.BISHOP.letter.upper()
        ):
            return ValidationResult.failure(
                InvalidBishopException(f"RankValidator.validate: {InvalidBishopException.DEFAULT_MESSAGE}")
            )
        return ValidationResult(payload=cast(Bishop, candidate))
    
    @classmethod
    def _validate_knight_spec(cls, candidate: Knight) -> ValidationResult[Knight]:
        if not (
                candidate.quota == RankSpec.KNIGHT.quota and
                candidate.ransom == RankSpec.KNIGHT.ransom and
                candidate.quadrants == RankSpec.KNIGHT.quadrants and
                candidate.name.upper() == RankSpec.KNIGHT.name.upper() and
                candidate.letter.upper() == RankSpec.KNIGHT.letter.upper()
        ):
            return ValidationResult(
                InvalidKnightException(f"RankValidator.validate: {InvalidKnightException.DEFAULT_MESSAGE}")
            )
        return ValidationResult(payload=cast(Knight, candidate))
    
    @classmethod
    def _validate_rook_spec(cls, candidate: Rook) -> ValidationResult[Rook]:
        if not (
                candidate.quota == RankSpec.ROOK.quota and
                candidate.ransom == RankSpec.ROOK.ransom and
                candidate.quadrants == RankSpec.ROOK.quadrants and
                candidate.name.upper() == RankSpec.ROOK.name.upper() and
                candidate.letter.upper() == RankSpec.ROOK.letter.upper()
        ):
            return ValidationResult(
                InvalidRookException(f"RankValidator.validate: {InvalidRookException.DEFAULT_MESSAGE}")
            )
        return ValidationResult(payload=cast(Rook, candidate))
    
    @classmethod
    def _validate_queen_spec(cls, candidate: Queen) -> ValidationResult[Queen]:
        if not (
                candidate.quota == RankSpec.QUEEN.quota and
                candidate.ransom == RankSpec.QUEEN.ransom and
                candidate.quadrants == RankSpec.QUEEN.quadrants and
                candidate.name.upper() == RankSpec.QUEEN.name.upper() and
                candidate.letter.upper() == RankSpec.QUEEN.letter.upper()
        ):
            return ValidationResult(
                InvalidQueenException(f"RankValidator.validate: {InvalidQueenException.DEFAULT_MESSAGE}")
            )
        return ValidationResult(payload=cast(Queen, candidate))
