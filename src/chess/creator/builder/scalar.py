from enum import Enum

from assurance.result.base import Result
from assurance.throw_helper import ThrowHelper


from chess.geometry.coord import Coord


class ScalarDistanceBuilder(Enum):

    @staticmethod
    def build(p: Coord, q: Coord) -> Result[Distance]:
        candidate = Distance(p, q)
        result = DistanceValidator.validate(candidate)

        try:
            result = DistanceValidator.validate(candidate)
            ThrowHelper.throw_if_invalid(ScalarDistanceBuilder, result)
            return result
        except Exception as e:
            return Result(payload=None, exception=e)

#
# def main():
#     p = Coord(0, 7)
#     q = Coord(2, 6)
#     build_result = DistanceMagnitudeBuilder.build(p, q)
#     if build_result.is_success():
#         distance_magnitude = build_result.payload
#         print(f"Successfully built distance magnitude: {distance_magnitude}")
#     else:
#         print(f"Failed to build distance magnitude: {build_result.exception}")
#
#
# if __name__ == "__main__":
#     main()
