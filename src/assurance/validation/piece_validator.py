from typing import TYPE_CHECKING

from assurance.validation.validatin_report import ValidationReport
from assurance.validation.validation_exception import ValidationException
from chess.piece.mobility_status import MobilityStatus
from chess.rank.king import King
from chess.rank.pawn import Pawn
from chess.rank.promotable.promotable_rank import PromotableRank
from chess.transaction.failure import Failure
from chess.transaction.transaction_result import TransactionResult

if TYPE_CHECKING:
    from chess.piece.piece import ChessPiece

class ChessPieceNotNullValidationFailed(ValidationException):
    default_message = "ChessPiece failed not null validation test"
class ChessPieceMovableValidationFailed(ValidationException):
    default_message = "ChessPiece failed movable validation test"
class ChessPiecePromotableValidationFailed(ValidationException):
    default_message = "ChessPiece failed promotable validation test"
class ChessPieceOnBoardValidationFailed(ValidationException):



class ChessPieceValidator:

    @staticmethod
    def is_not_null_test(chess_piece: ChessPiece) -> ValidationReport[ChessPiece]:
        if chess_piece is None:
            return ValidationReport.send_failed_valtidation_report(
                ChessPieceNotNullValidationFailed("ChessPiece failed not null validation test"))
        return ValidationReport.send_passed_validation_report(payload=chess_piece)


    @staticmethod
    def is_movable_test(chess_piece: ChessPiece) -> ValidationReport[ChessPiece]:
        test_report = ChessPieceValidator.is_not_null_test(chess_piece)

        if test_report.payload is None:
             return ValidationReport.send_failed_valtidation_report(
                 ChessPieceMovableValidationFailed(test_report.validation_exception.message))

        testing_payload = test_report.payload
        if testing_payload.coordinate_stack < 1 and testing_payload.status != MobilityStatus.FREE:
            return ValidationReport.send_failed_valtidation_report(
                ChessPieceMovableValidationFailed("ChessPiece failed movable validation test"))
        return ValidationReport.send_passed_validation_report(payload=chess_piece)


    @staticmethod
    def is_promotable_test(chess_piece: 'ChessPiece') -> ValidationReport[ChessPiece]:
        test_report = ChessPieceValidator.is_not_null_test(chess_piece)

        if test_report.payload is None:
            return ValidationReport.send_failed_valtidation_report(
                ChessPiecePromotableValidationFailed(test_report.validation_exception.message))

        testing_payload = test_report.payload
        if testing_payload.rank_tag.rank not in [King, Pawn]:
            return ValidationReport.send_failed_valtidation_report(
                ChessPiecePromotableValidationFailed("ChessPiece not king or pawn. failed promotable validation test")
            )

        if testing_payload.current_coordinate().row != testing_payload.player.home_quadrant.

            coordinate_stack < 1 and testing_payload.status != MobilityStatus.FREE:
            return ValidationReport.send_failed_valtidation_report(
                ChessPieceMovableValidationFailed("ChessPiece failed movable validation test"))

        return ValidationReport.send_passed_validation_report(payload=chess_piece)

    @staticmethod
    def target_is_capturable_test():

    @staticmethod
    def is_starting_square_placeable(piece: 'ChessPiece') -> TransactionResult:
        method = "ChessPieceValidator.is_not_null"

        if piece is None:
            return TransactionResult.failure("ChessPiece does not exist. It is null (None).")
        return TransactionResult(method, StatusCode.SUCCESS)


    @staticmethod
    def can_be_moved(iece: 'ChessPiece') -> TransactionResult:
        method = "ChessPieceValidator.can_move"

        if piece.test_outcome == MobilityStatus.FREE and piece.current_coordinate() is not None:
            return TransactionResult(method, StatusCode.SUCCESS)
        return TransactionResult.failure(f"{piece.label} is not free to move.")


    @staticmethod
    def can_place_on_board(chess_piece: 'ChessPiece') -> TransactionResult:
        method = "ChessPieceValidator.can_add_to_board"
        if (
            chess_piece is not None and
            chess_piece.status == MobilityStatus.FREE and
            chess_piece.current_coordinate() is None
        ):
            return TransactionResult(method, StatusCode.SUCCESS)
        return TransactionResult(method, Failure(f"{chess_piece.label} Cannot be added to the board"))


    @staticmethod
    def can_be_promoted(chess_piece: 'ChessPiece') -> TransactionResult:
        method = "ChessPieceValidator.is_promotable"

        rank = chess_piece.rank
        if isinstance(rank, PromotableRank) and not rank.is_promoted():
            return TransactionResult(method, StatusCode.SUCCESS)
        return TransactionResult(method, Failure(f"{chess_piece.label} of rank {rank.name} cannot be promoted."))


    @staticmethod
    def is_on_board(piece: 'ChessPiece') -> TransactionResult:
        method = "ChessPieceValidator.is_on_board"

        if piece.current_coordinate() is None:
            return TransactionResult(method, Failure(f"{piece.label} is not on the board."))
        return TransactionResult(method, StatusCode.SUCCESS)