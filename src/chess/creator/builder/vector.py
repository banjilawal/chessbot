from enum import Enum

from assurance.result.base import Result
from assurance.throw_helper import ThrowHelper
from assurance.validators.vector import VectorValidator
from chess.geometry.delta import Vector


class VectorBuilder(Enum):

    @staticmethod
    def build(x: int, y: int) -> Result[Vector]:
        try:
            candidate = Vector(x=x, y=y)
            validation = VectorValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(VectorBuilder, validation)
            return validation
        except Exception as e:
            return Result(payload=None, exception=e)


# def main():
#     build_result = CoordBuilder.build(3, 4)
#     if build_result.is_success():
#         coord = build_result.payload
#         print(f"Successfully built coord: {coord}")
#     else:
#         print(f"Failed to build coord: {build_result.exception}")
#
#     build_result = CoordBuilder.build(-1,  4)
#     if build_result.is_success():
#         coord = build_result.payload
#         print(f"Successfully built coord: {coord}")
#     else:
#         print(f"Failed to build coord: {build_result.exception}")
#
# if __name__ == "__main__":
#     main()