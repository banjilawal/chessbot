from enum import Enum

from assurance.result.base_result import Result
from assurance.throw_helper import ThrowHelper
from assurance.validation.distance_magnitude_specification import DistanceMagnitudeSpecification

from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.coordinate.distance_magnitude import DistanceMagnitude


class DistanceMagnitudeBuilder(Enum):

    @staticmethod
    def build(p: Coordinate, q: Coordinate) -> Result[DistanceMagnitude]:
        candidate =DistanceMagnitude(p, q)
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
