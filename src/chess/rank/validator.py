# from typing import Generic
#
# from assurance.result.base import Result
# # from assurance.validators.base import Validator, T
# # from chess.validation.base import Rank
#
#
from typing import Generic, TypeVar, cast


from chess.common import Result
from chess.common.validator import Validator
from chess.rank import (
    Rank, King, Pawn, Knight, Bishop, Rook, Queen, RankSpec,
    KingValidationException, PawnValidationException,
    KnightValidationException, BishopValidationException,
    RookValidationException, QueenValidationException,
    NullRankException, RankValidationException,
    UnRecognizedConcreteRankException, KingValidationException
)

T = TypeVar('T')

class RankValidator(Validator):

    @staticmethod
    def validate(t: Rank) -> Result[Rank]:
        method = "Rank.validate"
        try:
            if t is None:
                raise NullRankException(
                    f"{method} {NullRankException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, (King, Pawn, Knight, Bishop, Rook, Queen)):
                raise TypeError(f"{method} Expected a Rank subclass, got {type(t).__name__}")

            if isinstance(t, King):
                return RankValidator._validate_king_spec(cast(King, t))
            elif isinstance(t, Pawn):
                return RankValidator._validate_pawn_spec(cast(Pawn, t))
            elif isinstance(t, Knight):
                return RankValidator._validate_knight_spec(cast(Knight, t))
            elif isinstance(t, Bishop):
                return RankValidator._validate_bishop_spec(cast(Bishop, t))
            elif isinstance(t, Rook):
                return RankValidator._validate_rook_spec(cast(Rook, t))
            elif isinstance(t, Queen):
                return RankValidator._validate_queen_spec(cast(Queen, t))
            else:
                raise UnRecognizedConcreteRankException(
                    f"{method}: {UnRecognizedConcreteRankException.DEFAULT_MESSAGE}"
            )

        except (
                TypeError,
                NullRankException,
                UnRecognizedConcreteRankException,
        ) as e:
            raise RankValidationException(f"{method}: {RankValidationException.DEFAULT_MESSAGE}") from e

        # This block catches any unexpected exceptions
        # You might want to log the error here before re-raising
        except Exception as e:
            raise RankValidationException(f"An unexpected error occurred during validation: {e}") from e


    @staticmethod
    def _validate_king_spec(candidate: King) -> Result[King]:
        if not (
            candidate.quota == RankSpec.KING.quota and
            candidate.ransom == RankSpec.KING.ransom and
            candidate.quadrants == RankSpec.KING.quadrants and
            candidate.name.upper() == RankSpec.KING.name.upper() and
            candidate.letter.upper() == RankSpec.KING.letter.upper()
        ):
            return Result(
                exception=KingValidationException(
                    f"RankValidator.validate: {KingValidationException.DEFAULT_MESSAGE}"
                )
            )
        return Result(payload=cast(King, candidate))


    @staticmethod
    def _validate_pawn_spec(candidate: Pawn) -> Result[Pawn]:
        if not (
                candidate.quota == RankSpec.PAWN.quota and
                candidate.ransom == RankSpec.PAWN.ransom and
                candidate.quadrants == RankSpec.PAWN.quadrants and
                candidate.name.upper() == RankSpec.PAWN.name.upper() and
                candidate.letter.upper() == RankSpec.PAWN.letter.upper()
        ):
            return Result(
                exception=PawnValidationException(
                    f"RankValidator.validate: {PawnValidationException.DEFAULT_MESSAGE}"
                )
            )
        return Result(payload=cast(Pawn, candidate))


    @staticmethod
    def _validate_bishop_spec(candidate: Bishop) -> Result[Bishop]:
        if not (
                candidate.quota == RankSpec.BISHOP.quota and
                candidate.ransom == RankSpec.BISHOP.ransom and
                candidate.quadrants == RankSpec.BISHOP.quadrants and
                candidate.name.upper() == RankSpec.BISHOP.name.upper() and
                candidate.letter.upper() == RankSpec.BISHOP.letter.upper()
        ):
            return Result(
                exception=BishopValidationException(
                    f"RankValidator.validate: {BishopValidationException.DEFAULT_MESSAGE}"
                )
            )
        return Result(payload=cast(Bishop, candidate))


    @staticmethod
    def _validate_knight_spec(candidate: Knight) -> Result[Knight]:
        if not (
                candidate.quota == RankSpec.KNIGHT.quota and
                candidate.ransom == RankSpec.KNIGHT.ransom and
                candidate.quadrants == RankSpec.KNIGHT.quadrants and
                candidate.name.upper() == RankSpec.KNIGHT.name.upper() and
                candidate.letter.upper() == RankSpec.KNIGHT.letter.upper()
        ):
            return Result(
                exception=KnightValidationException(
                    f"RankValidator.validate: {KnightValidationException.DEFAULT_MESSAGE}"
                )
            )
        return Result(payload=cast(Knight, candidate))


    @staticmethod
    def _validate_rook_spec(candidate: Rook) -> Result[Rook]:
        if not (
                candidate.quota == RankSpec.ROOK.quota and
                candidate.ransom == RankSpec.ROOK.ransom and
                candidate.quadrants == RankSpec.ROOK.quadrants and
                candidate.name.upper() == RankSpec.ROOK.name.upper() and
                candidate.letter.upper() == RankSpec.ROOK.letter.upper()
        ):
            return Result(
                exception=RookValidationException(
                    f"RankValidator.validate: {RookValidationException.DEFAULT_MESSAGE}"
                )
            )
        return Result(payload=cast(Rook, candidate))


    @staticmethod
    def _validate_queen_spec(candidate: Queen) -> Result[Queen]:
        if not (
                candidate.quota == RankSpec.QUEEN.quota and
                candidate.ransom == RankSpec.QUEEN.ransom and
                candidate.quadrants == RankSpec.QUEEN.quadrants and
                candidate.name.upper() == RankSpec.QUEEN.name.upper() and
                candidate.letter.upper() == RankSpec.QUEEN.letter.upper()
        ):
            return Result(
                exception=QueenValidationException(
                    f"RankValidator.validate: {QueenValidationException.DEFAULT_MESSAGE}"
                )
            )
        return Result(payload=cast(Queen, candidate))