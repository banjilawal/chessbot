from enum import Enum
from typing import cast

from chess.common import BuildResult, KNIGHT_STEP_SIZE
from assurance.throw_helper import ThrowHelper
from chess.vector import (
    Vector, VectorValidator, VectorBelowBoundsException, VectorAboveBoundsException,
    NullXComponentException, NullYComponentException, VectorBuilderException
)



class VectorBuilder(Enum):

    @staticmethod
    def build(x: int, y: int) -> BuildResult[Vector]:

        method = "VectorBuilder.build"

        try:
            if x is None:
                ThrowHelper.throw_if_invalid(
                    VectorBuilder,
                    NullXComponentException(NullXComponentException.DEFAULT_MESSAGE)
                )
            if x < -KNIGHT_STEP_SIZE:
                ThrowHelper.throw_if_invalid(
                    VectorBuilder,
                    VectorBelowBoundsException(VectorBelowBoundsException.DEFAULT_MESSAGE)
                )
            if x > KNIGHT_STEP_SIZE:
                ThrowHelper.throw_if_invalid(
                    VectorBuilder,
                    VectorBelowBoundsException(VectorAboveBoundsException.DEFAULT_MESSAGE)
                )


            if y is None:
                ThrowHelper.throw_if_invalid(
                    VectorBuilder,
                    NullYComponentException(NullYComponentException.DEFAULT_MESSAGE)
                )
            if y < -KNIGHT_STEP_SIZE:
                ThrowHelper.throw_if_invalid(
                    VectorBuilder,
                    VectorBelowBoundsException(VectorBelowBoundsException.DEFAULT_MESSAGE)
                )
            if y > KNIGHT_STEP_SIZE:
                ThrowHelper.throw_if_invalid(
                    VectorBuilder,
                    VectorBelowBoundsException(VectorAboveBoundsException.DEFAULT_MESSAGE)
                )

            validation = VectorValidator.validate(Vector(x=x, y=y))
            if not validation.is_success():
                ThrowHelper.throw_if_invalid(VectorBuilder, validation.exception)

            vector = cast(Vector, validation.payload)
            return BuildResult(payload=vector)

        except Exception as e:
            raise VectorBuilderException(f"{method}: {VectorBuilderException.DEFAULT_MESSAGE}")


# def main():
#     build_result = CoordBuilder.build(3, 4)
#     if build_result.is_success():
#         coord = build_result.payload
#         print(f"Successfully built coord: {coord}")
#     else:
#         print(f"Failed to build coord: {build_result.team_exception}")
#
#     build_result = CoordBuilder.build(-1,  4)
#     if build_result.is_success():
#         coord = build_result.payload
#         print(f"Successfully built coord: {coord}")
#     else:
#         print(f"Failed to build coord: {build_result.team_exception}")
#
# if __name__ == "__main__":
#     main()