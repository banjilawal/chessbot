from typing import Generic, TypeVar

from assurance.result.base import Result
from chess.exception.piece import AttackingPrisonerException
from chess.exception.state.piece import MovableStateException

from chess.state.checks.base import StateCheck
from chess.state.checks.move import MovableState
from chess.token.model import Piece, Combatant

T = TypeVar('T')

class AttackerState(StateCheck):

    @staticmethod
    def run_check(t: Generic[T]) -> Result[Piece]:
        method = "AttackerState.run_check"

        try:
            state_check = MovableState.run_check(t)
            if not state_check.is_success():
                raise state_check.exception

            piece = state_check.payload

            if isinstance(piece, Combatant) and piece.killer is not None:
                raise AttackingPrisonerException(
                    f"{method}: {AttackingPrisonerException.DEFAULT_MESSAGE}"
                )


            return Result(piece)
        except (
                MovableStateException,
                AttackingPrisonerException
        ) as e:
            raise MovableStateException(f"{method}: {MovableStateException.DEFAULT_MESSAGE}") from e

