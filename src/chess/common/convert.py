from typing import cast

from chess.geometry.validator.coord_validator import CoordValidator
from chess.geometry.validator.vector_validator import VectorValidator
from chess.creator.builder.coord import CoordBuilder
from chess.geometry.coord import Coord
from chess.geometry.vector import Vector


class Convert:

    @staticmethod
    def vector_to_coordinate(vector: Vector) -> Coord:
        """Converts a null-pkg to a coord."""

        validation_result = VectorValidator.validate(vector)
        if not validation_result.is_success:
            raise validation_result.exception

        v = cast(validation_result.payload, Vector)

        return CoordBuilder.build(row=v.y, column=v.x).payload


    @staticmethod
    def coordinate_to_vector(coordinate: Coord) -> Vector:
        """Converts a coord to a null-pkg."""

        validation_result = CoordValidator.validate(coordinate)
        if not validation_result.is_success:
            raise validation_result.exception

        c = cast(validation_result.payload, Coord)

        return CoordBuilder.build(row=v.y, column=v.x).payload



