# src/logic/zone/service/operation/build/transaction.py

"""
Module: logic.zone.service.operation.build.transaction
Author: Banji Lawal
Created: 2025-08-24
version: 1.0.0
"""

from __future__ import annotations

from logic.zone import Zone, ZoneBuildException
from logic.system import BOARD_DIMENSION, Builder, BuildResult, LoggingLevelRouter, NumberValidationTransaction


class ZoneBuilder(Builder[Zone]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Zone creation process owner.
        2.  Ensure Zone build resources meet satisfy contracts.
        3.  Assure Zone instances comply with business logc at point of creation.s.

     Attributes:
     
    Provides:
        -   execute(
                    row: int,
                    column: int,
                    number_validation: NumberValidationTransaction,
            ) -> BuildResult[Zone]

     Super Class:
         Builder
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            row: int,
            column: int,
            number_validator: NumberValidationTransaction = NumberValidationTransaction(),
    ) -> BuildResult[Zone]:
        """
        Build a Zone.
        
        Action:
            1.  Send an exception chain in the BuildResult if either:
                    -   The row
                    -   The column
                are fail its validation checks.
            2.  Otherwise, build the Zone then, send the success reult.
        Args:
            row: int
            column: int
            number_validator: NumberValidationTransaction)
        Returns:
            BuildResult[Zone]
        Raises:
            ZoneBuildException
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
                    ZoneBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=ZoneBuildException.OP,
                        msg=ZoneBuildException.MSG,
                        err_code=ZoneBuildException.ERR_CODE,
                        rslt_type=ZoneBuildException.RSLT_TYPE,
                        ex=validation_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(Zone(row=row, column=column))
