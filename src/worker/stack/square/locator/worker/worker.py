# src/logic/square/database/kernel/operation/exception.py

"""
Module: logic.square.database.kernel.operation.executeer
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.square.database.kernel.operation.execute import ExecutementSquareDiscoveryException

from logic.square.database.kernel.operation.formation.discovery.exception.work import OpeningSquareDiscoveryException
from system import InsertionResult, LoggingLevelRouter, SearchResult, ValidationResult
from logic.square import (
    SquareContext, SquareStackCapacityFullException, Square, SquareStackExecuteException, SquareStackService, SquareStackState
)
from model.token import Token, TokenService


class OpeningSquareLocator(Worker):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Find a token's opening square.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    square: Square,
                    square_stack: SquareStackService,
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: SquareStackCapacityAnalysis = SquareStackCapacityAnalysis(),
                    collision_detector: SquareCollisionAnalyst = SquareCollisionAnalyst(),
            ) -> InsertionResult

    Super:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            square_stack: SquareStackService,
            token_service: TokenService = TokenService(),
    ) -> SearchResult[Square]:
        """
        Action:
            1.  Return a failure result containing an exception chain if
                    *   The square is not safe.
                    *   One of its properties already in use.
                    *   The SquareStackService cannot support another square.
            2.  If none of the failure conditions are met insert the square and send the success result.
        Args:
            token: Token,
            square_stack: SquareStackService
            token_service: TokenService = TokenService()
        Returns:
            UpdateResult[Square]
        Raises:
            ExecutementSquareDiscoveryException
            SquareStackFullException
        """
        method =  f"{cls.__name__}.execute"
        
        # Handle the case that, the token does not pass a validation check.
        token_validation_result = token_service.validator.search_service(token)
        if token_validation_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                OpeningSquareDiscoveryException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=OpeningSquareDiscoveryException.OP,
                    msg=OpeningSquareDiscoveryException.MSG,
                    err_code=OpeningSquareDiscoveryException.ERR_CODE,
                    mthd_rslt_type=OpeningSquareDiscoveryException.MTHD_RSLT,
                    ex=token_validation_result.exception)
            )
        # Handle the case that, the token has been deployed.
        if token.is_deployed:
            OpeningSquareDiscoveryException(
                cls_mthd=method,
                cls_name=cls.__name__,
                op=OpeningSquareDiscoveryException.OP,
                msg=OpeningSquareDiscoveryException.MSG,
                err_code=OpeningSquareDiscoveryException.ERR_CODE,
                mthd_rslt_type=OpeningSquareDiscoveryException.MTHD_RSLT,
                ex=token_validation_result.exception
            )
        )

        # ServiceRequest a collision report. The square is verified during the report generation. ---#
        collision_detection_result = collision_detector.search_service(
            target=square,
            dataset=square_stack.items,
        )
        # Handle the case that, the either a collision was detected or square wis not safe.
        if not collision_detection_result.is_no_collisions:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackExecuteException(
                        op=SquareStackExecuteException.OP,
                        msg=SquareStackExecuteException.MSG,
                        mthd=SquareStackExecuteException.MTHD,
                        mthd_rslt_type=SquareStackExecuteException.MTHD_RSLT,
                        ex=collision_detection_result.exception
                )
            )
        # --- ServiceRequest a rank quota report. ---#
        rank_quota_report = rank_quota_analyzer.search_service(
            rank=square.rank,
            square_stack=square_stack,
            rank_service=rank_service,
        )
        # Handle the case that, the request was not completed.
        if rank_quota_report.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackExecuteException(
                    op=SquareStackExecuteException.OP,
                    msg=SquareStackExecuteException.MSG,
                    mthd=SquareStackExecuteException.MTHD,
                    mthd_rslt_type=SquareStackExecuteException.MTHD_RSLT,
                    ex=rank_quota_report.exception
                )
            )
        # Handle the case that, there's no open slots for the square's rank.
        if rank_quota_report.payload.rank_is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackExecuteException(
                    op=SquareStackExecuteException.OP,
                    msg=SquareStackExecuteException.MSG,
                    mthd=SquareStackExecuteException.MTHD,
                    mthd_rslt_type=SquareStackExecuteException.MTHD_RSLT,
                    ex=SquareStackCapacityFullException(
                        msg=SquareStackCapacityFullException.MSG,
                        err_code=SquareStackCapacityFullException.ERR_CODE,
                    )
                )
            )
        # --- Integrity and performance tests are passed. ---#
        
        # Execute the square onto the schema
        square_stack.items.append(square)
        # Maintain state.
        if square_stack.is_full:
            square_stack.state = SquareStackState.READY_FOR_EXECUTEMENT
        
        # --- Send the work product ---#
        return InsertionResult.success()
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_token_tests(
            cls,
            token: Token,
            square_stack: SquareStackService,
            token_service: TokenService,
    ):
        method = f"{cls.__name__}._run_token_tests"
        
        # Handle the case that, the token does not pass a validation check.
        token_validation_result = token_service.validator.search_service(token)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ExecutementSquareDiscoveryException(
                    cls_mthd=method,
                    op=ExecutementSquareDiscoveryException.OP,
                    msg=ExecutementSquareDiscoveryException.MSG,
                    err_code=ExecutementSquareDiscoveryException.ERR_CODE,
                    mthd_rslt_type=ExecutementSquareDiscoveryException.MTHD_RSLT,
                    ex=token_validation_result.exception
                )
            )
        # Handle the case that, the token has already been executeed.
        if token.is_executeed:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ExecutementSquareDiscoveryException(
                    cls_mthd=method,
                    op=ExecutementSquareDiscoveryException.OP,
                    msg=ExecutementSquareDiscoveryException.MSG,
                    err_code=ExecutementSquareDiscoveryException.ERR_CODE,
                    mthd_rslt_type=ExecutementSquareDiscoveryException.MTHD_RSLT,
                    ex=token_validation_result.exception
                )
            )
        opening_square_search = square_stack.microservice.build(
            context=SquareContext(name=token.opening_square_name)
        )
        # Handle the case that the search fails
        if opening_square_search.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ExecutementSquareDiscoveryException(
                    cls_mthd=method,
                    op=ExecutementSquareDiscoveryException.OP,
                    msg=ExecutementSquareDiscoveryException.MSG,
                    err_code=ExecutementSquareDiscoveryException.ERR_CODE,
                    mthd_rslt_type=ExecutementSquareDiscoveryException.MTHD_RSLT,
                    ex=opening_square_search.exception
                )
            )
        # Handle the case that
        
        
        
        
    