# src/chess/coord/context/builder/builder.py

"""
Module: chess.coord.context.builder.builder
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.coord.context.builder.exception import CoordContextBuildException, CoordContextBuildRouteException
from chess.system import (
    BOARD_DIMENSION, BuildResult, Builder, NumberValidator, UnhandledRouteException, LoggingLevelRouter,
)
from chess.coord import CoordContext, ZeroCoordContextFlagsException


class CoordContextBuilder(Builder[CoordContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce CoordContext instances whose integrity is guaranteed at creation.
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
            row: Optional[int] = None,
            column: Optional[int] = None,
            number_validator: NumberValidator = NumberValidator(),
    ) -> BuildResult[CoordContext]:
        """
        # ACTION:
            1.  If all the optional params are null send and exception chain in the BuildResult. Else,
                route to the build path which matches the not null attribute.
            2.  If the build params fail their certification checks send an exception in the BuildResult. Otherwise,
                create the CoordContext and send it in the BuildResult.
        # PARAMETERS:
            At least one of these must be provided:
                *   row (Optional[int])
                *   column (Optional[int])
            This parameter is Required:
                *   number_validator (NumberValidator)
        # RETURNS:
            *   BuildResult[CoordContext] containing either:
                    - On failure: Exception.
                    - On success: CoordContext in the payload.
        # RAISES:
            *   ZeroCoordContextFlagsException
            *   CoordContextBuildException
            *   ExcessiveCoordContextFlagsException
        """
        method = "CoordContextBuilder.builder"
        
        # Count how many optional parameters are not-null. One param needs to be not-null.
        params = [row, column]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                CoordContextBuildException(
                    message=f"{method}: {CoordContextBuildException.ERROR_CODE}",
                    ex=ZeroCoordContextFlagsException(f"{method}: {ZeroCoordContextFlagsException.DEFAULT_MESSAGE}")
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the row_column CoordContext if both flags are enabled.
        if row is not None and column is not None:
            # Handle the case that the row is not certified safe.
            row_validation = number_validator.validate(candidate=row, floor=0, ceiling=BOARD_DIMENSION - 1)
            if row_validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CoordContextBuildException(
                        message=f"{method}: {CoordContextBuildException.ERROR_CODE}",
                        ex=row_validation.exception
                    )
                )
            # Handle the case that the column is not certified safe.
            column_validation = number_validator.validate(candidate=column, floor=0, ceiling=BOARD_DIMENSION - 1)
            if column_validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CoordContextBuildException(
                        message=f"{method}: {CoordContextBuildException.ERROR_CODE}",
                        ex=column_validation.exception
                    )
                )
            # On validation success return a row_CoordContext in the BuildResult.
            return BuildResult.success(CoordContext(row=row, column=column))
        
        # Build the row CoordContext if it's the only flag enabled.
        if row is not None:
            validation = number_validator.validate(candidate=row, floor=0, ceiling=BOARD_DIMENSION-1)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CoordContextBuildException(
                        message=f"{method}: {CoordContextBuildException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a row_CoordContext in the BuildResult.
            return BuildResult.success(CoordContext(row=row))
        
        # Build the column CoordContext if it's the only flag enabled.
        if column is not None:
            validation = number_validator.validate(candidate=column, floor=0, ceiling=BOARD_DIMENSION - 1)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CoordContextBuildException(
                        message=f"{method}: {CoordContextBuildException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a column_CoordContext in the BuildResult.
            return BuildResult.success(CoordContext(column=column))
  
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            CoordContextBuildException(
                message=f"{method}: {CoordContextBuildException.ERROR_CODE}",
                ex=CoordContextBuildRouteException(f"{method}: {CoordContextBuildRouteException.DEFAULT_MESSAGE}")
            )
        )