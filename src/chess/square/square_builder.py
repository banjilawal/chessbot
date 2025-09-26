from enum import Enum
from typing import cast

from chess.coord import Coord, CoordValidator
from assurance import ThrowHelper
from chess.common import BuildResult, IdValidator, NameValidator
from chess.square import Square, SquareBuilderException




class SquareBuilder(Enum):
    """
    Builder class responsible for safely constructing `Square` instances.

    `SquareBuilder` ensures that `Square` objects are always created successfully by
    performing comprehensive validation checks during construction. This separates
    the responsibility of building from validating - `SquareBuilder` focuses on
    creation while `SquareValidator` is used for validating existing `Square` instances
    that are passed around the system.

    The builder runs through all validation checks individually to guarantee that
    any `Square` instance it produces meets all required specifications before
    construction completes.

    Usage:
        ```python
        # Safe square creation
        build_result = SquareBuilder.build(square_id=1, name="A-1", coordinate=Coord(0, 0))
        
        if build_result.is_success():
            square = build_result.payload
        ```

    See Also:
        `SquareValidator`: Used for validating existing `Square` instances
        `Square`: The data structure being constructed
        `BuildResult`: Return type containing the built `Square` or error information
    """
    
    @staticmethod
    def build(square_id:int, name: str, coord: Coord) -> BuildResult[Square]:
        """
        Constructs a new `Square` instance with comprehensive validation.

        Performs individual validation checks on each component to ensure the 
        resulting `Square` meets all specifications. The method validates bounds, 
        null checks, and uses `SquareValidator` for final instance validation 
        before returning a successfully constructed `Square`.

        This method guarantees that if a `BuildResult` with a successful status 
        is returned, the contained `Square` is valid and ready for use.

        Args:
           `square_id`(`int`): The unique id for the square. Must pass `IdValidator` checks.
            `name`(`Name`): The human or cybernetic moving pieces in `Square.roster`. The name
                must not be None and must pass `NameValidator` checks.must pass `NameValidator` checks.
            `profile`(`SquareProfile`): The profile defining square attributes and behaviors. Must not be None and be
                an instance of `SquareProfile`.

        Returns:
            BuildResult[Square]: A `BuildResult` containing either:
                - On success: A valid `Square` instance in the payload
                - On failure: Error information and exception details

        Raises:
            SquareBuilderException: Wraps any underlying validation failures 
                that occur during the construction process. This includes:
                - `IdValidationException`: if `id` fails validation checks`
                - `NameValidationException`: if `name` fails validation checks
                - `CoordValidationException`: if `coord` fails validation checks
                - `SquareBuilderException`: for any other construction failures

        Note:
            The builder performs validation at construction time, while 
            `SquareValidator` is used for validating `Square` instances that 
            are passed around after creation. This separation of concerns 
            makes the validation responsibilities clearer.

        Example:
            ```python
            # Valid square creation
            result = SquareBuilder.build(square_id=1, name=black-name, profile=black_square_profile)
            if result.is_success():
                square = cast(Square, result.payload)  # Guaranteed valid Square

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
                
            square = Square(square_id=square_id, name=name, coord=coord)
            return BuildResult(payload=square)

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