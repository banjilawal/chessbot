# from abc import ABC
#
# from assurance.team_exception.validator.discovery import PieceValidationException
# from assurance.team_exception.validator.square import SquareValidationException
# from assurance.validators.discovery import PieceValidator
# from assurance.validators.square import SquareValidator
# from chess.board.square import Square
# from chess.types.base import TransactionOrchestrator
# from chess.discovery.model import Piece
#
#
# class CaptureFlow(TransactionOrchestrator, ABC):
#
#     @staticmethod
#     def
#
#     @staticmethod
#     def enter_flow(discovery: Piece, square: Square):
#         method = "CaptureFlow.enter_flow"
#
#         piece_result = PieceValidator.validate(discovery)
#         if not piece_result.is_success():
#             raise PieceValidationException(
#                 f"{method}: {PieceValidationException.DEFAULT_MESSAGE}"
#             )
#         attacker = piece_result.payload
#
#         square_result = SquareValidator.validate(square)
#         if not square_result.is_success():
#             raise SquareValidationException(
#                 f"{method}: {SquareValidationException.DEFAULT_MESSAGE}"
#             )
#         target = square_result.payload
#
#         if captor.
