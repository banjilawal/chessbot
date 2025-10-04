from enum import Enum

from assurance import ThrowHelper
from chess.system import ROW_SIZE, COLUMN_SIZE, BuildResult
from chess.coord import (
    Coord,
    NullRowException, NullColumnException,
    RowBelowBoundsException, RowAboveBoundsException,
    ColumnBelowBoundsException, ColumnAboveBoundsException,
    CoordBuilderException
)


class CoordBuilder(Enum):
    """
    Builder class responsible for safely constructing `Coord` instances.
    
    `CoordBuilder` ensures that `Coord` objects are always created successfully by performing comprehensive validate
    checks during construction. This separates the responsibility of building from validating `CoordBuilder` focuses on
    creation while `CoordValidator` is used for validating existing `Coord` instances that are passed around the system.
    
    The build runs through all validate checks individually to guarantee that any `Coord` instance it produces meets
    all required specifications before construction completes.
    
    Usage:
        ```python
        # Safe construction of a Coord instance if and only if the parameters meet specs
        build_outcome = CoordBuilder.build(row=1, column=1)
        if not build_outcome.is_success():
            raise build_outcome.err
        coord = cast(Coord, build_outcome.payload)
        ```
    
    See Also:
        `Coord`: Fundamental data structure for representing coordinates on a chessboard.
        `CoordValidator`: Used for validating existing `Coord` instances
        `BuildResult`: Return type containing the built `Coord` or err information
    """

    @staticmethod
    def build(row: int, column: int) -> BuildResult[Coord]:
        """
        Constructs a new `Coord` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validate checks on each component to ensure the resulting `Coord` meets all
        specifications. If all checks are passed, a `Coord` instance will be returned. It is not necessary to perform
        any additional validate checks on the returned `Coord` instance. This method guarantees if a `BuildResult`
        with a successful status is returned, the contained `Coord` is valid and ready for use.

        Args:
            `row` (int): The row index on `Board` where `Coord` is located. Must not be Nll
                and must `Board` dimension bounds.
            `column` (int): The column index on `Board` where `Coord` is located. Must not be Nll
                and must `Board` dimension bounds.

        Returns:
            BuildResult[Coord]: A `BuildResult` containing either:
                - On success: A valid `Coord` instance in the payload
                - On failure: Error information and err details

        Raises:
            `CoordBuilderException`: Wraps any underlying validate failures that occur during the construction process.
            This includes:
                * `NullRowException`: if `row` is null
                * `RowBelowBoundsException`: if `row` < 0
                * `RowAboveBoundsException`: if `row` >= `ROW_SIZE`
                * `NullColumnException`: if `column` is null
                * `ColumnBelowBoundsException`: if `column` < 0
                * `ColumnAboveBoundsException`: if `column` >= `ROW_SIZE`

        Note:
            The build runs through all the checks on parameters and state to guarantee only a valid `Coord` is
            created, while `CoordValidator` is used for validating `Coord` instances that are passed around after
            creation. This separation of concerns makes the validate and building independent of each other and
            simplifies maintenance.

        Example:
            ```python
            from typing import cast
            from chess.coord import Coord, CoordBuilder
            
            # Creates a valid coord
            build_outcome = CoordBuilder.build(x=2, y=1)
            
            if not build_outcome.is_success():
                raise build_outcome.err # <--- Skips this because x and y are valid
            u = cast(Coord, build_outcome.payload) # <-- executes this line
            ```
        """
        method = "CoordBuilder.build"

        try:
            if row is None:
                ThrowHelper.propagate_error(
                    CoordBuilder,
                    NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")
                )
            if row < 0:
                ThrowHelper.propagate_error(
                    CoordBuilder,
                    RowBelowBoundsException(f"{method} {RowBelowBoundsException.DEFAULT_MESSAGE}")
                )
            if row >= ROW_SIZE:
                ThrowHelper.propagate_error(
                    CoordBuilder,
                    RowAboveBoundsException(f"{method} {RowAboveBoundsException.DEFAULT_MESSAGE}")
                )


            if column is None:
                ThrowHelper.propagate_error(
                    CoordBuilder,
                    NullColumnException(f"{method} {NullRowException.DEFAULT_MESSAGE}")
                )
            if column < 0:
                ThrowHelper.propagate_error(
                    CoordBuilder,
                    ColumnBelowBoundsException(f"{method} {ColumnBelowBoundsException.DEFAULT_MESSAGE}")
                )
            if column >= COLUMN_SIZE:
                ThrowHelper.propagate_error(
                    CoordBuilder,
                    ColumnAboveBoundsException(f"{method} {ColumnAboveBoundsException.DEFAULT_MESSAGE}")
                )
            return BuildResult(payload=Coord(row=row, column=column))

        except Exception as e:
            raise CoordBuilderException(f"{method}: {CoordBuilderException.DEFAULT_MESSAGE}")

