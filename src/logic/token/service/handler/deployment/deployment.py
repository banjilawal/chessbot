# src/logic/token/service/handler/deployment/deployer.py

"""
Module: logic.token.service.handler.deployment.deployer
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
    # ROLE: Update Handler, Consistency, Integrity Maintenance, Lifecycle Management

    # RESPONSIBILITIES:
    1.  Ensure integrity and consistency are maintained during the pawn's deployment lifecycle.

    # PARENT:
    None

    # PROVIDES:
    None

    Attributes:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
    None

    # LOCAL METHODS:

    # INHERITED METHODS:
    None
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_validator: TokenValidator = TokenValidator(),
    ) -> UpdateResult[Token]:
        """
        # ACTION:
            1.  If the token or coord fail their validations return the exception in the InsertionResult.
            2.  If the position is already the updated position return the exception in the InsertionResult.
            3.  If the pushing the position to the token's coord stack fails encapsulate the exception then
                send the exception chain in the InsertionResult's payload.

        # Args:
            token: Token

        Returns:
            InsertionResult

        Raises:
            TokenServiceException
            CoordAlreadyToppingStackException
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
        opening_square_search_result = cls._square_search_runner(token)
        # Handle the case that, the square was not verified.
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
        
        pre_update_token = deepcopy(token)
        visitation_result = token.team.board.squares.integrity_service.begin_square_visit(
            visitor=token,
            square=opening_square_search_result.payload[0]
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
                    ex=opening_square_search_result.exception,
                )
            )
        updated_square = cast(Square, visitation_result.updated)
        
        # Handle the case that, the token is not the square's visitor.
        if updated_square.occupant != token:
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
        if token.current_position != updated_square.coord:
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
        # --- Assure that token.board_state has been updated. ---#
        if updated_square.occupant.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            updated_square.occupant.board_state = TokenBoardState.DEPLOYED_ON_BOARD
            
        return UpdateResult.update_success(
            original=pre_update_token,
            updated=updated_square.occupant,
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _square_search_runner(cls, token: Token) -> SearchResult[List[Square]]:
        """
        Args:
            token: Token
        """
        method = f"{cls.__class__.__name__}._opening_square_search_resultrunner"
        
        board = token.team.board
        opening_square_search_result = board.squares.search(
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
        return opening_square_search_result