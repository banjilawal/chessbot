# src/permitter/maneuver/destination/__init__.py

"""
Module: permitter.maneuver.destination.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import TokenManeuverPermitterException
from model import Maneuver, Path, Square, Token
from permitter import TokenPermitter
from report import ManeuverApprovalReport
from result import AnalysisResult, MethodResultType
from toolkit import TokenManeuverToolkit
from util import IdFactory, LoggingLevelRouter


class TokenManeuverPermitter(TokenPermitter):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a deletion.

    Attributes:

    Provides:
        -   execute(
                    requestor: Token,
                    destination: Square,
                    toolkit: TokenManeuverToolkit,
            ) -> AnalysisResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def run(
            cls,
            requestor: Token,
            destination: Square,
            toolkit: TokenManeuverToolkit | None = None,
    ) -> AnalysisResult[ManeuverApprovalReport]:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The collision_detector
                    -   The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a deletion denial if
                    -   The TokenStack is full.
                    -   The item collides with an existing stack member.
                    -   The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            requestor: Token
            destination: Square
            toolkit: TokenManeuverToolkit
        Returns:
            AnalysisResult
        Raises:
            TokenDeletePermitterException
            TokenStackFullException
        """
        method =  f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenManeuverToolkit()
        
        # Handle the case that, the token fails a validation check.
        readiness_analysis_result = toolkit.readiness_analyzer.analyze(subject=requestor)
        if readiness_analysis_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                TokenManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenManeuverPermitterException.MSG,
                    err_code=TokenManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=readiness_analysis_result.exception,
                )
            )
        token_origin_search_result = toolkit.origin_searcher.execute(target=requestor)
        # Handle the case that, the origin_searcher is not successful.
        if token_origin_search_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                TokenManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenManeuverPermitterException.MSG,
                    err_code=TokenManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=token_origin_search_result.exception,
                )
            )
        origin = token_origin_search_result.payload[0]
        
        destination_relation_analysis = toolkit.destination_relation_analyzer.analyze(
            candidate_primary=destination,
            candidate_satellite=requestor,
            token_validator=toolkit.token_validator,
            square_validator=toolkit.square_validator,
        )

        # Handle the case that, the destination_relation_analyzer aborts.
        if destination_relation_analysis.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                TokenManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenManeuverPermitterException.MSG,
                    err_code=TokenManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=destination_relation_analysis.exception,
                )
            )
        # Handle the case that, the token and destination are related in some fashion.
        if destination_relation_analysis.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                TokenManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenManeuverPermitterException.MSG,
                    err_code=TokenManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=destination_relation_analysis.exception,
                )
            )
        for square in [origin, destination]:
            square_validation_result = toolkit.square_validator.validate(square)
            if square_validation_result.is_failure:
                # Return the exception chain on failure
                return AnalysisResult.failure(
                    TokenManeuverPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenManeuverPermitterException.MSG,
                        err_code=TokenManeuverPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=square_validation_result.exception,
                    )
                )
        
        return AnalysisResult.completed(
            ManeuverApprovalReport.approve(
                Maneuver(
                    token=requestor,
                    path=Path(
                        origin=origin,
                        destination=destination,
                        id=IdFactory.next_id(class_name="Path")
                    ),
                    id=IdFactory.next_id(class_name="Maneuver")
                )
            )
        )

    