from enum import Enum
from typing import cast

from chess.result import Result
from assurance.throw_helper import ThrowHelper
from chess.square.square_validator import SquareValidator
from chess.square import Square
from chess.common.emit import id_emitter
from chess.coord import Coord


class SquareBuilder(Enum):

    @staticmethod
    def build(square_id:int, name: str, coordinate: Coord) -> Result[Square]:
        try:
            candidate = Square(square_id=square_id, name=name, coord=coordinate)
            validation = SquareValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(SquareBuilder, validation)
            return validation
        except Exception as e:
            return Result(payload=None, exception=e)


def main():
    build_result = SquareBuilder.build(square_id=id_emitter.square_id, name="A3", coordinate=Coord(0, 0))
    if build_result.is_success():
        square = cast(Square, build_result.payload)
        print(f"Successfully built square: {square}")
    else:
        print(f"Failed to build square: {build_result.exception}")

    build_result = SquareBuilder.build(square_id=-1, name="", coordinate=Coord(0, 0))
    if build_result.is_success():
        square = cast(Square, build_result.payload)
        print(f"Successfully built square: {square}")
    else:
        print(f"Failed to build square: {build_result.exception}")

if __name__ == "__main__":
    main()