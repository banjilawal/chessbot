# src/chess/coord/builder.py

"""
Module: chess.coord.builder
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""

from chess.system import Builder, BuildResult, ROW_SIZE, COLUMN_SIZE, LoggingLevelRouter
from chess.coord import (
    Coord, NullRowException, NullColumnException, RowBelowBoundsException, RowAboveBoundsException,
    ColumnBelowBoundsException, ColumnAboveBoundsException, CoordBuildFailedException
)


class CoordBuilder(Builder[Coord]):
    """
    # ROLE: Builder, Data Integrity Guarantor

    # RESPONSIBILITIES:
    Produce Coord instances whose integrity is always guaranteed. If any attributes do not pass their integrity checks,
    send an exception instead.

    # PROVIDES:
    BuildResult[Coord] containing either:
        - On success: Coord in payload.
        - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, row: int, column: int) -> BuildResult[Coord]:
        """
        # ACTION:
        1.  Check candidate.row is:
                *   an INT
                *   between 0 and ROW_SIZE - 1 inclusive.
        2. Check candidate.column is:
                *   an INT
                *   between 0 and ROW_SIZE - 1 inclusive.
        3.  If any check fails, return the exception inside a ValidationResult.
        4.  When all checks pass cast candidate to a Coord instance then return inside a ValidationResult.

        # PARAMETERS:
            *   row (int)
            *   column (int)

        # Returns:
        ValidationResult[Coord] containing either:
            - On success: Coord in payload.
            - On failure: Exception.

        # RAISES:
            *   NullRowException
            *   RowBelowBoundsException
            *   RowAboveBoundsException
            *   NullColumnException
            *   ColumnBelowBoundsException
            *   ColumnAboveBoundsException
            *   InvalidCoordException
        """
        method = "CoordBuilder.build"
        
        try:
            if row is None:
                return BuildResult.failure(
                    NullRowException(f"{method}: {NullRowException.DEFAULT_MESSAGE}")
                )
            
            if row < 0:
                return BuildResult.failure(
                    RowBelowBoundsException(
                        f"{method}: {RowBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if row >= ROW_SIZE:
                return BuildResult.failure(
                    RowAboveBoundsException(
                        f"{method}: {RowAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if column is None:
                return BuildResult.failure(
                    NullColumnException(f"{method}: {NullRowException.DEFAULT_MESSAGE}")
                )
            
            if column < 0:
                return BuildResult.failure(
                    ColumnBelowBoundsException(
                        f"{method}: {ColumnBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if column >= COLUMN_SIZE:
                return BuildResult.failure(
                    ColumnAboveBoundsException(
                        f"{method}: {ColumnAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return BuildResult.success(payload=Coord(row=row, column=column))
        
        except Exception as ex:
            return BuildResult.failure(
                CoordBuildFailedException(
                    f"{method}: {CoordBuildFailedException.DEFAULT_MESSAGE}",
                    ex
                )
            )