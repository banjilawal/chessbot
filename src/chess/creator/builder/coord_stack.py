from enum import Enum

from chess.common.result import Result
from assurance.throw_helper import ThrowHelper
from assurance.validators.coord_stack import CoordStackValidator
from chess.piece.piece.coord import CoordinateStack


class CoordinateStackBuilder(Enum):

    @staticmethod
    def build() -> Result[CoordinateStack]:
        try:
            candidate = CoordinateStack()
            result = CoordStackValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(CoordinateStackBuilder, result)
            return result
        except Exception as e:
            return Result(payload=None, exception=e)


def main():
    build_result = CoordinateStackBuilder.build()
    if build_result.is_success():
        coordinate_stack = build_result.payload
        print(f"Successfully built coordinate stack: {coordinate_stack}")
    else:
        print(f"Failed to build coordinate stack: {build_result.exception}")

if __name__ == "__main__":
    main()