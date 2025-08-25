from pygame.draw import lines

from assurance.result.base_result import Result
from assurance.validation.coordinate_specification import CoordinateSpecification
from chess import log
from chess.geometry.coordinate.coordinate import Coordinate




class CoordinateBuilder:
    @staticmethod
    def build(row: int, column: int) -> Result[Coordinate]:
        candidate = Coordinate(row, column)
        result = CoordinateSpecification.is_satisfied_by(candidate)

        if result.is_failure():
            log.error(f"Invalid coordinate: {result.exception}")
            return Result(payload=None, exception=result.exception)

        return Result(payload=candidate, exception=None)

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


class CoordinateBuilder:
    @staticmethod
    def build(row: int, column: int) -> TransactionResult[Coordinate]:
        candidate = Coordinate(row, column)
        result = CoordinateSpecification.is_satisfied_by(candidate)

        if result.is_failure():
            log.error(f"Invalid coordinate: {result.exception}")
            return Result(payload=None, exception=result.exception)

        return Result(payload=candidate, exception=None)