# src/logic/token/database/kernel/operation/deployment/validator.py

"""
Module: logic.token.database.kernel.operation.deployment.process
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy

from system import LoggingLevelRouter, UpdateResult
from model.state.token import TokenStackService, TokenStackState
from model.state.token import (
    TokenStackAlreadyDeployedException,
    TokenStackDeploymentException
)


class TokenStackDeployment:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, token_stack: TokenStackService) -> UpdateResult[TokenStackService]:
        """
        Deploy each token to its opening square.
        
        Action:
            1.  Create a container for tokens that have been deployed.
            2.  Process the schema's members in a loop.
            3.  If a token's deployment fails:
                    -   Undo all the previous deployments.
                    -   Send an exception chain the deletion result.
            4.  Otherwise, empty the schema and send the success result.
        Args:
            token_stack: TokenStack
        Returns:
            DeletionResult[List[Token]]
        Raises:
        
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the token_stack has already been deployed on the board.
        if token_stack.is_deployed_on_board:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=token_stack,
                exception=TokenStackDeploymentException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenStackDeploymentException.OP,
                    msg=TokenStackDeploymentException.MSG,
                    err_code=TokenStackDeploymentException.ERR_CODE,
                    mthd_rslt_type=TokenStackDeploymentException.MTHD_RSLT,
                    ex=TokenStackAlreadyDeployedException(
                        msg=TokenStackAlreadyDeployedException.MSG,
                        err_code=TokenStackAlreadyDeployedException.ERR_CODE
                    )
                )
            )
        # --- Make a deep copy of the schema then deploy its members in a loop. ---#
        pre_deployment_token_stack = deepcopy(token_stack)
        for token in token_stack.iterator:
            deployment_result = token_stack.microservice.controller.deployment.work(token)
            
            # Handle the case that, the token's deployment failed.
            if deployment_result.is_failure:
                # Send the exception chain on failure.
                return UpdateResult.update_failure(
                    original=pre_deployment_token_stack,
                    exception=TokenStackDeploymentException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenStackDeploymentException.OP,
                        msg=TokenStackDeploymentException.MSG,
                        err_code=TokenStackDeploymentException.ERR_CODE,
                        mthd_rslt_type=TokenStackDeploymentException.MTHD_RSLT,
                        ex=deployment_result.exception,
                    )
                )
        # --- Clean up and update the schema' state. ---#
        token_stack.items.clear()
        token_stack.stack_state = TokenStackState.DEPLOYED
        
        # --- Forward the work product to the caller. ---#
        return UpdateResult.update_success(
            original=pre_deployment_token_stack,
            updated=token_stack
        )

        