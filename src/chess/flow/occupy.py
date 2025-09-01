from typing import cast

from chess.board.board import ChessBoard
from chess.board.square import Square
from chess.common.permit import Event
from chess.exception.event import AttackPermissionInconsistencyException, \
    InconsistentMarkObstructionException
from chess.flow.base import Flow
from chess.request.occupy import OccupationRequest
from chess.request.validators.occupy import OccupationRequestValidator
from chess.token.model.base import Piece
from chess.token.model.combatant import CombatantPiece


class OccupationFlow(Flow):

    @staticmethod
    def enter(request: OccupationRequest, board: ChessBoard):

        validation = OccupationRequestValidator.validate(request)
        if not validation.is_success():
            return validation.exception

        piece = cast(Piece, validation.request.client)

        source_square = board.find_square_by_coordinate(piece.current_position)
        target_square = cast(Square, request.resource)

        enemy = None

        permission = validation.event

        if permission == Event.MARK_OBSTRUCTION:
            OccupationFlow._obstruction_stream(piece, target_square)
            return

        if permission == Event.ATTACK:
            enemy = OccupationFlow._attack_stream(piece, target_square)

        target_square.occupant = piece
        source_square.occupant = None


    @staticmethod
    def _obstruction_stream(piece: Piece, blocked_square: Square):
        method = "OccupationFlow._obstruction_stream"
        blocking_occupant = blocked_square.occupant

        if blocking_occupant is None or not piece.is_enemy(blocking_occupant):
            raise InconsistentMarkObstructionException(
                f"{method}: "
                f"{InconsistentMarkObstructionException.DEFAULT_MESSAGE}"
            )
        piece.add_obstruction(blocking_occupant)


    @staticmethod
    def _attack_stream(piece: Piece, target_square: Square) -> CombatantPiece:
        method = "OccupationFlow._attack_stream"
        if target_square.occupant is None:
            raise AttackPermissionInconsistencyException(
                f"{method}: {AttackPermissionInconsistencyException.DEFAULT_MESSAGE}"
            )
        target_square.occupant.captor = piece
        return target_square.occupant


