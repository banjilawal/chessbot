# src/integrity/build/coord/builder.py

"""
Module: integrity.build.coord.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from logic.coord import Coord, CoordBuildException
from system import COORD_DIMENSION, Builder, BuildResult, LoggingLevelRouter, NumberValidator


class CoordBuilder(Builder[Coord]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner
        
   Responsibilities:
        1.  Ensure a new Coord instance is born safe and reliable.

    Attributes:
     
    Provides:
        -   def(
                    row: int,
                    column: int,
                    number_validation: NumberValidator,
            ) -> BuildResult[Coord]

     Super Class:
         Builder
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            row: int,
            column: int,
            number_validator: NumberValidator = NumberValidator(),
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
            number_validator: NumberValidator)
        Returns:
            BuildResult[Coord]
        Raises:
            CoordBuildException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, either the row or column is not certofoed as safe.
        for param in [row, column]:
            validation_result = number_validator.validate(
                ceiling=COORD_DIMENSION - 1,
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
