from enum import Enum

from chess.coord import Coord, CoordValidator
from assurance import ThrowHelper
from chess.common import BuildResult, IdValidator, NameValidator
from chess.square import Square, SquareBuilderException




class SquareBuilder(Enum):
    """
    Builder class responsible for safely constructing `Square` instances.

    `SquareBuilder` ensures that `Square` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `SquareBuilder` 
     focuses on creation while `SquareValidator` is used for validating existing `Square` instances that are passed 
     around the system.

    The builder runs through all validation checks individually to guarantee that any `Square` instance it produces 
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
    
    @staticmethod
    def build(square_id:int, name: str, coord: Coord) -> BuildResult[Square]:
        """
        Constructs a new `Square` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `Square` meets all 
        specifications. If all checks are passed, a `Square` instance will be returned. It is not necessary to perform 
        any additional validation checks on the returned `Square` instance. This method guarantees if a `BuildResult` 
        with a successful status is returned, the contained `Square` is valid and ready for use.

        Args:
            `discovery_id` (`int`): The unique id for the piece. Must pass `IdValidator` checks.
            `name` (`Name`): Must pass `NameValidator` checks.
            `coord` (`Coord`): Where `Square` is located on a `Board`. Must pass `CoordValidator` checks.

        Returns:
            BuildResult[Square]: A `BuildResult` containing either:
                - On success: A valid `Square` instance in the payload
                - On failure: Error information and exception details

        Raises:
            `SquareBuilderException`: Wraps any underlying validation failures that occur during the construction
             process. This includes:
                * `IdValidationException`: if `id` fails validation checks`
                * `NameValidationException`: if `name` fails validation checks
                * `CoordValidationException`: if `coord` fails validation checks
                * `SquareBuilderException`: for any other construction failures

        Note:
            The builder runs through all the checks on parameters and state to guarantee only a valid `Square` is 
            created, while `SquareValidator` is used for validating `Square` instances that are passed around after 
            creation. This separation of concerns makes the validation and building independent of each other and 
            simplifies maintenance.

        Example:
            ```python
            # Valid square creation
            result = SquareBuilder.build(square_id=1, name=black-name, profile=black_square_profile)
            if result.is_success():
                square = cast(Square, result.payload) # Guaranteed valid Square

            # Null name will fail gracefully
            result = SquareBuilder.build(square_id=1, name=None, profile=black_square_profile)
            if not result.is_success():
                # Handle construction failure
                pass
            ```
        """
        method = "SquareBuilder.build"

        try:
            id_validation = IdValidator.validate(square_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(SquareBuilder, id_validation.exception)
                
            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                ThrowHelper.throw_if_invalid(SquareBuilder, name_validation.exception)
                
            coord_result = CoordValidator.validate(coord)
            if not coord_result.is_success():
                ThrowHelper.throw_if_invalid(SquareBuilder, coord_result.exception)

            return BuildResult(payload=Square(square_id=square_id, name=name, coord=coord))

        except Exception as e:
            raise SquareBuilderException(f"{method}: {SquareBuilderException.DEFAULT_MESSAGE}")


# def main():
#     build_result = SquareBuilder.build(square_id=id_emitter.square_id, name="A3", coordinate=Coord(0, 0))
#     if build_result.is_success():
#         square = cast(Square, build_result.payload)
#         print(f"Successfully built square: {square}")
#     else:
#         print(f"Failed to build square: {build_result.exception}")
#
#     build_result = SquareBuilder.build(square_id=-1, name="", coordinate=Coord(0, 0))
#     if build_result.is_success():
#         square = cast(Square, build_result.payload)
#         print(f"Successfully built square: {square}")
#     else:
#         print(f"Failed to build square: {build_result.exception}")
#
# if __name__ == "__main__":
#     main()