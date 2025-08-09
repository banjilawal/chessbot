# from typing import Optional
#
# from assurance.validation.validation_result import ValidationResult
# from assurance.validation.validation_exception import ValidationException
# from chess.board.repo.repo import ChessBoard
#
#
# class RepoNotNullValidationFailed(ValidationException):
#     default_message = "Repo failed not null validation test"
#
# class RepoNotEmptyValidationFailed(ValidationException):
#     default_message = "Repo failed not empty validation test"
#
#
# class SquareRepoValidator:
#
#     @staticmethod
#     def not_null_test(repo: Optional[ChessBoard]) -> ValidationResult[ChessBoard]:
#         if repo is None:
#             return ValidationResult.send_failed_valtidation_report(
#                 RepoNotNullValidationFailed("ChessBoard failed not null validation test")
#             )[ChessBoard]
#         return ValidationResult.send_passed_validation_report(payload=repo)[ChessBoard]
#
#     @staticmethod
#     def not_empty_test(repo: Optional[ChessBoard]) -> ValidationResult[ChessBoard]:
#         test_report = SquareRepoValidator.not_null_test(repo)
#
#         if test_report.payload is None:
#             return ValidationResult.send_failed_valtidation_report(
#                 RepoNotEmptyValidationFailed(test_report.validation_exception.message)
#             )
#
#         if test_report.payload.squares is None or len(test_report.payload.squares) == 0 or len(test_report.payload.squares[0]) == 0:
#             return ValidationResult.send_failed_valtidation_report(
#                 RepoNotEmptyValidationFailed("ChessBoard failed not empty validation test")
#             )
#
#         return ValidationResult.send_passed_validation_report(payload=repo)