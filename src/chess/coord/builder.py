# chess/coord/old_occupation_validator.py

"""
Module: `chess.coord.validator`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

Contains: CoordBuilder
 Provides: Create `Coord` instances 
"""

from chess.system import Builder, ROW_SIZE, COLUMN_SIZE, BuildResult, LoggingLevelRouter, LoggingLevelRouter
from chess.coord import (
    Coord, NullRowException, NullColumnException, RowBelowBoundsException, RowAboveBoundsException,
    ColumnBelowBoundsException, ColumnAboveBoundsException, CoordBuildFailedException
)


class CoordBuilder(Builder[Coord]):
    
    @classmethod
    def build(cls, row: int, column: int) -> BuildResult[Coord]:
        """"""
        method = "CoordBuilder.build"
        
        try:
            if row is None:
                return BuildResult(exception=NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}"))
            
            if row < 0:
                return BuildResult(
                    exception=RowBelowBoundsException(
                        f"{method} {RowBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if row >= ROW_SIZE:
                return BuildResult(
                    exception=RowAboveBoundsException(
                        f"{method} {RowAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if column is None:
                return BuildResult(exception=NullColumnException(f"{method} {NullRowException.DEFAULT_MESSAGE}"))
            
            if column < 0:
                return BuildResult(
                    exception=ColumnBelowBoundsException(
                        f"{method} {ColumnBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if column >= COLUMN_SIZE:
                return BuildResult(
                    exception=ColumnAboveBoundsException(
                        f"{method} {ColumnAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return BuildResult(payload=Coord(row=row, column=column))
        
        except Exception as e:
            return BuildResult(exception=e)
