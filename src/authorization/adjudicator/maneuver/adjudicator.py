# src/authorization/adjudicator/maneuver/adjudicator.py

"""
Module: authorization.adjudicator.maneuver.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from authorization import RequestAdjudicator
from err import (
    CircularPathException, ManeuverRequestNullException,
    ManeuverRequestAdjudicatorException
)
from model import Maneuver, Path, Square
from register import SquareRegister
from report import ManeuverRequestDecision
from request import ManeuverRequest
from result import MethodResultType
from toolkit import TokenManeuverToolkit
from util import IdFactory, LoggingLevelRouter


class ManeuverRequestAdjudicator(RequestAdjudicator[ManeuverRequest]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a deletion.

    Attributes:
        toolkit: Optional[TokenManeuverToolkit]
    Provides:
        -   def execute(self, candidate: Any) -> ManeuverApprovalReport:

    Super Class:
        Adjudicator
    """
    _toolkit: Optional[TokenManeuverToolkit]
    
    def __init__(self, toolkit: Optional[TokenManeuverToolkit] | None = None):
        """
        Args:
            toolkit: Optional[TokenManeuverToolkit]
        """
        super().__init__()
        self._toolkit = toolkit or TokenManeuverToolkit()
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ManeuverRequestDecision:
        """
        Action:
            1.  Return a denial report containing an exception chain if any of the following occur:
                    -   The candidate is null
                    -   The candidate is not a ManeuverRequest
                    -   The token in the request is not actionable.
                    -   Searching the token's square fails.
                    -   The destination is not approved.
                    -   The destination and the origin are the same.
            2.  Otherwise, send an approval report.
        Args:
            candidate: Any
        Returns:
            ManeuverApprovalReport
        Raises:
            ManeuverRequestAdjudicatorException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handle the case that the, the candidate is either null or the wrong type.
        bootstrap = self.priming_validator.execute(
            candidate=candidate,
            target_mode=[ManeuverRequest],
            null_exception=ManeuverRequestNullException(),
        )
        if bootstrap.is_failure:
            # Return the exception chain on failure
            return ManeuverRequestDecision.deny(
                ManeuverRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverRequestAdjudicatorException.MSG,
                    err_code=ManeuverRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=bootstrap.exception,
                )
            )
        request = cast(ManeuverRequest,bootstrap.payload)
        
        # Handle the case that, the token fails a validation check.
        readiness_analysis = self._toolkit.readiness_analyzer.execute(
            subject=request.token
        )
        if readiness_analysis.is_failure:
            # Return the exception chain on failure
            return ManeuverRequestDecision.deny(
                ManeuverRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverRequestAdjudicatorException.MSG,
                    err_code=ManeuverRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=readiness_analysis.exception,
                )
            )
        token_origin_search = self._toolkit.origin_searcher.execute(
            target=request.token
        )
        # Handle the case that, the origin_searcher is not successful.
        if token_origin_search.is_failure:
            # Return the exception chain on failure
            return ManeuverRequestDecision.deny(
                ManeuverRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverRequestAdjudicatorException.MSG,
                    err_code=ManeuverRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=token_origin_search.exception,
                )
            )
        origin = cast(Square, token_origin_search.payload[0])
        
        destination_certification = self._toolkit.destination_certifier.execute(
            candidate_primary=request.destination,
            candidate_satellite=request.token,
            token_validator=self._toolkit.token_validator,
            square_validator=self._toolkit.square_validator,
        )
        # Handle the case that, the destination is not valid.
        if destination_certification.is_denied:
            # Return the exception chain on failure
            return ManeuverRequestDecision.deny(
                ManeuverRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverRequestAdjudicatorException.MSG,
                    err_code=ManeuverRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=destination_certification.exception,
                )
            )
        # Handle the case that, the origin and destination are the same.
        if origin == request.destination:
            # Return the exception chain on failure
            return ManeuverRequestDecision.deny(
                ManeuverRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverRequestAdjudicatorException.MSG,
                    err_code=ManeuverRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=CircularPathException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CircularPathException.MSG,
                        err_code=CircularPathException.ERR_CODE,
                    ),
                )
            )
        path = Path(
            id=IdFactory.next_id(class_name="Path"),
            endpoints=SquareRegister(origin=origin, destination=request.destination,)
        )
        # --- Forward the work product to the caller. ---#
        return ManeuverRequestDecision.grant(
            Maneuver(
                path=path,
                token=request.token,
                id=IdFactory.next_id(class_name="Maneuver"),
            )
        )

    