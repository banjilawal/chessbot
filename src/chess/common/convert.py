from typing import cast

from assurance.validators.coord import CoordinateValidator
from assurance.validators.vector import VectorValidator
from chess.creator.builder.coord import CoordinateBuilder
from chess.geometry.coord import Coordinate
from chess.geometry.delta import Vector


class Convert:

    @staticmethod
    def vector_to_coordinate(vector: Vector) -> Coordinate:
        """Converts a vector to a coordinate."""

        validation_result = VectorValidator.validate(vector)
        if not validation_result.is_success:
            raise validation_result.exception

        v = cast(validation_result.payload, Vector)

        return CoordinateBuilder.build(row=v.y, column=v.x).payload


    @staticmethod
    def coordinate_to_vector(coordinate: Coordinate) -> Vector:
        """Converts a coordinate to a vector."""

        validation_result = CoordinateValidator.validate(coordinate)
        if not validation_result.is_success:
            raise validation_result.exception

        c = cast(validation_result.payload, Coordinate)

        return CoordinateBuilder.build(row=v.y, column=v.x).payload



