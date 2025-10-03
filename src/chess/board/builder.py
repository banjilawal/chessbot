from typing import List

from chess.coord import Coord
from chess.square import Square
from assurance import ThrowHelper
from chess.board import Board, BoardBuilderException
from chess.system import id_emitter, BuildResult, IdValidator, InvalidIdException, BOARD_DIMENSION



class BoardBuilder:
    """
    Builder class responsible for safely constructing `Board` instances.

    `BoardBuilder` ensures that `Board` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `BoardBuilder` 
     focuses on creating while `BoardValidator` is used for validating existing `Board` instances that are passed
     around the system.

    The build runs through all validation checks individually to guarantee that any `Board` instance it produces
    meets all required specifications before construction completes

    Usage:
        ```python
        from typing import cast
        from chess.system import BuildResult
        from chess.board import Board, BoardBuilder, BoardBuilderException
        
        # Safe board creation
        build_result = BoardBuilder.build(board_id=id_emitter.board_id)

        if not build_result.is_success():
            raise build_result.exception
        board = cast(Board, build_result.payload)
        ```

    See Also:
        `Board`: The data structure being constructed
        `BoardValidator`: Used for validating existing `Board` instances
        `BuildResult`: Return type containing the built `Board` or exception information
    """

    @staticmethod
    def build() -> BuildResult[Board]:
        """
        Constructs a new `Board` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `Board` meets all 
        specifications. If all checks are passed, a `Board` instance will be returned. It is not necessary to perform 
        any additional validation checks on the returned `Board` instance. This method guarantees if a `BuildResult` 
        with a successful status is returned, the contained `Board` is valid and ready for use.

        Args:
           `board_id`(`int`): The unique id for the board. Must pass `IdValidator` checks.

        Returns:
            BuildResult[Board]: A `BuildResult` containing either:
                - On success: A valid `Board` instance in the payload
                - On failure: Error information and exception details

        Raises:
            `BoardBuilderException`: Wraps any underlying validation failures that occur during the construction
            process. This includes:
                * `InvalidIdException``: if `board_id` `IdValidator.validate` returns an exception

        Note:
            The build runs through all the checks on parameters and state to guarantee only a valid `Board` is
            created, while `BoardValidator` is used for validating `Board` instances that are passed around after 
            creation. This separation of concerns makes the validation and building independent of each other and 
            simplifies maintenance.

        Example:
            ```python
            # Valid board creation
            build_outcome = BoardBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            board = cast(Board, build_outcome.payload)
            ```
        """
        method = "BoardBuilder.build"
        
        try:
            squares: List[List[Square]] = []
            for i in range(BOARD_DIMENSION):
                row_squares: List[Square] = []
                ascii_value = ord('A')
    
                for j in range(BOARD_DIMENSION):
                    name = chr(ascii_value) + str(i + 1)
                    coord = Coord(row=i, column=j)
                    square = Square(id_emitter.square_id, name, coord)
    
                    row_squares.append(square)
                    ascii_value += 1
                squares.append(row_squares)
            return BuildResult(payload=Board(board_id=board_id, squares=squares))

        except InvalidIdException as e:
            raise BoardBuilderException(f"{method}: {BoardBuilderException.DEFAULT_MESSAGE}") from e



def main():
    board = BoardBuilder.build(id_emitter.board_id)
    print(board)

if __name__ == "__main__":
    main()


