# src/toolkit/context/coord/toolkit.py

"""
Module: toolkit.context.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional

from logic.coord import (
    CoordContext, CoordContextToolkitException, CoordContextToolkitRouteException,
    ZeroCoordContextFlagsException
)
from system import (
    BOARD_DIMENSION, ToolkitResult, Toolkit, NumberValidator, LoggingLevelRouter
)


class CoordContextToolkit(Toolkit[CoordContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Toolkit Process Owner

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
            ) -> ToolkitResult[Token]

     Super Class:
         Toolkit
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            row: Optional[int] = None,
            column: Optional[int] = None,
            number_validator: NumberValidator = NumberValidator(),
    ) -> ToolkitResult[CoordContext]:
        """
        Toolkit a CoordContext from the enabled attribute.

        Action:
            1.  Send an exception chain in the ToolkitResult if either:
                    -   The row
                    -   The column
                fail its validation checks.
            2.  Otherwise, toolkit the CoordContext then, send the success reult.
        Args:
            row: Optional[int]
            column: Optional[int]
            number_validator: NumberValidator
        Returns:
            ToolkitResult[CoordContext]
        Raises:
            CoordContextToolkitException
            ZeroCoordContextFlagsException
        """
        method = f"{cls.__name__}.toolkit"
        
        # --- Count how many optional parameters are not-null. One param needs to be not-null. ---#
        params = [row, column]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return ToolkitResult.failure(
                CoordContextToolkitException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=CoordContextToolkitException.OP,
                    msg=CoordContextToolkitException.MSG,
                    err_code=CoordContextToolkitException.ERR_CODE,
                    rslt_type=CoordContextToolkitException.RSLT_TYPE,
                    ex=ZeroCoordContextFlagsException(
                        msg=CoordContextToolkitException.MSG,
                        err_code=CoordContextToolkitException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate validation/toolkit branch. ---#
        
        # --- Toolkit the row_column CoordContext if both fields are enabled. ---#
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
            return ToolkitResult.success(CoordContext(row=row, column=column))
        
        # --- Toolkit the row CoordContext if it's the only field enabled. ---#
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
            return ToolkitResult.success(CoordContext(row=row))
        
        # --- Toolkit the column CoordContext if it's the only field enabled. ---#
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
            return ToolkitResult.success(CoordContext(column=column))
  
        # Handle there is no toolkit route for the attribute.
        return ToolkitResult.failure(
            CoordContextToolkitException(
                cls_mthd=method,
                cls_name=method.__name__,
                op=CoordContextToolkitException.OP,
                msg=CoordContextToolkitException.MSG,
                err_code=CoordContextToolkitException.ERR_CODE,
                rslt_type=CoordContextToolkitException.RSLT_TYPE,
                ex=CoordContextToolkitRouteException(
                    msg=CoordContextToolkitRouteException.MSG,
                    err_code=CoordContextToolkitRouteException.ERR_CODE,
                )
            )
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _run_attribute_checks(
            self,
            attributes: List[int],
            number_validator: NumberValidator,
    ) -> ToolkitResult[CoordContext]:
        """
        Run checks on which ether attributes have been enabled.
        Action:
            Send an exception in the ToolkitResult if list member fails a check.
            Otherwise, send the success result.
        Args:
            attributes: List[int]
            number_validator: NumberValidator
        Returns:
            ToolkitResult[CoordContext]
        Raises:
            CoordContextToolkitException
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
                return ToolkitResult.failure(
                    CoordContextToolkitException(
                        cls_mthd=method,
                        cls_name=method.__name__,
                        op=CoordContextToolkitException.OP,
                        msg=CoordContextToolkitException.MSG,
                        err_code=CoordContextToolkitException.ERR_CODE,
                        rslt_type=CoordContextToolkitException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ToolkitResult.success(CoordContext())
        