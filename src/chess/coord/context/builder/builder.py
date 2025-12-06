# src/chess/coord/context/builder/builder.py

"""
Module: ches.coord.context.builder.builder
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.system import BuildResult, Builder, LoggingLevelRouter
from chess.coord import (
    CoordContextValidator, CoordContext, CoordContextBuildFailedException, NoCoordContextFlagSetException
)


class CoordContextBuilder(Builder[CoordContext]):
    """
    # ROLE: Builder

    # RESPONSIBILITIES:
        1. Produce only CoordContext instances that are safe and reliable.
        2. Ensure params for CoordContext have correctness.

    # PROVIDES:
      BuildResult[CoordContext] containing either:
            - On success: CoordContext in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            row: Optional[int],
            column: Optional[int],
            validator: CoordContextValidator = CoordContextValidator()
    ) -> BuildResult[CoordContext]:
        """
        # Action:
            1. Use validator to certify either row or column are safe.
            2. If any validations fail return the exception in a BuildResult.
            3. If all checks pass build the CoordContext in a BuildResult.

        # Parameters:
        At least one of these must be provided:
            *   row (Optional[int])
            *   column (Optional[int])
            
        This parameter is Required:
            *   validator (CoordContextValidator)

        # Returns:
          BuildResult[CoordContext] containing either:
                - On success: CoordContext in the payload.
                - On failure: Exception.

        # Raises:
            *   CoordContextBuildFailedException
            *   NoCoordContextFlagSetException
        """
        method = "CoordContextBuilder.builder"
        
        try:
            params = [row, column]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoCoordContextFlagSetException(
                        f"{method}: "
                        f"{NoCoordContextFlagSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if row is not None and column is not None:
                validation = validator.validate_both(
                    row_candidate=row,
                    column_candidate=column
                )
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(CoordContext(row=row, column=column))
            
            if row is not None:
                validation = validator.validate_row_context(row=row)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(CoordContext(row=row))
                
            if column is not None:
                validation = validator.validate_column_context(column=column)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(CoordContext(column=column))
        
        except Exception as ex:
            return BuildResult.failure(
                CoordContextBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordContextBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )