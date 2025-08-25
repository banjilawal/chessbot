from enum import Enum

from pygame.draw import lines

from assurance.error_handler import ErrorHandler
from assurance.result.base_result import Result
from assurance.throw_helper import ThrowHelper
from assurance.validation.coordinate_specification import CoordinateSpecification
from chess import log
from chess.geometry.coordinate.coordinate import Coordinate




class CoordinateBuilder(Enum):

    @staticmethod
    def build(row: int, column: int) -> Result[Coordinate]:
        candidate = Coordinate(row, column)
        result = CoordinateSpecification.is_satisfied_by(candidate)

        try:
            result = CoordinateSpecification.is_satisfied_by(candidate)
            ThrowHelper.throw_if_invalid(CoordinateBuilder, result)
            return result
        except Exception as e:
            return Result(payload=None, exception=e)


def main():
    build_result = CoordinateBuilder.build(3, 4)
    if build_result.is_success():
        coordinate = build_result.payload
        print(f"Successfully built coordinate: {coordinate}")
    else:
        print(f"Failed to build coordinate: {build_result.exception}")

    build_result = CoordinateBuilder.build(-1,  4)
    if build_result.is_success():
        coordinate = build_result.payload
        print(f"Successfully built coordinate: {coordinate}")
    else:
        print(f"Failed to build coordinate: {build_result.exception}")

if __name__ == "__main__":
    main()