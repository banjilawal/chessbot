# from typing import Optional
#
# from assurance.validation.validation_result import ValidationResult
# from assurance.validation.validation_exception import ValidationException
# from chess.map.repo.repo import Map
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
#     def not_null_test(repo: Optional[Map]) -> ValidationResult[Map]:
#         if repo is None:
#             return ValidationResult.send_failed_valtidation_report(
#                 RepoNotNullValidationFailed("Map failed not null validation test")
#             )[Map]
#         return ValidationResult.send_passed_validation_report(payload=repo)[Map]
#
#     @staticmethod
#     def not_empty_test(repo: Optional[Map]) -> ValidationResult[Map]:
#         test_report = SquareRepoValidator.not_null_test(repo)
#
#         if test_report.payload is None:
#             return ValidationResult.send_failed_valtidation_report(
#                 RepoNotEmptyValidationFailed(test_report.validation_exception.message)
#             )
#
#         if test_report.payload.squares is None or len(test_report.payload.squares) == 0 or len(test_report.payload.squares[0]) == 0:
#             return ValidationResult.send_failed_valtidation_report(
#                 RepoNotEmptyValidationFailed("Map failed not empty validation test")
#             )
#
#         return ValidationResult.send_passed_validation_report(payload=repo)