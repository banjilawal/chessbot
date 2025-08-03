# from typing import Optional
#
# from assurance.validation.validation_result import ValidationResult
# from assurance.validation.validation_exception import ValidationException
# from chess.square.repo.square_repo import SquareRepo
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
#     def not_null_test(square_repo: Optional[SquareRepo]) -> ValidationResult[SquareRepo]:
#         if square_repo is None:
#             return ValidationResult.send_failed_valtidation_report(
#                 RepoNotNullValidationFailed("SquareRepo failed not null validation test")
#             )[SquareRepo]
#         return ValidationResult.send_passed_validation_report(payload=square_repo)[SquareRepo]
#
#     @staticmethod
#     def not_empty_test(square_repo: Optional[SquareRepo]) -> ValidationResult[SquareRepo]:
#         test_report = SquareRepoValidator.not_null_test(square_repo)
#
#         if test_report.payload is None:
#             return ValidationResult.send_failed_valtidation_report(
#                 RepoNotEmptyValidationFailed(test_report.validation_exception.message)
#             )
#
#         if test_report.payload.squares is None or len(test_report.payload.squares) == 0 or len(test_report.payload.squares[0]) == 0:
#             return ValidationResult.send_failed_valtidation_report(
#                 RepoNotEmptyValidationFailed("SquareRepo failed not empty validation test")
#             )
#
#         return ValidationResult.send_passed_validation_report(payload=square_repo)