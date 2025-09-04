from enum import Enum

from assurance.result.base import Result
from assurance.throw_helper import ThrowHelper
from assurance.validators.coord import CoordValidator
from chess.geometry.coord import Coord




class CoordBuilder(Enum):

    @staticmethod
    def build(row: int, column: int) -> Result[Coord]:
        try:
            candidate = Coord(row, column)
            result = CoordValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(CoordBuilder, result)
            return result
        except Exception as e:
            return Result(payload=None, exception=e)


def main():
    build_result = CoordBuilder.build(3, 4)
    if build_result.is_success():
        coord = build_result.payload
        print(f"Successfully built coordinate: {coord}")
    else:
        print(f"Failed to build coordinate: {build_result.exception}")

    build_result = CoordBuilder.build(-1, 4)
    if build_result.is_success():
        coord= build_result.payload
        print(f"Successfully built coordinate: {coord}")
    else:
        print(f"Failed to build coordinate: {build_result.exception}")

if __name__ == "__main__":
    main()