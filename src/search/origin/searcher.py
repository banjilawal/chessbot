# src/search/origin/searcher.py

"""
Module: search.origin/searcher
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from analyzer import SquareTokenRelationAnalyzer, TokenReadinessAnalyzer
from err import (
    BidirectionalSourceTokenRelationException, DisabledTokenManeuverException,
    ItinerarySourceEqualsDestinationException, PoppingEmptyTokenStackException,
    TokenOriginSearcherException,
    TokenStackNullException
)
from microservice import SquareValidator
from model import Square, SquareContext, Token
from report import DeleteApproval, RelationReport, TokenReadinessReport
from report.approval.maneuver import ManeuverApproval
from result import SearchResult, MethodResultType, SearchResult
from stack import TokenStackService
from util import LoggingLevelRouter
from validation import TokenFreedomAnalyzer


class TokenOriginSearcher:
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
                    cls,
                    token: Token,
                    token_stack: TokenStackService,
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
                    collision_detector: TokenCollisionAnalyst = TokenCollisionAnalyst(),
            ) -> SearchResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            readiness_analyzer: TokenReadinessAnalyzer | None = None,
    ) -> SearchResult:
        """
        Find the square a Token occupies on a Board.
        
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
            item_id: int
            stack: TokenStackService
            square_validator: SquareValidator
            readiness_analyzer: TokenFreedomAnalyzer
        Returns:
            SearchResult
        Raises:
            TokenDeletePermitterException
            TokenStackFullException
        """
        method =  f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if readiness_analyzer is None:
            readiness_analyzer = TokenReadinessAnalyzer()

        # Handle the case that, the token fails a validation check.
        readiness_analysis_result = readiness_analyzer.analyze(token)
        # Handle the case that, the freedom
        if readiness_analysis_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                exception=TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=readiness_analysis_result.exception,
                )
            )
        # Handle the case that, the token is not ready for use.
        report = cast(TokenReadinessReport, readiness_analysis_result.payload)
        if report.token_is_not_ready:
            # Return the exception chain on failure
            return SearchResult.failure(
                exception=TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=readiness_analysis_result.exception,
                )
            )
            return SearchResult.completed(
                ManeuverApproval.deny(
                    exception=TokenOriginSearcherException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenOriginSearcherException.MSG,
                        err_code=TokenOriginSearcherException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=DisabledTokenManeuverException(
                            msg=DisabledTokenManeuverException.MSG,
                            err_code=DisabledTokenManeuverException.ERR_CODE,
                        ),
                    )
                )
            )
        origin_search_result = token.team.board.squares.search(
            context=SquareContext(occupant=token)
        )
        # Handle the case that, the search is not completed.
        if origin_search_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.completed(
                ManeuverApproval.deny(
                    exception=TokenOriginSearcherException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenOriginSearcherException.MSG,
                        err_code=TokenOriginSearcherException.ERR_CODE,
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
            return SearchResult.completed(
                ManeuverApproval.deny(
                    exception=TokenOriginSearcherException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenOriginSearcherException.MSG,
                        err_code=TokenOriginSearcherException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=DisabledTokenManeuverException(
                            msg=DisabledTokenManeuverException.MSG,
                            err_code=DisabledTokenManeuverException.ERR_CODE,
                        ),
                    )
                )
            )
        path_validation_result =
        origin_token_relation_result = square_token_relation_analyzer.analyze(
            candidate_primary=origin,
            candidate_satellite=token,
        )
        # Handle the case that, the relation_analysis is not completed.
        if origin_token_relation_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=origin_token_relation_result.exception,
                )
            )
        # Handle the case that, the token does not have a bidirectional relation with its source.
        origin_relation = cast(RelationReport, origin_token_relation_result.payload)
        if not origin_relation.fully_exists:
            # Return the exception chain on failure
            return SearchResult.completed(
                ManeuverApproval.deny(
                    exception=TokenOriginSearcherException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenOriginSearcherException.MSG,
                        err_code=TokenOriginSearcherException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=BidirectionalSourceTokenRelationException(
                            msg=BidirectionalSourceTokenRelationException.MSG,
                            err_code=BidirectionalSourceTokenRelationException.ERR_CODE,
                        ),
                    )
                )
            )
        destination_token_relation_result = square_token_relation_analyzer.analyze(
            candidate_primary=destination,
            candidate_satellite=token,
        )
        # Handle the case that, the relation_analysis is not completed.
        # Return the exception chain on failure
        return SearchResult.failure(
            TokenOriginSearcherException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=TokenOriginSearcherException.MSG,
                err_code=TokenOriginSearcherException.ERR_CODE,
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
            return SearchResult.failure(
                TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=id_validation_result.exception,
                )
            )

        
        stack_validation_result = readiness_analyzer.execute(
            candidate=stack,
            target_model=TokenStackService,
            null_exception=TokenStackNullException()
        )
        if stack_validation_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=stack_validation_result.exception,
                )
            )
        if stack.is_empty:
            # Return the exception chain on failure
            return SearchResult.completed(
                DeleteApproval.deny(
                    exception=TokenOriginSearcherException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenOriginSearcherException.MSG,
                        err_code=TokenOriginSearcherException.ERR_CODE,
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
        return SearchResult.completed(DeleteApproval.approve(id=item_id, stack=stack))

    