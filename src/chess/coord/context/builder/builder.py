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
    Coord, CoordContextValidator, CoordContext, CoordContextBuildFailedException, NoCoordContextFlagSetException
)


class CoordContextBuilder(Builder[CoordContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce CoordContext instances whose integrity is always guaranteed.
     2.  Manage construction of CoordContext instances that can be used safely by the client.
     3.  Ensure params for CoordContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
         *   CoordContextBuilder

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
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
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [row, column, Coord]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which Coords match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroCoordFlagsException(f"{method}: {ZeroCoordFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveCoordContextFlagsException(f"{method}: {ExcessiveCoordContextFlagsException}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveAgentContextFlagsException(f"{method}: {ExcessiveAgentContextFlagsException}")
                )
            # After verifying only one Coord attribute-value-tuple is enabled, validate it.
            
            # Build the row AgentContext if its flag is enabled.
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