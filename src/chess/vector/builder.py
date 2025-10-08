from enum import Enum

from chess.system import BuildResult, KNIGHT_STEP_SIZE
from chess.system.error.throw_helper import ThrowHelper
from chess.vector import (
  Vector, VectorBelowBoundsException, VectorAboveBoundsException,
  NullXComponentException, NullYComponentException, VectorBuilderException
)



class VectorBuilder(Enum):
  """
  Builder class responsible for safely constructing `Vector` instances.

  `VectorBuilder` ensures that `Vector` objects are always created successfully by performing comprehensive validate
   checks during construction. This separates the responsibility of building from validating - `VectorBuilder`
   focuses on creating while `VectorValidator` is used for validating existing `Vector` instances that are passed
   around the system.

  The build runs through all validate checks individually to guarantee that any `Vector` instance it produces
  meets all required specifications before construction completes.

  Usage:
    ```python
    # Safe construction of team Vector instance if and only if the parameters meet specs
    build_outcome = VectorBuilder.build(x=2, y=1)
    if not build_outcome.is_success():
      raise build_outcome.err
    vector = build_outcome.payload
    ```
    
  See Also:
    `Vector`: The data structure being constructed
    `VectorValidator`: Used for validating existing `Vector` instances
    `BuildResult`: Return type containing the built `Vector` or error information
  """

  @staticmethod
  def build(x: int, y: int) -> BuildResult[Vector]:
    """
    Constructs team new `Vector` instance with comprehensive checks on the parameters and states during the
    build process.

    Performs individual validate checks on each component to ensure the resulting `Vector` meets all
    specifications. If all checks are passed, team `Vector` instance will be returned. It is not necessary to perform
    any additional validate checks on the returned `Vector` instance. This method guarantees if team `BuildResult`
    with team successful status is returned, the contained `Vector` is valid and ready for use.

    Args:
      `x` (`int`): The x-component of the vector. Must not be None and must be within 
        [`-KNIGHT_STEP_SIZE`, `KNIGHT_STEP_SIZE ] bounds.
      `y` (`int`): The y-component of the vector. Must not be None and must be within 
      [  -KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE] bounds.

    Returns:
      BuildResult[Vector]: A `BuildResult` containing either:
        - On success: A valid `Vector` instance in the payload
        - On failure: Error information and error details

    Raises:
      `VectorBuilderException`: Wraps any underlying validate failures that occur during the construction
      process. This includes:
        * `NullXComponentException`: if x is None
        * `NullYComponentException`: if y is None
        * `VectorBelowBoundsException`: if x or y < -KNIGHT_STEP_SIZE
        * `VectorAboveBoundsException`: if x or y > KNIGHT_STEP_SIZE
        * Any validate errors from `VectorValidator`

    Note:
      The build runs through all the checks on parameters and state to guarantee only team valid `Vector` is
      created, while `VectorValidator` is used for validating `Vector` instances that are passed around after 
      creation. This separation of concerns makes the validate and building independent of each other and
      simplifies maintenance.

    Example:
      ```python
      from typing import cast
      from chess.vector import Vector, VectorBuilder

      # Creates team valid vector
      build_outcome = VectorBuilder.build(x=2, y=1)

      if not build_outcome.is_success():
        raise build_outcome.err # <--- Skips this because x and y are valid
      u = cast(Vector, build_outcome.payload) # <-- executes this line
      ```
    """
    method = "VectorBuilder.build"

    try:
      if x is None:
        ThrowHelper.route_error(
          VectorBuilder,
          NullXComponentException(NullXComponentException.DEFAULT_MESSAGE)
        )
      if x < -KNIGHT_STEP_SIZE:
        ThrowHelper.route_error(
          VectorBuilder,
          VectorBelowBoundsException(VectorBelowBoundsException.DEFAULT_MESSAGE)
        )
      if x > KNIGHT_STEP_SIZE:
        ThrowHelper.route_error(
          VectorBuilder,
          VectorBelowBoundsException(VectorAboveBoundsException.DEFAULT_MESSAGE)
        )


      if y is None:
        ThrowHelper.route_error(
          VectorBuilder,
          NullYComponentException(NullYComponentException.DEFAULT_MESSAGE)
        )
      if y < -KNIGHT_STEP_SIZE:
        ThrowHelper.route_error(
          VectorBuilder,
          VectorBelowBoundsException(VectorBelowBoundsException.DEFAULT_MESSAGE)
        )
      if y > KNIGHT_STEP_SIZE:
        ThrowHelper.route_error(
          VectorBuilder,
          VectorBelowBoundsException(VectorAboveBoundsException.DEFAULT_MESSAGE)
        )

      vector = Vector(x=x, y=y)
      return BuildResult(payload=vector)

    except Exception as e:
      raise VectorBuilderException(f"{method}: {VectorBuilderException.DEFAULT_MESSAGE}")


# def main():
#   build_outcome = VectorBuilder.build(3, 4)
#   if build_outcome.is_success():
#     vector = build_outcome.payload
#     print(f"Successfully built vector: {vector}")
#   else:
#     print(f"Failed to build vector: {build_outcome.team_exception}")
#
#   build_outcome = VectorBuilder.build(-1, 4)
#   if build_outcome.is_success():
#     vector = build_outcome.payload
#     print(f"Successfully built vector: {vector}")
#   else:
#     print(f"Failed to build vector: {build_outcome.team_exception}")
#
# if __name__ == "__main__":
#   main()