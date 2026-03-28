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


class CoordBuilder(BuildProcess[Coord]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Coord creation process owner.
        2.  Ensure Coord build resources meet satisfy contracts.
        3.  Assure Coord instances comply with business logc at point of creation.s.

     Attributes:
     
    Provides:
        -   execute(
                    row: int,
                    column: int,
                    number_validation: NumberValidationProcess,
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
        
        # Handle the case that, either the row or column is not certofoed as safe.
        for param in [row, column]:
            validation_result = number_validator.execute(
                ceiling=BOARD_DIMENSION - 1,
                candidate=param,
                floor=0,
            )
            if validation_result.is_failure:
                # Return the validation chain on failure.
                return BuildResult.failure(
                    CoordBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=CoordBuildException.OP,
                        msg=CoordBuildException.MSG,
                        err_code=CoordBuildException.ERR_CODE,
                        rslt_type=CoordBuildException.RSLT_TYPE,
                        ex=validation_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(Coord(row=row, column=column))
