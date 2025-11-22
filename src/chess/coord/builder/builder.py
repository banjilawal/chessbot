# src/chess/coord/builder/builder.py

"""
Module: chess.coord.builder.builder
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""


from chess.system import Builder, BuildResult,  LoggingLevelRouter
from chess.coord import Coord, CoordValidator,  CoordBuildFailedException



class CoordBuilder(Builder[Coord]):
    """
    # ROLE: Builder, Data Integrity Guarantor

    # RESPONSIBILITIES:
    Produce Coord instances whose integrity is always guaranteed. If any attributes do
    not pass their integrity checks, send an exception instead.

    # PROVIDES:
    BuildResult[Coord] containing either:
        - On success: Coord in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            row: int,
            column: int,
            validator: CoordValidator = CoordValidator(),
    ) -> BuildResult[Coord]:
        """
        # ACTION:
        1.  Use the validator to certify the row is safe to use.
        2.  Use the validator to certify the column is safe to use.
        3.  If any check fails, return the exception inside a BuildResult.
        4.  When all checks pass return a new Coord instance in a BuildResult.

        # PARAMETERS:
            *   row (int)
            *   column (int)
            *   validator (CoordValidator)

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        # RAISES:
            *   CoordBuildFailedException
        """
        method = "CoordBuilder.builder"
        
        try:
            row_validation = validator.validate_row(row)
            if row_validation.is_failure:
                return BuildResult.failure(row_validation.exception)
                
            column_validation = validator.validate_column(column)
            if column_validation.is_failure:
                return BuildResult.failure(column_validation.exception)
            
            return BuildResult.success(payload=Coord(row=row, column=column))
        
        except Exception as ex:
            return BuildResult.failure(
                CoordBuildFailedException(
                    ex=ex,
                    message=f"{method}: {CoordBuildFailedException.DEFAULT_MESSAGE}"
                )
            )