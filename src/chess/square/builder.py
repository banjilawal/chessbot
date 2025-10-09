from enum import Enum

from assurance import ThrowHelper
from chess.coord import Coord, CoordValidator
from chess.square import Square, SquareBuildFailed
from chess.system import BuildResult, IdValidator, NameValidator, Builder


class SquareBuilder(Builder[[Square]]):
  """
  Builder class responsible for safely constructing `Square` instances.

  `SquareBuilder` ensures that `Square` objects are always created successfully by performing comprehensive validate
   checks during construction. This separates the responsibility of building from validating - `SquareBuilder`
   focuses on creation while `SquareValidator` is used for validating existing `Square` instances that are passed
   around the system.

  The build runs through all validate checks individually to guarantee that any `Square` instance it produces
  meets all required specifications before construction completes

  Usage:
    ```python
    # Safe square creation
    build_result = SquareBuilder.build(square_id=1, name="A-1", coordinate=Coord(0, 0))

    if build_result.is_success():
      square = build_result.payload
    ```

  See Also:
    `Square`: The data structure being constructed
    `SquareValidator`: Used for validating existing `Square` instances
    `BuildResult`: Return type containing the built `Square` or error information
  """

  @classmethod
  def build(cls, name: str, coord: Coord) -> BuildResult[Square]:
    """
    Constructs team new `Square` instance with comprehensive checks on the parameters and states during the
    build process.

    Performs individual validate checks on each component to ensure the resulting `Square` meets all
    specifications. If all checks are passed, team `Square` instance will be returned. It is not necessary to perform
    any additional validate checks on the returned `Square` instance. This method guarantees if team `BuildResult`
    with team successful status is returned, the contained `Square` is valid and ready for use.

    Args:
      `discovery_id` (`int`): The unique id for the piece. Must pass `IdValidator` checks.
      `name` (`Name`): Must pass `NameValidator` checks.
      `coord` (`Coord`): Where `Square` is located on team `Board`. Must pass `CoordValidator` checks.

    Returns:
      BuildResult[Square]: A `BuildResult` containing either:
        - On success: A valid `Square` instance in the payload
        - On failure: Error information and error details

    Raises:
      `SquareBuildFailed`: Wraps any underlying validate failures that occur during the construction
       process. This includes:
        * `InvalidIdException`: if `id` fails validate checks`
        * `InvalidNameException`: if `name` fails validate checks
        * `InvalidCoordException`: if `coord` fails validate checks
        * `SquareBuildFailed`: for any other construction failures

    Note:
      The build runs through all the checks on parameters and state to guarantee only team valid `Square` is
      created, while `SquareValidator` is used for validating `Square` instances that are passed around after
      creation. This separation of concerns makes the validate and building independent of each other and
      simplifies maintenance.

    Example:
      ```python
      # Valid square creation
      result = SquareBuilder.build(square_id=1, name=black-name, schema=black_square_profile)
      if result.is_success():
        square = cast(Square, result.payload) # Guaranteed valid Square

      # Null name will fail gracefully
      result = SquareBuilder.build(square_id=1, name=None, schema=black_square_profile)
      if not result.is_success():
        # Handle construction failure
        pass
      ```
    """
    method = "SquareBuilder.build"

    try:
      id_validation = IdValidator.validate(square_id)
      if not id_validation.is_success():
        ThrowHelper.log_and_raise_error(SquareBuilder, id_validation.exception)

      name_validation = NameValidator.validate(name)
      if not name_validation.is_success():
        ThrowHelper.log_and_raise_error(SquareBuilder, name_validation.exception)

      coord_result = CoordValidator.validate(coord)
      if not coord_result.is_success():
        ThrowHelper.log_and_raise_error(SquareBuilder, coord_result.exception)

      return BuildResult(payload=Square(square_id=square_id, name=name, coord=coord))

    except Exception as e:
      raise SquareBuildFailed(f"{method}: {SquareBuildFailed.DEFAULT_MESSAGE}")


# def main():
#   build_result = SquareBuilder.build(square_id=id_emitter.square_id, name="A3", coordinate=Coord(0, 0))
#   if build_result.is_success():
#     square = cast(Square, build_result.payload)
#     print(f"Successfully built square: {square}")
#   else:
#     print(f"Failed to build square: {build_result.err}")
#
#   build_result = SquareBuilder.build(square_id=-1, name="", coordinate=Coord(0, 0))
#   if build_result.is_success():
#     square = cast(Square, build_result.payload)
#     print(f"Successfully built square: {square}")
#   else:
#     print(f"Failed to build square: {build_result.err}")
#
# if __name__ == "__main__":
#   main()