# from abc import ABC
#
# from assurance.exception.validator.piece import PieceValidationException
# from assurance.exception.validator.square import SquareValidationException
# from assurance.validators.piece import PieceValidator
# from assurance.validators.square import SquareValidator
# from chess.board.square import Square
# from chess.flow.base import Flow
# from chess.piece.model import Piece
#
#
# class CaptureFlow(Flow, ABC):
#
#     @staticmethod
#     def
#
#     @staticmethod
#     def enter_flow(piece: Piece, square: Square):
#         method = "CaptureFlow.enter_flow"
#
#         piece_result = PieceValidator.validate(piece)
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
