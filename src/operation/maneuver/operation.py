# src/operation/maneuver/operation.py

"""
Module: operation.maneuver.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from bootstrapper import PrimingValidator
from err import ManeuverException
from err.null.event import ManeuverEventNullException
from report import ManeuverApproval, ManeuverApprovalReport
from result import TurnResult
from util import LoggingLevelRouter


class ManeuverLauncher:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Square entry exception owner.
        2.  Preserve original and updated square data for rollbacks.
        3.  Ensure both the token and the squares are consistent throughout
            square entry lifecycle.

    Attributes:
    
    Provides:
        -   execute(
                    token: Token,
                    square: Square,
                    token_freedom_analyzer: TokenFreedomAnalyzer,
                    priming_validator: PrimingValidator,
            ) -> ManeuverResult:

    Super Class:
    """
    _priming_validator: PrimingValidator
    
    
    @LoggingLevelRouter.monitor
    def execute(self, report: ManeuverApprovalReport,) -> TurnResult:
        """
        Action:
            1.  Send the original square along with an exception chain in the validation result if:
                    -   The square or token are insecure.
                    -   The token is disabled
                    -   The token belongs to a different board.
                    -   The new token is being deployed to the wrong square.
                    -   The square is already occupied.
                    -   The square accepts the token but the token cannot update its position.
            2.  Otherwise, each updates its state.
            3.  Send the success result.
        Args:
            report: ManeuverItineraryApproval
            priming_validator: PrimingValidator
       Returns:
            ManeuverResult
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        

        # Handle the case that, the itinerary is not valid.
        priming = self._priming_validator.execute(
            candidate=report,
            target_type=ManeuverApproval,
            null_ex_cls=ManeuverEventNullException,
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return TurnResult.failure(
                ManeuverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverException.MSG,
                    err_code=ManeuverException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.EVENT_RESULT,
                    ex=priming.exception,
                )
            )
        report = cast(ManeuverApprovalReport, priming.payload)
        # Handle the case that, the destination is not empty.
        if report.is_denied:
            # Send the exception chain on failure.
            return TurnResult.failure(
                ManeuverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverException.MSG,
                    err_code=ManeuverException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.EVENT_RESULT,
                    ex=report.exception,
                )
            )
        
        maneuver = report.maneuver

        token = report.maneuver.token
        maneuver.path.endpoints.destination.occupant = token
        maneuver.path.endpoints.destination.state = SquareState.OCCUPIED
        
        maneuver.path.endpoints.origin.occupant = None
        maneuver.path.endpoints.origin.state = SquareState.EMPTY
        
        maneuver.state = ManeuverState.COMPLETED
        
        # --- Forward the work product to the caller. ---#
        return TurnResult.success(maneuver)
