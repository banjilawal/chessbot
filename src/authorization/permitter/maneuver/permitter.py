# src/authorization/permitter/maneuver/destination/__init__.py

"""
Module: authorization.permitter.maneuver.destination.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from err import ManeuverPermitterException

from report import ManeuverRequestDecision
from request import ManeuverRequest
from result import MethodResultType
from authorization.adjudicator import ManeuverRequestAdjudicator
from util import LoggingLevelRouter


class TokenManeuverPermitter:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests before a token can be authorized to move.

    Attributes:
         adjudicator: Optional[ManeuverRequestAdjudicator]

    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverApprovalReport

    Super Class:
        Permitter
    """
    _adjudicator: Optional[ManeuverRequestAdjudicator]
    
    def __init__(self, adjudicator: Optional[ManeuverRequestAdjudicator] |  None = None):
        """
        Args:
             adjudicator: Optional[ManeuverRequestAdjudicator]
        """
        self._adjudicator = adjudicator or ManeuverRequestAdjudicator()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverRequestDecision:
        """
        Action:
            1.  Send an exception chain in the ApprovalReport if the adjudicator denies the
                request.
            2.  Otherwise, forward the adjudicator's approval.
        Args:
            request: ManeuverRequest
        Returns:
            ManeuverApprovalReport
        Raises:
            ManeuverPermitterException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handoff the request to the adjudicator for processing.
        approval = self._adjudicator.execute(cadidate=request)
        
        # Handle the case that the request is denied.
        if approval.request_is_denied:
            # Return the exception chain on failure
            return ManeuverRequestDecision.deny(
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