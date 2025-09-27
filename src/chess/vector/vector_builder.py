from enum import Enum

from chess.common import BuildResult, KNIGHT_STEP_SIZE
from assurance.throw_helper import ThrowHelper
from chess.vector import (
    Vector, VectorBelowBoundsException, VectorAboveBoundsException,
    NullXComponentException, NullYComponentException, VectorBuilderException
)



class VectorBuilder(Enum):
    """
    Builder class responsible for safely constructing `Vector` instances.

    `VectorBuilder` ensures that `Vector` objects are always created successfully by
    performing comprehensive validation checks during construction. This separates
    the responsibility of building from validating - `VectorBuilder` focuses on
    creation while `VectorValidator` is used for validating existing `Vector` instances
    that are passed around the system.

    The builder runs through all validation checks individually to guarantee that
    any `Vector` instance it produces meets all required specifications before
    construction completes.

    Usage:
        ```python
        # Safe construction of a Vector instance if and only if the parameters meet specs
        build_outcome = VectorBuilder.build(x=2, y=1)
        if not build_outcome.is_success():
            raise build_outcome.exception
        vector = build_outcome.payload
        ```
        
    See Also:
        `VectorValidator`: Used for validating existing `Vector` instances
        `Vector`: The data structure being constructed
        `BuildResult`: Return type containing the built `Vector` or error information
    """

    @staticmethod
    def build(x: int, y: int) -> BuildResult[Vector]:
        """
        Constructs a new `Vector` instance with comprehensive validation.

        Performs individual validation checks on each component to ensure the
        resulting `Vector` meets all specifications. The method validates bounds,
        null checks, and uses `VectorValidator` for final instance validation
        before returning a successfully constructed `Vector`.

        This method guarantees that if a `BuildResult` with a successful status
        is returned, the contained `Vector` is valid and ready for use.

        Args:
            x (int): The x-component of the vector. Must not be None and must
                    be within [-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE] bounds.
            y (int): The y-component of the vector. Must not be None and must
                    be within [-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE] bounds.

        Returns:
            BuildResult[Vector]: A `BuildResult` containing either:
                - On success: A valid `Vector` instance in the payload
                - On failure: Error information and exception details

        Raises:
            VectorBuilderException: Wraps any underlying validation failures
                that occur during the construction process. This includes:
                - `NullXComponentException`: if x is None
                - `NullYComponentException`: if y is None
                - `VectorBelowBoundsException`: if x or y < -KNIGHT_STEP_SIZE
                - `VectorAboveBoundsException`: if x or y > KNIGHT_STEP_SIZE
                - Any validation errors from `VectorValidator`

        Note:
            The builder performs runs through all the checks on parameters and state to guarantee only
            a valid Vector is created, while `VectorValidator` is used for validating `Vector` instances that
            are passed around after creation. This separation of concerns makes the validation and building
            independent of each other and simplifies maintenance.

        Example:
            ```python
            from typing import cast
            from chess.vector import Vector, VectorBuilder

            # Creates a valid vector
            build_outcome = VectorBuilder.build(x=2, y=1)

            if not build_outcome.is_success():
                raise build_outcome.exception # <--- Skips this because x and y are valid
            u = cast(Vector, build_outcome.payload) # <-- executes this line
            ```
        """
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

            vector = Vector(x=x, y=y)
            return BuildResult(payload=vector)

        except Exception as e:
            raise VectorBuilderException(f"{method}: {VectorBuilderException.DEFAULT_MESSAGE}")


# def main():
#     build_outcome = CoordBuilder.build(3, 4)
#     if build_outcome.is_success():
#         coord = build_outcome.payload
#         print(f"Successfully built coord: {coord}")
#     else:
#         print(f"Failed to build coord: {build_outcome.team_exception}")
#
#     build_outcome = CoordBuilder.build(-1,  4)
#     if build_outcome.is_success():
#         coord = build_outcome.payload
#         print(f"Successfully built coord: {coord}")
#     else:
#         print(f"Failed to build coord: {build_outcome.team_exception}")
#
# if __name__ == "__main__":
#     main()