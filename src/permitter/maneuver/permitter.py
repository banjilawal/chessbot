# src/deletion/token/py

"""
Module: deletion.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from analyzer import FriendshipAnalyzer, SquareTokenRelationAnalyzer, TokenReadinessAnalyzer
from builder import TokenPathDtoBuilder
from err import (
    BidirectionalSourceTokenRelationException, CircularPathException, DisabledTokenManeuverException,
    ItinerarySourceEqualsDestinationException, PoppingEmptyTokenStackException,
    ManeuverPermitterException,
    TokenStackNullException
)
from microservice import SquareValidator, TokenService
from model import Square, SquareContext, Token, TokenPathDTO
from report import DeleteApproval, FriendshipReport, RelationReport, TokenReadinessReport
from report.approval.maneuver import ManeuverApproval
from result import AnalysisResult, MethodResultType
from search import TokenOriginSearcher
from stack import TokenStackService
from toolkit import TokenPathToolkit
from util import LoggingLevelRouter
from validation import TokenFreedomAnalyzer, TokenValidator
from validation.destination import TokenDestinationRelationValidator


class ManeuverPermitter:
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
            ) -> AnalysisResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            destination: Square,
            friendship_analyzer: FriendshipAnalyzer | None = None,
            token_service: TokenService | None = None,
            path_toolkit: TokenPathToolkit | None = None,
            path_dto_builder: TokenPathDtoBuilder | None = None,
            token_validator: TokenValidator | None = None,
            square_validator: SquareValidator | None = None,
            origin_searcher: TokenOriginSearcher | None = None,
            readiness_analyzer: TokenReadinessAnalyzer | None = None,
            relation_analyzer: SquareTokenRelationAnalyzer | None = None,
            destination_validator: TokenDestinationRelationValidator | None = None,
    ) -> AnalysisResult:
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
            item_id: int
            stack: TokenStackService
            square_validator: SquareValidator
            token_freedom_analyzer: TokenFreedomAnalyzer
        Returns:
            AnalysisResult
        Raises:
            TokenDeletePermitterException
            TokenStackFullException
        """
        method =  f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if token_validator is None:
            token_validator = TokenValidator()
        if path_toolkit is None:
            path_toolkit = TokenPathToolkit()
        if path_dto_builder is None:
            path_dto_builder = TokenPathDtoBuilder()
        if square_validator is None:
            square_validator = SquareValidator()
        if origin_searcher is None:
            origin_searcher = TokenOriginSearcher()
        if readiness_analyzer is None:
            readiness_analyzer = TokenReadinessAnalyzer()
        if relation_analyzer is None:
            relation_analyzer = SquareTokenRelationAnalyzer()
        if destination_validator is None:
            destination_validator = TokenDestinationRelationValidator()
        if friendship_analyzer is None:
            friendship_analyzer = FriendshipAnalyzer()
            
        dto_build_result = path_dto_builder.build(
            token=token,
            destination=destination,
            toolkit=path_toolkit,
        )
        if dto_build_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=dto_build_result.exception,
                )
            )
        dto = cast(TokenPathDTO, dto_build_result.payload)
        
        destination_occupant = dto.destination.occupant
        if destination_occupant is not None:
            friendship_analysis_result = token_service.controller.friendship_analyzer.execute(
                hunter=token,
                target=destination_occupant,
            )
            if friendship_analysis_result.is_failure:
                # Return the exception chain on failure
                return AnalysisResult.failure(
                    ManeuverPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ManeuverPermitterException.MSG,
                        err_code=ManeuverPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=friendship_analysis_result.exception,
                    )
                )
            report = cast(FriendshipReport, friendship_analysis_result.payload[0])
            if report.are_friends:
                return
                
        origin_search_result = origin_searcher.execute(
            token=token,
            readiness_analyzer=readiness_analyzer
        )
        # Handle the case that, the origin_searcher is not successful.
        if origin_search_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=origin_search_result.exception,
                )
            )
        origin = origin_search_result.payload[0]
        
        # Handle the case that, the token is already at the destination.
        token_destination_validation_result = destination_validator.execute(
            token=token,
            destination=destination,
            token_validator=token_validator,
            square_validator=square_validator,
            relation_analyzer=relation_analyzer,
        )
        if token_destination_validation_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=token_destination_validation_result.exception,
                )
            )
        # Handle the case that, the origin and destination are the same.
        if origin == destination:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=CircularPathException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=CircularPathException.MSG,
                        err_code=CircularPathException.ERR_CODE,
                    ),
                )
            )
        destination_relation_analysis = destination_relation_analyzer.analyze(
            candidate_primary=destination,
            candidate_satellite=token,
            token_validator=token_validator,
            square_validator=square_validator,
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
            square_validation_result = square_validator.validate(square)
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
        # Handle the case that, the token fails a validation check.
        freedom_analysis_result = token_freedom_analyzer.analyze(token)
        if freedom_analysis_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=freedom_analysis_result.exception,
                )
            )
        # Handle the case that, the token is not free.
        report = cast(TokenReadinessReport, freedom_analysis_result.payload)
        if report.token_is_not_ready:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                ManeuverApproval.deny(
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
        origin_search_result = token.team.board.squares.search(
            context=SquareContext(occupant=token)
        )
        # Handle the case that, the search is not completed.
        if origin_search_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                ManeuverApproval.deny(
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
                ManeuverApproval.deny(
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
                ManeuverApproval.deny(
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

    