# src/logic/token/service/operation/deployment/deployer.py

"""
Module: logic.token.service.operation.deployment.deployer
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from _ast import List
from copy import deepcopy
from typing import cast

from logic.square import Square, SquareContext, SquareNotFoundException, VisitingOccupiedSquareException
from logic.system import LoggingLevelRouter, SearchResult, UpdateResult
from logic.token import (
    InconsistentTokenCoordException, InconsistentTokenSquareException, Token, TokenAlreadyDeployedException,
    TokenBoardState, TokenDeploymentException, TokenValidator
)


class TokenDeployment:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner
        
    Responsibilities:
        1.  Token deployment process owner.
        2.  Preserve original and updated data for rollbacks.
        3.  Ensure the token's integrity and consistency are maintained during the transaction.
    Attributes:
    Provides:
        -   execute(
                    token: Token,
                    token_validator: TokenValidator,
            ) -> UpdateResult[Token]
            
        - _run_opening_square_tests(token: Token) -> SearchResult[List[Square]]
        
        - _square_visitation_process_wrapper(
                    token: Token,
                    pre_update_token: Token,
                    opening_square: Square,
            ) -> UpdateResult[Token]
    Super:
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_validator: TokenValidator = TokenValidator(),
    ) -> UpdateResult[Token]:
        """
        Executes the deployment transaction.
        
        Action:
            1.  Send the unmodified pawn_token along with an exception chain in the UpdateResult if:
                        *   The token is not certified as safe and actionable.
                        *   The token is already deployed.
                        *   Its opening square fails a test
                        *   The square visitation transaction fails.
            2.  Otherwise:
                    *   Deepcopy token to pre_update_token.
                    *   Set the token's board_state to BoardState.DEPLOYED_ON_BOARD.
            3.  Send the success result containing, the finished work product.
        # Args:
            token: Token
        Returns:
            UpdateResult[Token]
        Raises:
            TokenDeploymentException
            TokenAlreadyDeployedException
        """
        method = f"{cls.__class__.__name__}.deploy_on_board"
        # Handle the case that, the token is not certified safe.
        token_validation = token_validator.validate(token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=token_validation.exception,
                )
            )
        # Handle the case that, the token has already been deployed.
        if token.is_deployed:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=TokenAlreadyDeployedException(
                        msg=TokenDeploymentException.MSG,
                        err_code=TokenDeploymentException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, an opening_square test fails.
        opening_square_search_result = cls._run_opening_square_tests(token)
        if opening_square_search_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=opening_square_search_result.exception,
                )
            )
        # --- Integrity and consistency checks are passed. Make a deep copy of the original token. ---#
        pre_update_token = deepcopy(token)
        
        #--- Run _square_visitation_process_wrapper which runs token side consistency checks ---#
        update_result = cls._square_visitation_process_wrapper(
            token=token,
            pre_update_token=pre_update_token,
            square_service=token.team.board.squares.integrity_service,
            opening_square=cast(Square, opening_square_search_result.payload[0]),
        )
        # Handle the case that, the visitation transaction fails.
        if update_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=update_result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        return update_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_opening_square_tests(cls, token: Token) -> SearchResult[List[Square]]:
        """
        Get the token's opening square if, it can be occupied.
        
        Action:
            1.  Send an exception chain in the SearchResult if:
                *   The search does not run to completion.
                *   The square is not found.
                *   The square is occupied by a different token.
                *   The token is already on the square.
            2.  Otherwise, send the success result.,
        Args:
            token: Token
        Returns:
            SearchResult[Square]
        Raises:
            TokenDeploymentException
            SquareNotFoundException
            SquareOccupiedException
        """
        method = f"{cls.__class__.__name__}._run_opening_square_tests"
        
        # Get the board's squares to run the search.
        opening_square_search_result = token.team.board.squares.search(
            context=SquareContext(name=token.opening_square_name)
        )
        # Handle the case that, the search fails.
        if opening_square_search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=opening_square_search_result.exception,
                )
            )
        # Handle the case that, the token's square is not found.
        if opening_square_search_result.is_empty:
            # Return the exception chain on failure.
            return SearchResult.failure(
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=SquareNotFoundException(
                        var="opening_square_name",
                        val=token.opening_square_name,
                        msg=TokenDeploymentException.MSG,
                        err_code=TokenDeploymentException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the token's opening square is occupied
        if opening_square_search_result.payload[0].is_occupied:
            # Return the exception chain on failure.
            return SearchResult.failure(
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=VisitingOccupiedSquareException(
                        var="square_occupant",
                        msg=TokenDeploymentException.MSG,
                        err_code=TokenDeploymentException.ERR_CODE,
                        val=opening_square_search_result.payload[0].occupant.designation,
                    )
                )
            )
        # --- Send the work product. ---#
        return opening_square_search_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _square_visitation_process_wrapper(
            cls,
            token: Token,
            pre_update_token: Token,
            opening_square: Square,
    ) -> UpdateResult[Token]:
        """
        Run consistency checks on the token after SquareService.start_square_visit transaction
        has finished.
        
        Action:
            1.  Send the pre_deployment token along with an exception chain in UpdateResult if:
                    *  The visitation transaction was not successful.
                    *  The transaction was successful but either
                            *   The token is not registered with the square.
                            *   The square has a stale link to the token.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            pre_update_token: Token
            opening_square: Square
        Returns:
            UpdateResult[Square]
        Raises:
            TokenDeploymentException
            InconsistentTokenSquareException
            InconsistentTokenCoordException
        """
        method = f"{cls.__class__.__name__}._visitation_process_wrapper"
        
        # Make a visitation request to square_service.
        visitation_result = token.team.board.squares.integrity_service.begin_square_visit(
            visitor=token,
            square=opening_square,
        )
        # Handle the case that the visit is not successful.
        if visitation_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=visitation_result.exception,
                )
            )
        # Handle the case that, the token is not the square's visitor.
        if opening_square.occupant != token:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=InconsistentTokenSquareException(
                        msg=InconsistentTokenSquareException.MSG,
                        err_code=InconsistentTokenSquareException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the, token's current position is not the square's
        if opening_square.coord != token.current_position:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=InconsistentTokenCoordException(
                        msg=InconsistentTokenCoordException.MSG,
                        err_code=InconsistentTokenCoordException.ERR_CODE,
                    )
                )
            )
        # --- Ensure the token.board_state has been updated. ---#
        if token.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            token.board_state = TokenBoardState.DEPLOYED_ON_BOARD
            
        # --- Send the work product ---#
        return UpdateResult.update_success(original=pre_update_token, updated=token,)
        