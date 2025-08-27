from assurance.validation.coord import CoordinateSpecification
from assurance.validation.scalar import ScalarSpecification
from assurance.validation.vector import VectorSpecification
from chess.creator.builder.coord import CoordinateBuilder
from chess.geometry.coordinate.coord import Coordinate
from chess.geometry.vector.delta import Vector
from chess.geometry.vector.scalar import Scalar


class VectorAlgebra:

    """
        Provides static methods for vector algebra operations.
        Used to do safe algebraic operations on Vectors and Coordinates.
        The addition and multiplication methods are used to create safe:

            - SquareIterator
            - Adding quadrant vectors to coordinates to see where a piece can move
    """

    @staticmethod
    def convert_to_coordinate(vector: Vector) -> Coordinate:
        """Converts a vector to a coordinate."""

        vector_validation_result = VectorSpecification.is_satisfied_by(vector)
        if not vector_validation_result.is_success:
            raise vector_validation_result.exception

        v = vector_validation_result.payload
        return CoordinateBuilder.build(row=v.y, column=v.x).payload


    @staticmethod
    def convert_to_vector(coordinate: Coordinate) -> Vector:

        coord_validation_result = CoordinateSpecification.is_satisfied_by(coordinate)
        if not coord_validation_result.is_success:
            raise coord_validation_result.exception

        c = coord_validation_result.payload

        vector_validation_result = VectorSpecification.is_satisfied_by(Vector(x=c.column, y=c.row))
        if not vector_validation_result.is_success:
            raise vector_validation_result.exception

        return vector_validation_result.payload
        """Converts a coordinate to a vector."""

        return Vector(x=coordinate.column, y=coordinate.row)


    @staticmethod
    def scalar_multiply(vector: Vector, scalar: Scalar) -> Vector:

        scalar_validation_result = ScalarSpecification.is_satisfied_by(scalar)
        if not scalar_validation_result.is_success:
            raise scalar_validation_result.exception

        s = scalar_validation_result.payload

        vector_validation_result = VectorSpecification.is_satisfied_by(vector)
        if not vector_validation_result.is_success:
            raise vector_validation_result.exception

        v = vector_validation_result.payload

        candidate = Vector(v.x  * s.value, y=v.y * s.value)

        candidate_validation_result = VectorSpecification.is_satisfied_by(candidate)
        if not candidate_validation_result.is_success:
            raise candidate_validation_result.exception

        return candidate_validation_result.payload


    @staticmethod
    def add_vector_to_coordinate(coordinate: Coordinate, vector: Vector) -> Coordinate:
        """Adds a vector to a coordinate."""

        coord_validation_result = CoordinateSpecification.is_satisfied_by(coordinate)
        if not coord_validation_result.is_success:
            raise coord_validation_result.exception

        c = coord_validation_result.payload

        vector_validation_result = VectorSpecification.is_satisfied_by(vector)
        if not vector_validation_result.is_success:
            raise vector_validation_result.exception

        v = vector_validation_result.payload

        candidate = Coordinate(row=c.row + v.y, column=c.column + v.x)
        # print("vector", v, "candidate:", candidate)
        candidate_validation_result = CoordinateSpecification.is_satisfied_by(candidate)
        if not candidate_validation_result.is_success:
            raise candidate_validation_result.exception

        return candidate_validation_result.payload


    @staticmethod
    def dot_product(vector_a, vector_b):
        """Calculates the dot product of two vectors."""
        if len(vector_a) != len(vector_b):
            raise ValueError("Vectors must be of the same length")
        return sum(a * b for a, b in zip(vector_a, vector_b))