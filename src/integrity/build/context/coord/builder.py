# src/integrity/build/context/coord/builder.py

"""
Module: integrity.build.context.coord.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional

from logic.coord import (
    CoordContext, CoordContextBuildException, CoordContextBuildRouteException,
    ZeroCoordContextFlagsException
)
from system import (
    BOARD_DIMENSION, BuildResult, Builder, NumberValidator, LoggingLevelRouter
)


class CoordContextBuilder(Builder[CoordContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Token]

     Super Class:
         Builder
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
        Build a CoordContext from the enabled attribute.

        Action:
            1.  Send an exception chain in the BuildResult if either:
                    -   The row
                    -   The column
                fail its validation checks.
            2.  Otherwise, build the CoordContext then, send the success reult.
        Args:
            row: Optional[int]
            column: Optional[int]
            number_validator: NumberValidator
        Returns:
            BuildResult[CoordContext]
        Raises:
            CoordContextBuildException
            ZeroCoordContextFlagsException
        """
        method = f"{cls.__name__}.build"
        
        # --- Count how many optional parameters are not-null. One param needs to be not-null. ---#
        params = [row, column]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                CoordContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=CoordContextBuildException.OP,
                    msg=CoordContextBuildException.MSG,
                    err_code=CoordContextBuildException.ERR_CODE,
                    mthd_rslt=CoordContextBuildException.MTHD_RSLT,
                    ex=ZeroCoordContextFlagsException(
                        msg=CoordContextBuildException.MSG,
                        err_code=CoordContextBuildException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # --- Build the row_column CoordContext if both fields are enabled. ---#
        if row is not None and column is not None:
            # Handle the case that, the rowis not safe.
            validation_result = cls._run_attribute_checks(
                attributes=[row, column],
                number_validator=number_validator,
            )
            # Forward the exception chain if a check fails.
            if validation_result.is_failure:
                return validation_result
            # Otherwise, forward the work product.
            return BuildResult.success(CoordContext(row=row, column=column))
        
        # --- Build the row CoordContext if it's the only field enabled. ---#
        if row is not None:
            # Handle the case that, the rowis not safe.
            validation_result = cls._run_attribute_checks(
                attributes=[row],
                number_validator=number_validator,
            )
            # Forward the exception chain if a check fails.
            if validation_result.is_failure:
                return validation_result
            # Otherwise, forward the work product.
            return BuildResult.success(CoordContext(row=row))
        
        # --- Build the column CoordContext if it's the only field enabled. ---#
        if column is not None:
            # Handle the case that, the rowis not safe.
            validation_result = cls._run_attribute_checks(
                attributes=[column],
                number_validator=number_validator,
            )
            # Forward the exception chain if a check fails.
            if validation_result.is_failure:
                return validation_result
            # Otherwise, forward the work product.
            return BuildResult.success(CoordContext(column=column))
  
        # Handle there is no build route for the attribute.
        return BuildResult.failure(
            CoordContextBuildException(
                cls_mthd=method,
                cls_name=cls.__name__,
                op=CoordContextBuildException.OP,
                msg=CoordContextBuildException.MSG,
                err_code=CoordContextBuildException.ERR_CODE,
                mthd_rslt=CoordContextBuildException.MTHD_RSLT,
                ex=CoordContextBuildRouteException(
                    msg=CoordContextBuildRouteException.MSG,
                    err_code=CoordContextBuildRouteException.ERR_CODE,
                )
            )
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _run_attribute_checks(
            cls,
            attributes: List[int],
            number_validator: NumberValidator,
    ) -> BuildResult[CoordContext]:
        """
        Run checks on which ether attributes have been enabled.
        Action:
            Send an exception in the BuildResult if list member fails a check.
            Otherwise, send the success result.
        Args:
            attributes: List[int]
            number_validator: NumberValidator
        Returns:
            BuildResult[CoordContext]
        Raises:
            CoordContextBuildException
        """
        method = f"{cls.__name__}._run_validation_check"
        
        for attribute in attributes:
            # Handle the case that, the rowis not safe.
            validation_result = number_validator.validate(
                candidate=attribute,
                ceiling=BOARD_DIMENSION - 1,
                floor=0,
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CoordContextBuildException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=CoordContextBuildException.OP,
                        msg=CoordContextBuildException.MSG,
                        err_code=CoordContextBuildException.ERR_CODE,
                        mthd_rslt=CoordContextBuildException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(CoordContext())
        