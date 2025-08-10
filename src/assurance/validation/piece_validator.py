from typing import TYPE_CHECKING

from assurance.validation.validation_result import ValidationResult
from assurance.validation.validation_exception import ValidationException
from chess.token.mobility_status import MobilityStatus
from chess.rank.promotable.king_rank import KingRank
from chess.rank.promotable.pawn_rank import PawnRank

if TYPE_CHECKING:
    from chess.token.chess_piece import ChessPiece

class ChessPieceNotNullValidationFailed(ValidationException):
    default_message = "ChessPiece failed not null validation test"
class ChessPieceMovableValidationFailed(ValidationException):
    default_message = "ChessPiece failed movable validation test"
class ChessPiecePromotableValidationFailed(ValidationException):
    default_message = "ChessPiece failed promotable validation test"
class ChessPieceOnBoardValidationFailed(ValidationException):
    default_message = "ChessPiece failed on chess_board validation test"


class ChessPieceValidator:

    @staticmethod
    def not_null_test(chess_piece: ChessPiece) -> ValidationResult[ChessPiece]:
        if chess_piece is None:
            return ValidationResult.send_failed_valtidation_report(
                ChessPieceNotNullValidationFailed("ChessPiece failed not null validation test"))
        return ValidationResult.send_passed_validation_report(payload=chess_piece)


    @staticmethod
    def is_movable_test(chess_piece: ChessPiece) -> ValidationResult[ChessPiece]:
        test_report = ChessPieceValidator.not_null_test(chess_piece)

        if test_report.payload is None:
             return ValidationResult.send_failed_valtidation_report(
                 ChessPieceMovableValidationFailed(test_report.validation_exception.message))

        testing_payload = test_report.payload
        if testing_payload.coordinate_stack < 1 and testing_payload.status != MobilityStatus.FREE:
            return ValidationResult.send_failed_valtidation_report(
                ChessPieceMovableValidationFailed("ChessPiece failed movable validation test"))
        return ValidationResult.send_passed_validation_report(payload=chess_piece)


    @staticmethod
    def is_promotable_test(chess_piece: 'ChessPiece') -> ValidationResult[ChessPiece]:
        test_report = ChessPieceValidator.not_null_test(chess_piece)

        if test_report.payload is None:
            return ValidationResult.send_failed_valtidation_report(
                ChessPiecePromotableValidationFailed(test_report.validation_exception.message))

        testing_payload = test_report.payload
        if testing_payload.rank_tag.rank not in [KingRank, PawnRank]:
            return ValidationResult.send_failed_valtidation_report(
                ChessPiecePromotableValidationFailed("ChessPiece not king or chess_piece. failed promotable validation test")
            )

        if testing_payload.current_coordinate().row != testing_payload.player.home_quadrant.enemy_quadrant():
            return ValidationResult.send_failed_valtidation_report(
                ChessPiecePromotableValidationFailed(
                    "Promotable chess chess_piece is not in enemy home. Failed is_promotable_test"
                )
            )

        return ValidationResult.send_passed_validation_report(payload=chess_piece)

    @staticmethod
    def target_is_capturable_test(captor: 'ChessPiece', target: 'ChessPiece') -> ValidationResult[ChessPiece]:
        captor_test_report = ChessPieceValidator.not_null_test(captor)
        target_test_report = ChessPieceValidator.not_null_test(target)

        if captor_test_report.payload is None or target_test_report.payload is None:
            return ValidationResult.send_failed_valtidation_report(
                ChessPiecePromotableValidationFailed(
                    "ChessPiece failed target_is_capturable_test. One of the pieces is None"
                )
            )

        captor_payload = captor_test_report.payload
        target_payload = target_test_report.payload

        if captor_payload.player == target_payload.player:
            return ValidationResult.send_failed_valtidation_report(
                ChessPiecePromotableValidationFailed(
                    "ChessPiece failed target_is_capturable_test. Captor and target are on the same team"
                )
            )
        if captor_payload.status != target_payload.status and captor_payload.status != MobilityStatus.FREE:
            return ValidationResult.send_failed_valtidation_report(
                ChessPiecePromotableValidationFailed(
                    "ChessPiece failed target_is_capturable_test. Captor and target are not in the same mobility status"
                )
            )
        return ValidationResult.send_passed_validation_report(payload=target_payload)

    @staticmethod
    def is_starting_square_placeable(piece: 'ChessPiece') -> ValidationResult[ChessPiece]:
        not_null_report = ChessPieceValidator.not_null_test(piece)
        if not_null_report.payload is None:
            return ValidationResult(payload=None,
                validationException=ChessPieceOnBoardValidationFailed(not_null_report.validation_exception.message)
            )

        test_payload = not_null_report.payload
        not_movable_report = ChessPieceValidator.is_movable_test(test_payload)
        if not_movable_report.payload is None:
            return ValidationResult.send_failed_valtidation_report(
                ChessPieceOnBoardValidationFailed(not_movable_report.validation_exception.message))

        if len(piece.coordinate_stack) != 0 :
            return ValidationResult.send_failed_valtidation_report(
                ChessPieceOnBoardValidationFailed("The chess chess_piece is already on the chess_board"))

        return ValidationResult.send_passed_validation_report(payload=test_payload)