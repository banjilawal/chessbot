from chess.geometry.vector.delta import Vector


class VectorProduct:
    @staticmethod

    def scalar_multiply(vector: Vector, scalar: Scalar) -> Vector:
        """Multiplies a vector by a scalar."""
        if scalar:

        return [component * scalar for component in vector]

    @staticmethod
    def dot_product(vector_a, vector_b):
        """Calculates the dot product of two vectors."""
        if len(vector_a) != len(vector_b):
            raise ValueError("Vectors must be of the same length")
        return sum(a * b for a, b in zip(vector_a, vector_b))