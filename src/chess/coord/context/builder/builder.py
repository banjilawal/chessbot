# src/chess/coord/map/builder/builder.py

"""
Module: ches.coord.map.builder.builder
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.system import (
    BuildResult, Builder, FailsafeBranchExitPointException, LoggingLevelRouter,
    NumberInBoundsValidator
)
from chess.coord import (
    Coord, CoordContextValidator, CoordContext, CoordContextBuildFailedException
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
        *   Builder

    # PROVIDES:
    None

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
            coord: Optional[Coord] = None,
            coord_validator: CoordContextValidator = CoordContextValidator(),
            validator: NumberInBoundsValidator = NumberInBoundsValidator(),
    ) -> BuildResult[CoordContext]:
        """
        # Action:
            1.  Confirm that only one in the (row, column, coord) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a CoordContext and send in a BuildResult. Else, send an exception
                in the BuildResult.

        # Parameters:
            At least one of these must be provided:
                *   row (Optional[int])
                *   coord (Optional[Coord])
                *   column (Optional[int])
                
            This parameter is Required:
                *   coord_validator (CoordContextValidator)
                *   validator (NumberInBoundsValidator)

        # Returns:
          BuildResult[CoordContext] containing either:
                - On success: CoordContext in the payload.
                - On failure: Exception.

        # Raises:
            *   ZeroCoordContextFlagsException
            *   CoordContextBuildFailedException
            *   ExcessiveCoordContextFlagsException
        """
        method = "CoordContextBuilder.builder"
        
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [row, column, Coord]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which Coords match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroCoordFlagsContextException(f"{method}: {ZeroCoordFlagsContextException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveCoordContextFlagsException(f"{method}: {ExcessiveCoordContextFlagsException}")
                )
            # After verifying only one Coord attribute-value-tuple is enabled, validate it.
            
            # Build the row CoordContext if its flag is enabled.
            if row is not None:
                validation = validator.validate(candidate=row)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a row_CoordContext in the BuildResult.
                return BuildResult.success(CoordContext(row=row, column=column))
                
            # Build the column CoordContext if its flag is enabled.
            if column is not None:
                validation = validator.validate(candidate=column)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a column_CoordContext in the BuildResult.
                return BuildResult.success(CoordContext(row=row))
            
            # Build the coord CoordContext if its flag is enabled.
            if coord is not None:
                validation = coord_validator.validate(candidate=coord)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a coord_CoordContext in the BuildResult.
                return BuildResult.success(CoordContext(column=column))
            
            # As a failsafe send a buildResult failure if a map path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        # Finally, if there is an unhandled exception Wrap a CoordContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                CoordContextBuildFailedException(
                    ex=ex,  message=f"{method}: {CoordContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )