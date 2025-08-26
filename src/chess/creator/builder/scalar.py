from enum import Enum

from assurance.result.base import Result
from assurance.throw_helper import ThrowHelper
from assurance.validation.coord_distance_spec import DistanceMagnitudeSpecification

from chess.geometry.coordinate.coord import Coordinate
from chess.geometry.coordinate.distance import ScalarDistance


class DistanceMagnitudeBuilder(Enum):

    @staticmethod
    def build(p: Coordinate, q: Coordinate) -> Result[ScalarDistance]:
        candidate =ScalarDistance(p, q)
        result = DistanceMagnitudeSpecification.is_satisfied_by(candidate)

        try:
            result = DistanceMagnitudeSpecification.is_satisfied_by(candidate)
            ThrowHelper.throw_if_invalid(DistanceMagnitudeBuilder, result)
            return result
        except Exception as e:
            return Result(payload=None, exception=e)

#
# def main():
#     p = Coordinate(0, 7)
#     q = Coordinate(2, 6)
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
