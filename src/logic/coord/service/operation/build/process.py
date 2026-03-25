# src/logic/coord/service/operation/build/exception.py

"""
Module: logic.coord.service.operation.build.build
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import Coord, CoordBuildException
from logic.system import BOARD_DIMENSION, BuildProcess, BuildResult, LoggingLevelRouter, NumberValidationProcess


class CoordBuildProcess(BuildProcess[Coord]):
    """
     Role:
        -   Worker,
        -   Integrity Management
     
     Responsibilities:
         1.  Produce Coord instances whose integrity is guaranteed at creation.
         2.  Ensure params for Coord creation have met the application's safety contract.
         3.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     Attributes:
     
    Provides:
        -   execute(
                    row: int,
                    column: int,
                    number_validator: NumberValidationProcess,
            ) -> BuildResult[Coord]

     Super Class:
         BuildProcess
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            row: int,
            column: int,
            number_validator: NumberValidationProcess = NumberValidationProcess(),
    ) -> BuildResult[Coord]:
        """
        Build a Coord.
        
        Action:
            1.  Send an exception chain in the BuildResult if either:
                    -   The row
                    -   The column
                are fail its validation checks.
            2.  Otherwise, build the Coord then, send the success reult.
        Args:
            row: int
            column: int
            number_validator: NumberValidationProcess)
        Returns:
            BuildResult[Coord]
        Raises:
            CoordBuildException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, the row is not certified safe
        row_validation_result = number_validator.execute(
            candidate=row,
            floor=0,
            ceiling=BOARD_DIMENSION - 1
        )
        if row_validation_result.is_failure:
            # Return the validation chain on failure.
            return BuildResult.failure(
                CoordBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordBuildException.OP,
                    msg=CoordBuildException.MSG,
                    err_code=CoordBuildException.ERR_CODE,
                    rslt_type=CoordBuildException.RSLT_TYPE,
                    ex=row_validation_result.exception,
                )
            )
        # Handle the case that, the column is not certified safe
        column_validation_result = number_validator.execute(
            candidate=column,
            floor=0,
            ceiling=BOARD_DIMENSION - 1
        )
        if column_validation_result.is_failure:
            # Return the validation chain on failure.
            return BuildResult.failure(
                CoordBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordBuildException.OP,
                    msg=CoordBuildException.MSG,
                    err_code=CoordBuildException.ERR_CODE,
                    rslt_type=CoordBuildException.RSLT_TYPE,
                    ex=column_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            Coord(row=row, column=column)
        )
