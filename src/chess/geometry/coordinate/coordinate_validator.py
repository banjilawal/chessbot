# from typing import Optional
#
# from chess.board.repo.square_repo_validator import SquareRepoValidator
# from assurance.validation.validation_result import ValidationResult
# from assurance.validation.validation_exception import ValidationException
# from chess.geometry.coordinate.coordinate import Coordinate
# from chess.board.repo.repo import ChessBoard
#
#
# class CoordinateNotNullValidationFailed(ValidationException):
#     default_message = "Coordinate failed not null validation test"
#
# class CoordinateDimensionValidationFailed(ValidationException):
#     default_message = "Coordinate failed dimension validation test"
#
# class CoordinateValidator(ValidationException):
#
#     @staticmethod
#     def test_not_none(coordinate: Optional[Coordinate]) -> ValidationResult[Coordinate]:
#         if coordinate is None:
#             return ValidationResult.send_failed_valtidation_report(
#                 CoordinateNotNullValidationFailed("Coordinate failed not null validation test")
#             )
#         return ValidationResult.send_passed_validation_report(payload=coordinate)
#
#
#     @staticmethod
#     def test_coordinate_in_board_dimension(
#         coordinate: Optional[Coordinate],
#         repo: Optional[ChessBoard]
#     ) -> ValidationResult[Coordinate]:
#
#         square_repo_validation_report = SquareRepoValidator.not_null_test(repo)
#         if square_repo_validation_report.payload is None:
#             return ValidationResult.send_failed_valtidation_report(
#                 CoordinateDimensionValidationFailed(square_repo_validation_report.validation_exception)
#             )
#
#         coordinate_validation_report = CoordinateValidator.test_coordinate_not_none(coordinate)
#         if coordinate_validation_report.payload is None:
#             return ValidationResult.send_failed_valtidation_report(
#                 CoordinateDimensionValidationFailed("Coordinate failed not null validation test")
#             )
#
#         payload = coordinate_validation_report.payload
#         if payload.row >= len(repo.squares) or payload.column >= len(repo.squares[0]):
#             return ValidationResult.send_failed_valtidation_report(
#                 CoordinateDimensionValidationFailed("Coordinate failed dimension validation test")
#             )
#
#         return ValidationResult.send_passed_validation_report(payload=coordinate)