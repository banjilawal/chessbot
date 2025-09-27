from enum import Enum

from assurance import ThrowHelper
from chess.common import ROW_SIZE, COLUMN_SIZE, BuildResult
from chess.coord import (
    Coord,
    NullRowException, NullColumnException,
    RowBelowBoundsException, RowAboveBoundsException,
    ColumnBelowBoundsException, ColumnAboveBoundsException,
    CoordBuilderException
)


class CoordBuilder(Enum):

    @staticmethod
    def build(row: int, column: int) -> BuildResult[Coord]:

        method = "CoordBuilder.build"
        try:

            # If cannot cast from t to Coord need to break
            if not isinstance(t, Coord):
                raise TypeError(f"{method} Expected a Coord, got {type(t).__name__}")

            # cast and run checks for the fields
            coordinate = cast(Coord, t)


            if row is None:
                ThrowHelper.throw_if_invalid(
                    CoordBuilder,
                    NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")
                )
            if row < 0:
                ThrowHelper.throw_if_invalid(
                    CoordBuilder,
                    RowBelowBoundsException(f"{method} {RowBelowBoundsException.DEFAULT_MESSAGE}")
                )
            if row >= ROW_SIZE:
                ThrowHelper.throw_if_invalid(
                    CoordBuilder,
                    RowAboveBoundsException(f"{method} {RowAboveBoundsException.DEFAULT_MESSAGE}")
                )


            if column is None:
                ThrowHelper.throw_if_invalid(
                    CoordBuilder,
                    NullColumnException(f"{method} {NullRowException.DEFAULT_MESSAGE}")
                )
            if column < 0:
                ThrowHelper.throw_if_invalid(
                    CoordBuilder,
                    ColumnBelowBoundsException(f"{method} {ColumnBelowBoundsException.DEFAULT_MESSAGE}")
                )
            if column >= COLUMN_SIZE:
                ThrowHelper.throw_if_invalid(
                    CoordBuilder,
                    ColumnAboveBoundsException(f"{method} {ColumnAboveBoundsException.DEFAULT_MESSAGE}")
                )
            return BuildResult(payload=Coord(row=row, column=column))

        except Exception as e:
            raise CoordBuilderException(f"{method}: {CoordBuilderException.DEFAULT_MESSAGE}")

