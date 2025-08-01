from typing import Optional, TYPE_CHECKING

from assurance.validation.square_repo_validator import SquareRepoValidator
from assurance.validation.validatin_report import ValidationReport
from assurance.validation.validation_exception import ValidationException
from chess.geometry.board.coordinate import Coordinate
from chess.square.repo.square_repo import SquareRepo


class CoordinateNotNullValidationFailed(ValidationException):
    default_message = "Coordinate failed not null validation test"

class CoordinateDimensionValidationFailed(ValidationException):
    default_message = "Coordinate failed dimension validation test"

class CoordinateValidator(ValidationException):

    @staticmethod
    def test_coordinate_not_none(coordinate: Optional[Coordinate]) -> ValidationReport[Coordinate]:
        if coordinate is None:
            return ValidationReport.send_failed_valtidation_report(
                CoordinateNotNullValidationFailed("Coordinate failed not null validation test")
            )
        return ValidationReport.send_passed_validation_report(payload=coordinate)


    @staticmethod
    def test_coordinate_in_board_dimension(
        coordinate: Optional[Coordinate],
        square_repo: Optional[SquareRepo]
    ) -> ValidationReport[Coordinate]:

        square_repo_validation_report = SquareRepoValidator.test_square_repo_exists(square_repo)
        if square_repo_validation_report.payload is None:
            return ValidationReport.send_failed_valtidation_report(
                CoordinateDimensionValidationFailed(square_repo_validation_report.validation_exception)
            )

        coordinate_validation_report = CoordinateValidator.test_coordinate_not_none(coordinate)
        if coordinate_validation_report.payload is None:
            return ValidationReport.send_failed_valtidation_report(
                CoordinateDimensionValidationFailed("Coordinate failed not null validation test")
            )

        payload = coordinate_validation_report.payload
        if payload.row >= len(square_repo.squares) or payload.column >= len(square_repo.squares[0]):
            return ValidationReport.send_failed_valtidation_report(
                CoordinateDimensionValidationFailed("Coordinate failed dimension validation test")
            )

        return ValidationReport.send_passed_validation_report(payload=coordinate)