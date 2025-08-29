from typing import Generic, TypeVar

from assurance.result.base import Result
from assurance.validators.piece import PieceValidator
from chess.exception.piece import PrisonerEscapeException
from chess.exception.state.piece import MovableStateException

from chess.state.checks.base import StateCheck
from chess.token.model import Piece, Combatant

T = TypeVar('T')


class MovableState(StateCheck):

    @staticmethod
    def run_check(t: Generic[T]) -> Result[Piece]:
        method = "MovableState.run_check"

        try:
            validation_result = PieceValidator.validate(t)
            if not validation_result.is_success():
                raise validation_result.exception

            piece = validation_result.payload

            if piece.coordinate is None:
                raise PieceCoordinateException(f"{method}: {PieceCoordinateException.DEFAULT_MESSAGE}")

            if isinstance(piece, Combatant) and piece.killer is not None:
                raise PrisonerEscapeException(f"{method}: {PrisonerEscapeException.DEFAULT_MESSAGE}")

            return Result(piece)

        except (
                PieceCoordinateException,
                PieceCoordinateException,
                PrisonerEscapeException
        ) as e:
            raise MovableStateException(f"{method}: {MovableStateException.DEFAULT_MESSAGE}") from e
