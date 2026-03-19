# src/logic/square/database/kernel/operation/process.py

"""
Module: logic.square.database.kernel.operation.deployer
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.square.database.kernel.operation.deploy import TokenDeploymentProcessException
from logic.system import InsertionResult, LoggingLevelRouter, UpdateResult, ValidationResult
from logic.square import (
    SquareContext, SquareStackCapacityFullException, Square, SquareStackFullException,
    SquareStackDeployException, SquareStackService, SquareStackState
)
from logic.token import Token, TokenService


class TokenDeploymentProcess:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Token deployment process owner.

    Attributes:

    Provides:
        -   deploy(
                    cls,
                    square: Square,
                    square_stack: SquareStackService,
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: SquareStackCapacityAnalyzer = SquareStackCapacityAnalyzer(),
                    collision_detector: SquareCollisionAnalysis = SquareCollisionAnalysis(),
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
    ) -> UpdateResult[Square]:
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
            TokenDeploymentException
            SquareStackFullException
        """
        method =  f"{cls.__name__}.execute"
        
        # Handle the case that, the token is not certified as safe.
        token_validation_result = token_service.validator.execute(token)
        if token_validation_result.is_failure:
            # Return the exception chain on failure
            
            return InsertionResult.failure(
                SquareStackDeployException(
                    mthd=method,
                    op=SquareStackDeployException.OP,
                    msg=SquareStackDeployException.MSG,
                    err_code=SquareStackDeployException.ERR_CODE,
                    rslt_type=SquareStackDeployException.RSLT_TYPE,
                    ex=SquareStackFullException(
                        msg=SquareStackFullException.MSG,
                        err_code=SquareStackFullException.ERR_CODE,
                    )
                )
            )
        if square_stack.is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackDeployException(
                    mthd=method,
                    op=SquareStackDeployException.OP,
                    msg=SquareStackDeployException.MSG,
                    err_code=SquareStackDeployException.ERR_CODE,
                    rslt_type=SquareStackDeployException.RSLT_TYPE,
                    ex=SquareStackFullException(
                        msg=SquareStackFullException.MSG,
                        err_code=SquareStackFullException.ERR_CODE,
                    )
                )
            )
        # Request a collision report. The square is verified during the report generation. ---#
        collision_detection_result = collision_detector.execute(
            target=square,
            collider_candidates=square_stack.items,
        )
        # Handle the case that, the either a collision was detected or square wis not safe.
        if not collision_detection_result.is_no_collision:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackDeployException(
                        op=SquareStackDeployException.OP,
                        msg=SquareStackDeployException.MSG,
                        mthd=SquareStackDeployException.MTHD,
                        rslt_type=SquareStackDeployException.RSLT_TYPE,
                        ex=collision_detection_result.exception
                )
            )
        # --- Request a rank quota report. ---#
        rank_quota_report = rank_quota_analyzer.execute(
            rank=square.rank,
            square_stack=square_stack,
            rank_service=rank_service,
        )
        # Handle the case that, the request was not completed.
        if rank_quota_report.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackDeployException(
                    op=SquareStackDeployException.OP,
                    msg=SquareStackDeployException.MSG,
                    mthd=SquareStackDeployException.MTHD,
                    rslt_type=SquareStackDeployException.RSLT_TYPE,
                    ex=rank_quota_report.exception
                )
            )
        # Handle the case that, there's no open slots for the square's rank.
        if rank_quota_report.payload.rank_is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackDeployException(
                    op=SquareStackDeployException.OP,
                    msg=SquareStackDeployException.MSG,
                    mthd=SquareStackDeployException.MTHD,
                    rslt_type=SquareStackDeployException.RSLT_TYPE,
                    ex=SquareStackCapacityFullException(
                        msg=SquareStackCapacityFullException.MSG,
                        err_code=SquareStackCapacityFullException.ERR_CODE,
                    )
                )
            )
        # --- Integrity and performance tests are passed. ---#
        
        # Deploy the square onto the stack
        square_stack.items.append(square)
        # Maintain state.
        if square_stack.is_full:
            square_stack.state = SquareStackState.READY_FOR_DEPLOYMENT
        
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
        
        # Handle the case that, the token is not certified as safe.
        token_validation_result = token_service.validator.execute(token)
        if token_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentProcessException(
                    mthd=method,
                    op=TokenDeploymentProcessException.OP,
                    msg=TokenDeploymentProcessException.MSG,
                    err_code=TokenDeploymentProcessException.ERR_CODE,
                    rslt_type=TokenDeploymentProcessException.RSLT_TYPE,
                    ex=token_validation_result.exception
                )
            )
        # Handle the case that, the token has already been deployed.
        if token.is_deployed:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentProcessException(
                    mthd=method,
                    op=TokenDeploymentProcessException.OP,
                    msg=TokenDeploymentProcessException.MSG,
                    err_code=TokenDeploymentProcessException.ERR_CODE,
                    rslt_type=TokenDeploymentProcessException.RSLT_TYPE,
                    ex=token_validation_result.exception
                )
            )
        opening_square_search = square_stack.integrity_service.search(
            context=SquareContext(name=token.opening_square_name)
        )
        # Handle the case that the search fails
        if opening_square_search.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentProcessException(
                    mthd=method,
                    op=TokenDeploymentProcessException.OP,
                    msg=TokenDeploymentProcessException.MSG,
                    err_code=TokenDeploymentProcessException.ERR_CODE,
                    rslt_type=TokenDeploymentProcessException.RSLT_TYPE,
                    ex=opening_square_search.exception
                )
            )
        # Handle the case that
        
        
        
        
    