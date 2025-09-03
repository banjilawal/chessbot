from enum import Enum

from assurance.result.base import Result
from assurance.throw_helper import ThrowHelper
from assurance.validators.owner import CompertitorValidator
from chess.geometry.coord import Coordinate
from chess.competitor.model import Competitor


class OwnerBuilder(Enum):

    @staticmethod
    def build(owner_id:int, name: str, coordinate: Coordinate ) -> Result[Competitor]:
        try:
            candidate = Competitor(owner_id=owner_id, name=name)
            validation = CompertitorValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(OwnerBuilder, validation)
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