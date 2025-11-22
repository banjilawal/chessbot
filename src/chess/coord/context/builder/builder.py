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
    Coord, CoordSearchContextValidator, CoordValidator, CoordSearchContext, CoordSearchContextBuildFailedException,
    NoCoordSearchOptionSelectedException, MoreThanOneCoordSearchOptionPickedException,
)


class CoordSearchContextBuilder(Builder[CoordSearchContext]):
    """
    # ROLE: Builder

    # RESPONSIBILITIES:
        1. Manage conintuction of CoordSearchService instances that can be used safely by the client.
        2. Ensure params for CoordSearchService creation have met the application's safety contract.
        3. Provide pluggable factories for creating different CoordSearchContext products.


    # PROVIDES:
      ValidationResult[CoordSearchContext] containing either:
            - On success: CoordSearchContext in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            row: Optional[int],
            column: Optional[int],
            validator: CoordSearchContextValidator = CoordSearchContextValidator()
    ) -> BuildResult[CoordSearchContext]:
        """
        # Action:
            1. Use dependency injected validators to verify correctness of parameters required to
                builder a CoordSearchContext instance.
            2. If the parameters are safe the CoordSearchContext is built and returned.

        # Parameters:
            * row (Optional[int]): selected if search square is an id.
            * column (Optional[int]): selected if search square is a column.
            * square (Optional[Coord]): selected if search square is a square.
            * validator (type[CoordValidator]): validates an id-search-square

        # Returns:
          BuildResult[CoordSearchContext] containing either:
                - On success: CoordSearchContext in the payload.
                - On failure: Exception.

        # Raises:
            * CoordSearchContextBuildFailedException
            * NoCoordSearchOptionSelectedException
            * MoreThanOneCoordSearchOptionPickedException
        """
        method = "CoordSearchContextBuilder.builder"
        
        try:
            params = [row, column]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoCoordSearchOptionSelectedException(
                        f"{method}: "
                        f"{NoCoordSearchOptionSelectedException.DEFAULT_MESSAGE}"
                    )
                )
            
            if row is not None and column is not None:
                validation = validator.validate_both(
                    row_candidate=row,
                    column_candidate=column
                )
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                else:
                    return BuildResult.success(
                        payload=CoordSearchContext(
                            row=row,
                            column=column
                        )
                    )
            
            if row is not None:
                validation = validator.validate_row_context(row=row)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                else:
                    return BuildResult.success(
                        payload=CoordSearchContext(row=row)
                    )
                
            if column is not None:
                validation = validator.validate_column_context(column=column)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                else:
                    return BuildResult.success(
                        payload=CoordSearchContext(column=column)
                    )
        
        except Exception as ex:
            return BuildResult.failure(
                CoordSearchContextBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordSearchContextBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )