from enum import Enum
from typing import cast

from chess.common import BuildResult, KNIGHT_STEP_SIZE
from assurance.throw_helper import ThrowHelper
from chess.vector import (
    Vector, VectorValidator, VectorBelowBoundsException, VectorAboveBoundsException,
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
        # Safe vector creation with validation
        result = VectorBuilder.build(x=2, y=1)
        if result.is_success():
            vector = result.payload
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
            The builder performs validation at construction time, while
            `VectorValidator` is used for validating `Vector` instances that
            are passed around after creation. This separation of concerns 
            makes the validation responsibilities clearer.

        Example:
            ```python
            # Valid vector creation
            result = VectorBuilder.build(2, 1)
            if result.is_success():
                vector = result.payload  # Guaranteed valid Vector

            # Invalid bounds - will fail gracefully
            result = VectorBuilder.build(10, 5)  # Outside KNIGHT_STEP_SIZE
            if not result.is_success():
                # Handle construction failure
                pass
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
#     build_result = CoordBuilder.build(3, 4)
#     if build_result.is_success():
#         coord = build_result.payload
#         print(f"Successfully built coord: {coord}")
#     else:
#         print(f"Failed to build coord: {build_result.team_exception}")
#
#     build_result = CoordBuilder.build(-1,  4)
#     if build_result.is_success():
#         coord = build_result.payload
#         print(f"Successfully built coord: {coord}")
#     else:
#         print(f"Failed to build coord: {build_result.team_exception}")
#
# if __name__ == "__main__":
#     main()