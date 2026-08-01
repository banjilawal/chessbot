# src/permitter/maneuver/destination/__init__.py

"""
Module: permitter.maneuver.destination.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from err import ManeuverPermitterException

from report import ManeuverApprovalReport
from request import ManeuverRequest
from result import MethodResultType
from core.adjudcator import ManeuverRequestTester
from util import LoggingLevelRouter


class TokenManeuverPermitter:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a deletion.

    Attributes:
         tester: Optional[ManeuverRequestTester]

    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverApprovalReport

    Super Class:
    """
    _tester: Optional[ManeuverRequestTester]
    
    def __init__(self, tester: Optional[ManeuverRequestTester] |  None = None):
        """
        Args:
             tester: Optional[ManeuverRequestTester]
        """
        self._tester = tester or ManeuverRequestTester()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverApprovalReport:
        """
        Action:
            1.  Send an exception chain in the ApprovalReport if the tester denies the
                request.
            2.  Otherwise, forward the tester's approval.
        Args:
            request: ManeuverRequest
        Returns:
            ManeuverApprovalReport
        Raises:
            ManeuverPermitterException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handoff the request to the tester for processing.
        approval = self._tester.execute(cadidate=request)
        
        # Handle the case that the request is denied.
        if approval.is_denied:
            # Return the exception chain on failure
            return ManeuverApprovalReport.deny(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=approval.exception,
                )
            )
        # --- Forward the work product. ---#
        return approval