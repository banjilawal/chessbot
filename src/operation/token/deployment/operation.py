# src/operation/token/deployment/operation.py

"""
Module: operation.token.deployment.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from copy import deepcopy
from typing import cast

from analyzer import HomeSquareClaimAnalyzer
from controller import WorkerRegistryController
from err import TokenDeploymentException
from model import DeploymentState, OpeningSquare, Token, TokenHomeClaimState
from operation import Operation
from report import HomeSquareClaimReport
from result import MethodResultType, UpdateResult
from util import LoggingLevelRouter


class TokenDeployer(Operation[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner
        
    Responsibilities:
        1.  Puts token onto its opening square on the board.
        2.  Preserve original and updated data for rollbacks.
        3.  Ensure the token's integrity and consistency are maintained during the transaction.
    
    Attributes:
    
    Provides:
        -   execute(
                    token: Token,
                    home_square_claim_analyzer: HomeSquareClaimAnalyzer,
            ) -> UpdateResult[Token]
            
    Super:
        Operation
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            home_square_claim_analyzer: HomeSquareClaimAnalyzer | None = None,
    ) -> UpdateResult[Token]:
        """
        Executes the deployment transaction.
        
        Action:
            1.  Send the unmodified token along with an exception chain in the UpdateResult if either
                    -   HomeSquare claim analysis fails.
                    -   Square visitation fails.
            2.  Otherwise:
                    -   Deepcopy of token to pre_update_token.
                    -   Ensure the token's state is deployed.
                    -   Ensure the opening square is marked as claimed.
            3.  Send the success result containing, the finished work product.
        Args:
            token: Token
            home_square_claim_analyzer: HomeSquareClaimAnalyzer
        Returns:
            UpdateResult[Token]
        Raises:
            TokenDeploymentException
        """
        method = f"{cls.__class__.__name__}.deploy_on_board"
        
        # --- Supply any missing dependencies. ---#
        if home_square_claim_analyzer is None:
            home_square_claim_analyzer = HomeSquareClaimAnalyzer()
         
        # Handle the case that, a claim report is not generated.
        analysis_result = home_square_claim_analyzer.analyze(token=token)
        if analysis_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=analysis_result.exception,
                )
            )
        claim_report = cast(HomeSquareClaimReport, analysis_result.payload)
        pre_update_token = deepcopy(token)
        
        # Make a visitation request to square_validator.
        visitation_result = token.team.board.squares.service.begin_square_visit(
            visitor=token,
            square=claim_report.home_square,
        )
        # Handle the case that, the visitation transaction fails.
        if visitation_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_token,
                exception=TokenDeploymentException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=visitation_result.exception,
                )
            )
        # --- Token has occupied its home square. Perform consistency maintenance tasks. ---#
        home_square = cast(OpeningSquare, visitation_result.payload)
        token = home_square.occupant
        
        # Confirm token's deployment state is updated.
        if token.deployment_state == DeploymentState.NOT_DEPLOYED:
            token.mark_deployed()
        # Confirm opening_square is marked as claimed.
        if home_square.token_claim_state != TokenHomeClaimState.UNCLAIMED:
            home_square.record_claim()
            
        # --- Forward the work product to the client. ---#
        return UpdateResult.update_success(original=pre_update_token, updated=token,)


# Register the operation.
WorkerRegistryController.register_worker(TokenDeployer)
        