from typing import cast

from chess.action import Directive, Executor, ExecutionContext, OccupationExecutionException, OperationResult
from chess.board.board import Board
from chess.search import BoardSearch
from chess.square import Square
from chess.common.permit import Event
from chess.action.occupation_exception import AttackEventInconsistencyException, \
    CorruptRecordEventException
from chess.piece.exception.null.null_piece import NullPieceException
from chess.exception.team_exception import RemoveCombatantException
from chess.action.orchestrator import TransactionOrchestrator
from chess.action.send import OccupationRequest
from chess.action.validators.occupy import OccupationDirectiveValidator
from chess.piece.piece import Piece, CombatantPiece
from chess.piece.encounter import Encounter

class OOccupationDirective(Directive):

    def __init__(self, directive_id: int, actor: Piece, target: Square):
        super().__init__(directive_id=directive_id, actor=actor, target=target)

    @property
    def id(self):
        return self._id

    @property
    def piece(self):
        return cast(Piece, self.target)

    @property
    def square(self):
        return cast(self._target, Square)

    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if isinstance(other, OOccupationDirective):
            return self._id == other.id


class OccupationExecutor(Executor):

    @staticmethod
    def execute_directive(directive: Directive, context: ExecutionContext) -> OperationResult:
        method = "OccupationExecutor.execute-directive"

        occupy_directive = cast('OccupyDirective', directive)
        piece = cast(Piece, occupy_directive.actor)

        board = cast(Board, context.board)
        target_square = cast(Square, occupy_directive.target)

        search_result = BoardSearch.square_by_coord(piece.current_position)
        if search_result.exception is not None:
            raise search_result.exception

        if search_result.is_not_found():
            raise OccupationExecutionException(f"{method}: {OccupationExecutionException.DEFAULT_MESSAGE}")
        source_square = cast(Square, search_result.payload)


        # validation = OccupationDirectiveValidator.validate(request)
        # if not validation.is_success():
        #     return validation.exception
        #
        # piece = cast(Piece, validation.request.actor)
        #
        # source_square = board.find_square_by_coord(piece.current_position)
        # target_square = cast(Square, request.target)


        target_occupant = target_square.occupant


        if target_occupant is not None and not piece.is_enemy(target_occupant):
            OccupationExecutor._record_encounter(piece, target_square)
            return

        if target_occupant is not None and piece.is_enemy(target_occupant):
            OccupationExecutor._attack_enemy(piece, target_square)
        #
        #
        # if event == Event.ATTACK:
        #     enemy = OccupationExecutor._attack_stream(piece, target_square)

        target_square.occupant = piece
        source_square.occupant = None
        return OperationResult(id_emitter.)


    @staticmethod
    def _record_encounter(piece: Piece, blocked_square: Square):
        method = "OccupationExecutor._record_encounter"

        """
        A destination occupied by a friendly is handled differently during an occupation operation than a
        scan operation. The difference is the conditions which raise exceptions. The friendly occupant is
        not provided directly to avoid mixing two args of the same type.

        Args
            `piece` (Piece): Records the encounter with a friendly at  `blocked_square`
            `blocked_square` (Square): The blocking friendly is extracted from here

         Returns:
             Result[T]: A Result object containing the validated payload if the Validator is 
                satisfied, NameValidationException otherwise.

        Raises:
            TypeError: if t is not int
            NullNameException: if t is null
            BlankNameException: if t only contains white space.
            ShortNameException: if t is shorter than MIN_NAME_LENGTH

            NameValidationException: Wraps any preceding team_exception 
        """

        """During an occupation operation the a square occupied by a friendly is handled differently 
        than a `ScanOperation.
        
        
        """





        try:
            blocking_occupant = blocked_square.occupant

            if blocking_occupant is None:
                raise NullPieceException(f"{method}: {NullPieceException.DEFAULT_MESSAGE}")

            if piece.is_enemy(blocking_occupant):
                raise CorruptRecordEventException(f"{method}: {CorruptRecordEventException.DEFAULT_MESSAGE}")

            piece.encounters.add_encounter(Encounter(blocking_occupant))
        except (NullPieceException, ) as e:
            raise CorruptRecordEventException(
                f"{method}: {CorruptRecordEventException.DEFAULT_MESSAGE}"
            )


    @staticmethod
    def _attack_enemy(piece: Piece, target_square: Square) -> CombatantPiece:
        method = "OccupationExecutor._attack_stream"

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
            loosing_side = hostage_candidate.team

            removal_result = loosing_side.remove_captured_combatant(hostage_candidate)
            if not removal_result.is_success():
                raise removal_result.exception

            hostage = cast(CombatantPiece, removal_result.payload)

            winning_side = piece.team
            addition_result = winning_side.add_hostage(hostage)
            if not addition_result.is_success():
                raise addition_result.exception

            board.remove_captured_piece(hostage)


        except (
            AttackingNullPieceException,
            AttackingKingException,
            RemoveCombatantException
        ) as e:
            raise AttackEventInconsistencyException(
                f"{method}: {AttackEventInconsistencyException.DEFAULT_MESSAGE}"
            ) from e


