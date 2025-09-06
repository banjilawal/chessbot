from typing import cast

from chess.board.board import Board
from chess.board.square import Square
from chess.common.permit import Event
from chess.exception.event import AttackEventInconsistencyException, \
    CorruptRecordEventException
from chess.exception.null.piece import NullPieceException
from chess.exception.side import RemoveCombatantException
from chess.flow.base import Flow
from chess.request.occupy import OccupationRequest
from chess.request.validators.occupy import OccupationRequestValidator
from chess.token.model import Piece, CombatantPiece
from chess.token.encounter import Encounter


class OccupationFlow(Flow):

    @staticmethod
    def enter(request: OccupationRequest, board: Board):

        validation = OccupationRequestValidator.validate(request)
        if not validation.is_success():
            return validation.exception

        piece = cast(Piece, validation.request.client)

        source_square = board.find_square_by_coord(piece.current_position)
        target_square = cast(Square, request.resource)

        enemy = None

        event = validation.event

        if event == Event.RECORD_ENCOUNTER:
            OccupationFlow.record_stream(piece, target_square)
            return

        if event == Event.ATTACK:
            enemy = OccupationFlow._attack_stream(piece, target_square)

        target_square.occupant = piece
        source_square.occupant = None


    @staticmethod
    def record_stream(piece: Piece, blocked_square: Square):
        method = "OccupationFlow._encounter_stream"
        try:
            blocking_occupant = blocked_square.occupant

            if blocking_occupant is None:
                raise NullPieceException(
                    f"{method}: {NullPieceException.DEFAULT_MESSAGE}"
                )

            if piece.is_enemy(blocking_occupant):
                raise CorruptRecordEventException(
                    f"{method}: {CorruptRecordEventException.DEFAULT_MESSAGE}"
                )

            piece.encounters.add_encounter(Encounter(blocking_occupant))
        except (NullPieceException, ) as e:
            raise CorruptRecordEventException(
                f"{method}: {CorruptRecordEventException.DEFAULT_MESSAGE}"
            )

    @staticmethod
    def _attack_stream(piece: Piece, target_square: Square) -> CombatantPiece:
        method = "OccupationFlow._attack_stream"

        try:
            hostage_candidate = target_square.occupant
            if hostage_candidate is None:
                raise AttackingNullPieceException(
                    f"{method}: {AttackingNullPieceException.DEFAULT_MESSAGE}"
                )

            if not isinstance(hostage_candidate, CombatantPiece):
                raise AttackingKingException(
                    f"{method}: {AttackingKingException.DEFAULT_MESSAGE}"
                )

            hostage_candidate.captor = piece
            enemy_side = hostage_candidate.side
            removal_result = enemy_side.remove_captured_combatant(hostage_candidate)
            if not removal_result.is_success():
                raise removal_result.exception

            hostage = cast(CombatantPiece, removal_result.payload)
            piece.side.add_hostage(hostage)

            if hostag

            return hostage

        except (
            AttackingNullPieceException,
            AttackingKingException,
            RemoveCombatantException
        ) as e:
            raise AttackEventInconsistencyException(
                f"{method}: {AttackEventInconsistencyException.DEFAULT_MESSAGE}"
            ) from e


