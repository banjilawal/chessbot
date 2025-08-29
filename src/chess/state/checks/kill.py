from typing import Generic, TypeVar

from assurance.result.base import Result
from chess.exception.piece.dead import DeadPieceAttackingException
from chess.exception.piece.king import KingKillingException
from chess.exception.state.piece import MovableStateException

from chess.state.checks.base import StateCheck
from chess.state.checks.move import MovableState
from chess.token.model import Piece, Combatant, King

T = TypeVar('T')

class KillableState(StateCheck):

    @staticmethod
    def run_check(t: Generic[T]) -> Result[Piece]:
        method = "KillableState.run_check"

        try:
            state_check = MovableState.run_check(t)
            if not state_check.is_success():
                raise state_check.exception

            piece = state_check.payload

            if isinstance(piece, King):
                raise KingKillingException(f"{method}: {KingKillingException.DEFAULT_MESSAGE}")


            return Result(piece)
        except (
            KingKillingException,
            MovableStateException
        ) as e:
            raise MovableStateException(f"{method}: {MovableStateException.DEFAULT_MESSAGE}") from e

