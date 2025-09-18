from typing import cast

from chess.common import id_emitter
from chess.exception.hostage.hostage import RosterRemovalException
from chess.operation.occupation import (
    OccupationDirectiveValidator,
    InvalidOccupationDirectiveException,
    EmptyBoardSearchException, OccupationDirective, OccupationException
)
from chess.piece import Piece, Encounter, NullPieceException
from chess.square import Square
from chess.board import Board
from chess.search import BoardSearch
from chess.operation import Executor, Directive, ExecutionContext, OperationResult



class OccupationExecutor(Executor):

    @staticmethod
    def execute_directive(directive: Directive, context: ExecutionContext) -> OperationResult:
        method = "OccupationExecutor.execute-directive"

        op_result_id = id_emitter.op_result_id

        validation = OccupationDirectiveValidator.validate(directive)
        if not validation.is_success():
            return OperationResult(
                op_result_id=op_result_id,
                directive=directive,
                exception=validation.exception
            )

        occupation_directive = cast(OccupationDirective, directive)
        piece = cast(Piece, occupation_directive.actor)

        board = cast(Board, context.board)
        target_square = cast(Square, occupation_directive.target)

        search_result = BoardSearch.square_by_coord(piece.current_position)
        if search_result.exception is not None:
            raise search_result.exception

        if search_result.is_not_found():
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=EmptyBoardSearchException(f"{method}: {EmptyBoardSearchException.DEFAULT_MESSAGE}")
            )
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
            return OccupationExecutor._record_encounter(op_result_id, occupation_directive, piece, target_square)


        if target_occupant is not None and piece.is_enemy(target_occupant):
            OccupationExecutor._attack_enemy(directive, piece, target_square)
        #
        #
        # if event == Event.ATTACK:
        #     enemy = OccupationExecutor._attack_stream(piece, target_square)

        target_square.occupant = piece
        source_square.occupant = None
        piece.positions.push_coord(target_square.coord)

        if piece.current_position == target_square.coord and not source_square.occupant == piece:
            piece.positions.undo_push()
            target_square.occupant = None
            source_square.occupant = piece
            return OperationResult(
                op_result_id=op_result_id,
                directive=directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )

        success_directive = OccupationDirective(
            directive_id=id_emitter.directive_id,
            actor=piece,
            target=target_square
        )
        return OperationResult(op_result_id=op_result_id, directive=success_directive)


    @staticmethod
    def _record_encounter(
        op_result_id :int,
        piece: Piece,
        blocked_square: Square,
        occupation_directive: OccupationDirective
    ) -> OperationResult:

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
                return OperationResult(
                    op_result_id=op_result_id,
                    directive=occupation_directive,
                    exception=NullPieceException(f"{method}: {NullPieceException.DEFAULT_MESSAGE}")
                )

            if piece.is_enemy(blocking_occupant):
                return OperationResult(
                    op_result_id=op_result_id,
                    directive=occupation_directive,
                    exception=CorruptRecordEventException(f"{method}: {CorruptRecordEventException.DEFAULT_MESSAGE}")
                )

            encounter = Encounter(blocking_occupant)
            if encounter not in piece.encounters:
                piece.add_encounter(encounter)

            if encounter not in piece.encounters:
                return OperationResult(
                    op_result_id=op_result_id,
                    directive=occupation_directive,
                    exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
                    was_rolled_back=True
                )

            success_directive = OccupationDirective(
                actor=piece,
                target=occupation_directive.square,
                directive_id=id_emitter.directive_id
            )
            return OperationResult(op_result_id=op_result_id, directive=success_directive)


    @staticmethod
    def _attack_enemy(
        op_result_id: int,
        piece: Piece,
        source_square: Square,
        target_square: Square,
        board: Board,
        occupation_directive: OccupationDirective
    ) -> OperationResult:

        method = "OccupationExecutor._attack_enemy"

        enemy = target_square.occupant
        if enemy is None:
            return OperationResult(op_result_id, occupation_directive,
                AttackingNullPieceException(f"{method}: {AttackingNullPieceException.DEFAULT_MESSAGE}")
            )


        if not piece.is_enemy(enemy):
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}")
            )

        if enemy.positions.is_empty():
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}")
            )

        if enemy not in board.pieces:
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}")
            )

        if not isinstance(enemy, CombatantPiece):
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=AttackingKingException(f"{method}: {AttackingKingException.DEFAULT_MESSAGE}")
            )

        if enemy.captor is not None:
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}")
            )

        enemy_team = enemy.team
        if enemy not in enemy_team.roster:
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}")
            )

        if enemy in piece.team.hostages:
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}")
            )

        enemy.captor = piece
        enemy_team.roster.remove(enemy)

        if enemy in enemy_team.roster:
            enemy.captor = None
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=RosterRemovalException(f"{method}: {RosterRemovalException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )

        piece.team.hostages.append(enemy)
        if enemy not in piece.team.hostages:
            enemy.captor = None
            enemy_team.roster.append(enemy)
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=HostageAdditionException(f"{method}: {HostageAdditionException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )

        board.pieces.remove(enemy)
        if enemy in board.pieces:
            enemy.captor = None
            enemy_team.roster.append(enemy)
            piece.team.hostages.remove(enemy)
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=BoardPieceRemovalException(f"{method}: {BoardPieceRemovalException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )


        target_square.occupant = piece
        if not target_square.occupant == piece:
            enemy.captor = None
            enemy_team.roster.append(enemy)
            piece.team.hostages.remove(enemy)
            board.pieces.append(enemy)
            target_square.occupant = enemy
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=SquareOccupationException(f"{method}: {SquareOccupationException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )

        source_square.occupant = None
        if source_square.occupant == piece:
            enemy.captor = None
            enemy_team.roster.append(enemy)
            piece.team.hostages.remove(enemy)
            board.pieces.append(enemy)
            target_square.occupant = enemy
            source_square.enemy = piece
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=SquareVacationException(f"{method}: {SquareVacationException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )

        piece.positions.push_coord(target_square.coord)
        if not target_square.coord == piece.current_position:
            enemy.captor = None
            enemy_team.roster.append(enemy)
            piece.team.hostages.remove(enemy)
            board.pieces.append(enemy)
            target_square.occupant = enemy
            source_square.enemy = piece
            piece.positions.undo_push()
            return OperationResult(
                op_result_id=op_result_id,
                directive=occupation_directive,
                exception=PositionUpdateException(f"{method}: {PositionUpdateException.DEFAULT_MESSAGE}}"),
                was_rolled_back=True
            )

        success_directive = OccupationDirective(
            directive_id=id_emitter.directive_id,
            actor=piece,
            target=target_square
        )

        return OperationResult(
            op_result_id=id_emitter.op_result_id,
            directive=success_directive,
        )