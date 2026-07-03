# src/builder/coord/builder.py

"""
Module: builder.coord.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from logic.coord import Coord, CoordBuilderException
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
            CoordBuilderException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, either the row or column is not certofoed as safe.
        for param in [row, column]:
            validation_result = number_validator.build(
                ceiling=COORD_DIMENSION - 1,
                candidate=param,
                floor=0,
            )
            if validation_result.is_failure:
                # Return the validation chain on failure.
                return BuildResult.failure(
                    CoordBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=CoordBuilderException.OP,
                        msg=CoordBuilderException.MSG,
                        err_code=CoordBuilderException.ERR_CODE,
                        mthd_rslt_type=CoordBuilderException.MTHD_RSLT,
                        ex=validation_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(Coord(row=row, column=column))
