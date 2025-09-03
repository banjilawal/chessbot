from enum import Enum

from assurance.result.base import Result
from assurance.throw_helper import ThrowHelper
from assurance.validators.square import SquareValidator
from chess.board.square import Square
from chess.geometry.coord import Coordinate


class SquareBuilder(Enum):

    @staticmethod
    def build(square_id:int, name: str, coordinate: Coordinate ) -> Result[Square]:
        try:
            candidate = Square(square_id=square_id, name=name, coordinate=coordinate)
            validation = SquareValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(SquareBuilder, validation)
            return validation
        except Exception as e:
            return Result(payload=None, exception=e)


# def main():
#     build_result = CoordinateBuilder.build(3, 4)
#     if build_result.is_success():
#         coordinate = build_result.payload
#         print(f"Successfully built coordinate: {coordinate}")
#     else:
#         print(f"Failed to build coordinate: {build_result.exception}")
#
#     build_result = CoordinateBuilder.build(-1,  4)
#     if build_result.is_success():
#         coordinate = build_result.payload
#         print(f"Successfully built coordinate: {coordinate}")
#     else:
#         print(f"Failed to build coordinate: {build_result.exception}")
#
# if __name__ == "__main__":
#     main()