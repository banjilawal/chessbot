# src/permitter/maneuver/destination/__init__.py

"""
Module: permitter.maneuver.destination.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import Square, Token
from permitter import TokenPermitter
from report.approval.maneuver import ManeuverApprovalReport
from result import AnalysisResult
from toolkit import TokenManeuverToolkit
from util import LoggingLevelRouter


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
    def execute(
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
        readiness_analysis_result = toolkit.readiness_analyzer.analyze(token)
        if readiness_analysis_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=readiness_analysis_result.exception,
                )
            )
        # Handle the case that, the token is not free.
        report = cast(TokenReadinessReport, readiness_analysis_result.payload)
        if report.token_is_not_ready:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                ManeuverApprovalReport.deny(
                    exception=ManeuverPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ManeuverPermitterException.MSG,
                        err_code=ManeuverPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=DisabledTokenManeuverException(
                            msg=DisabledTokenManeuverException.MSG,
                            err_code=DisabledTokenManeuverException.ERR_CODE,
                        ),
                    )
                )
            )
            
        token_origin_search_result = toolkit.origin_searcher.execute(
            token=requestor,
            readiness_analyzer=toolkit.readiness_analyzer
        )
        # Handle the case that, the origin_searcher is not successful.
        if token_origin_search_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
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
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=destination_relation_analysis.exception,
                )
            )
        # Handle the case that, the token and destination are related in some fashion.
        if destination_relation_analysis.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=destination_relation_analysis.exception,
                )
            )
        for square in [origin, destination]:
            square_validation_result = toolkit.square_validator.validate(square)
            if square_validation_result.is_failure:
                # Return the exception chain on failure
                return AnalysisResult.failure(
                    ManeuverPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ManeuverPermitterException.MSG,
                        err_code=ManeuverPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=square_validation_result.exception,
                    )
                )
        # Handle the case, that the source and destination are the same.
        if origin == destination:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=ItinerarySourceEqualsDestinationException(
                        msg=ItinerarySourceEqualsDestinationException.MSG,
                        err_code=ItinerarySourceEqualsDestinationException.ERR_CODE,
                    ),
                )
            )

        origin_search_result = token.team.board.squares.search(
            context=SquareContext(occupant=token)
        )
        # Handle the case that, the search is not completed.
        if origin_search_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                ManeuverApprovalReport.deny(
                    exception=ManeuverPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ManeuverPermitterException.MSG,
                        err_code=ManeuverPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=DisabledTokenManeuverException(
                            msg=DisabledTokenManeuverException.MSG,
                            err_code=DisabledTokenManeuverException.ERR_CODE,
                        ),
                    )
                )
            )
        # Handle the case that, the token is not on the board.
        if origin_search_result.is_empty:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                ManeuverApprovalReport.deny(
                    exception=ManeuverPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ManeuverPermitterException.MSG,
                        err_code=ManeuverPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=DisabledTokenManeuverException(
                            msg=DisabledTokenManeuverException.MSG,
                            err_code=DisabledTokenManeuverException.ERR_CODE,
                        ),
                    )
                )
            )
        path_validation_result =
        origin_token_relation_result = destination_relation_analyzer.analyze(
            candidate_primary=origin,
            candidate_satellite=token,
        )
        # Handle the case that, the relation_analysis is not completed.
        if origin_token_relation_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=origin_token_relation_result.exception,
                )
            )
        # Handle the case that, the token does not have a bidirectional relation with its source.
        origin_relation = cast(RelationReport, origin_token_relation_result.payload)
        if not origin_relation.fully_exists:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                ManeuverApprovalReport.deny(
                    exception=ManeuverPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ManeuverPermitterException.MSG,
                        err_code=ManeuverPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=BidirectionalSourceTokenRelationException(
                            msg=BidirectionalSourceTokenRelationException.MSG,
                            err_code=BidirectionalSourceTokenRelationException.ERR_CODE,
                        ),
                    )
                )
            )
        destination_token_relation_result = destination_relation_analyzer.analyze(
            candidate_primary=destination,
            candidate_satellite=token,
        )
        # Handle the case that, the relation_analysis is not completed.
        # Return the exception chain on failure
        return AnalysisResult.failure(
            ManeuverPermitterException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=ManeuverPermitterException.MSG,
                err_code=ManeuverPermitterException.ERR_CODE,
                mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                ex=destination_token_relation_result.exception,
            )
        )
        # Handle the case that, the token does have a bidirectional relation with its source.
        destination_token_relation_result = cast(RelationReport, destination_token_relation_result.payload)
        if not destination_relation.does_not_exist:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryConsistencyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryConsistencyException.MSG,
                    err_code=ItineraryConsistencyException.ERR_CODE,
                    ex=BidirectionalSourceTokenRelationException(
                        msg=BidirectionalSourceTokenRelationException.MSG,
                        err_code=BidirectionalSourceTokenRelationException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(itinerary)
        
        id_validation_result = square_validator.validate_id(candidate=id)
        if id_validation_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=id_validation_result.exception,
                )
            )

        
        stack_validation_result = token_freedom_analyzer.build(
            candidate=stack,
            target_model=TokenStackService,
            null_exception=TokenStackNullException()
        )
        if stack_validation_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=stack_validation_result.exception,
                )
            )
        if stack.is_empty:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                DeleteApproval.deny(
                    exception=ManeuverPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ManeuverPermitterException.MSG,
                        err_code=ManeuverPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=PoppingEmptyTokenStackException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=PoppingEmptyTokenStackException.MSG,
                            err_code=PoppingEmptyTokenStackException.ERR_CODE,
                        ),
                    )
                )
            )
        # --- Integrity and performance tests are passed. ---#
        return AnalysisResult.completed(DeleteApproval.approve(id=item_id, stack=stack))

    