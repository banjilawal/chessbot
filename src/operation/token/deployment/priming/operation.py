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

from analysis import SquareTokenRelationAnalyzer, TokenFreedomAnalyzer
from database.square.database import square
from err import (
    ConsistencyException, SquareNotFoundSearchException, SquareOccupiedException,
    TokenDeploymentPrimingException
)
from err.operation.token.deployment.duplicate.exception import DuplicateTokenDeploymentException
from model import OpeningSquare, SquareContext, Token
from operation import Operation
from report import RelationReport, TokenFreedomReport
from result import MethodResultType, UpdateResult, ValidationResult
from util import LoggingLevelRouter
from validation import TokenValidator


class TokenDeploymentPrimer(Operation[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner
        
    Responsibilities:
        1.  Token deployment exception owner.
        2.  Preserve original and updated data for rollbacks.
        3.  Ensure the token's integrity and consistency are maintained during the transaction.
    
    Attributes:
    
    Provides:
        -   execute(
                    token: Token,
                    token_validator: TokenValidator,
            ) -> UpdateResult[Token]
            
        - _run_opening_square_tests(token: Token) -> SearchResult[List[Square]]
        
        - _square_visitation_process_work(
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
            square_token_relation_analyzer: SquareTokenRelationAnalyzer | None = None,
            token_freedom_analyzer: TokenFreedomAnalyzer | None = None,
    ) -> ValidationResult[Token]:
        """
        Executes the deployment transaction.
        
        Action:
            1.  Send the unmodified pawn_token along with an exception chain in the UpdateResult if:
                        *   The token does not pass a validation check. and actionable.
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
            TokenDeploymentPrimingException
            TokenAlreadyDeployedException
        """
        method = f"{cls.__class__.__name__}.deploy_on_board"
        
        # --- Supply any missing dependencies. ---#
        if token_freedom_analyzer is None:
            token_freedom_analyzer = TokenFreedomAnalyzer()
        if square_token_relation_analyzer is None:
            square_token_relation_analyzer = SquareTokenRelationAnalyzer()
        
        # Handle the case that, the token is not safe.
        freedom_analysis_result = token_freedom_analyzer.analyze(token)
        if freedom_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=freedom_analysis_result.exception,
                )
            )
        report = cast (TokenFreedomReport, freedom_analysis_result.payload)
        # Handle the case that, the token has already been deployed.
        if report.token_is_deployed:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=DuplicateTokenDeploymentException(
                        msg=DuplicateTokenDeploymentException.MSG,
                        err_code=DuplicateTokenDeploymentException.ERR_CODE,
                    ),
                )
            )
        
        board = token.team.board
        square_search_result = board.squares.search(context=SquareContext(id=token.opening_square.id))
        if square_search_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=square_search_result.exception,
                )
            )
        if square_search_result.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=SquareNotFoundSearchException(
                        msg=SquareNotFoundSearchException.MSG,
                        err_code=SquareNotFoundSearchException.ERR_CODE,
                        var=f"opening_square:{token.opening_square.name}",
                        val=token.opening_square,
                    ),
                )
            )
        opening_square = cast(OpeningSquare, square_search_result.payload[0])
        if opening_square.is_activated:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=DuplicateTokenDeploymentException(
                        msg=DuplicateTokenDeploymentException.MSG,
                        err_code=DuplicateTokenDeploymentException.ERR_CODE,
                    ),
                )
            )
        opening_square = token.opening_square
        if opening_square.board != board:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=ConsistencyException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=f"Board inconsistency between token:{token.id} and opening_square:{opening_square.id}",
                        err_code=ConsistencyException.ERR_CODE,
                        var="board_ids()",
                        val=f"(opening_square_board.id:{opening_square.board.id}, token.board.id:{board.id})",
                    )
                )
            )
        
        square_token_relation_analysis_result = square_token_relation_analyzer.analyze(
            candidate_primary=token.opening_square,
            candidate_satellite=token
        )
        if square_token_relation_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=square_token_relation_analysis_result
                )
            )
        report = cast(RelationReport, square_token_relation_analysis_result.payload)
        if opening_square.is_occupied:
            ValidationResult.failure(
                exception=TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=TokenDeploymentPrimingException.MTHD_RSLT_TYPE,
                    ex=SquareOccupiedException(
                        var="square_occupant",
                        msg=f"square:{opening_square.name} already occupied by {opening_square.occupant.designation}",
                        err_code=SquareOccupiedException.ERR_CODE,
                        val=opening_square.occupant,
                    )
                )
            )
        # Handle the case that, an opening_square test fails.
        opening_square_search_result = cls._run_opening_square_tests(token)
        if opening_square_search_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=opening_square_search_result.exception,
                )
            )
        # --- Integrity and consistency checks are passed. Make a deep copy of the original token. ---#
        pre_update_token = deepcopy(token)
        
        #--- Run _square_visitation_process_work which runs token side consistency checks ---#
        update_result = cls._square_visitation_process_work(
            token=token,
            pre_update_token=pre_update_token,
            square_service=token.team.board.squares.service,
            opening_square=cast(OpeningSquare, opening_square_search_result.payload[0]),
        )
        # Handle the case that, the visitation transaction fails.
        if update_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                original=token,
                exception=TokenDeploymentPrimingException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
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
            TokenDeploymentPrimingException
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
            # Send the exception chain on failure.
            return SearchResult.failure(
                exception=TokenDeploymentPrimingException(
                    cls_mthd=method,
                    op=TokenDeploymentPrimingException.OP,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=TokenDeploymentPrimingException.MTHD_RSLT,
                    ex=opening_square_search_result.exception,
                )
            )
        # Handle the case that, the token's square is not found.
        if opening_square_search_result.is_empty:
            # Send the exception chain on failure.
            return SearchResult.failure(
                exception=TokenDeploymentPrimingException(
                    cls_mthd=method,
                    op=TokenDeploymentPrimingException.OP,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=TokenDeploymentPrimingException.MTHD_RSLT,
                    ex=SquareNotFoundException(
                        var="opening_square_name",
                        val=token.opening_square_name,
                        msg=TokenDeploymentPrimingException.MSG,
                        err_code=TokenDeploymentPrimingException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the token's opening square is occupied
        if opening_square_search_result.payload[0].is_occupied:
            square = opening_square_search_result.payload[0]
            # Send the exception chain on failure.
            return SearchResult.failure(
                exception=TokenDeploymentPrimingException(
                    cls_mthd=method,
                    op=TokenDeploymentPrimingException.OP,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=TokenDeploymentPrimingException.MTHD_RSLT,
                    ex=SquareOccupiedException(
                        var="square_occupant",
                        msg=f"square:{square.name} already occupied by {square.occupant.designation}",
                        err_code=SquareOccupiedException.ERR_CODE,
                        val=opening_square_search_result.payload[0].occupant.designation,
                    )
                )
            )
        # --- Send the work product. ---#
        return opening_square_search_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _square_visitation_process_work(
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
            TokenDeploymentPrimingException
            InconsistentTokenSquareException
            InconsistentTokenCoordException
        """
        method = f"{cls.__class__.__name__}._visitation_process_work"
        
        # Make a visitation request to square_validator.
        visitation_result = token.team.board.squares.service.begin_square_visit(
            visitor=token,
            square=opening_square,
        )
        # Handle the case that the visit is not successful.
        if visitation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                original=token,
                exception=TokenDeploymentPrimingException(
                    cls_mthd=method,
                    op=TokenDeploymentPrimingException.OP,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=TokenDeploymentPrimingException.MTHD_RSLT,
                    ex=visitation_result.exception,
                )
            )
        # Handle the case that, the token is not the square's visitor.
        if opening_square.occupant != token:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                original=pre_update_token,
                exception=TokenDeploymentPrimingException(
                    cls_mthd=method,
                    op=TokenDeploymentPrimingException.OP,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=TokenDeploymentPrimingException.MTHD_RSLT,
                    ex=InconsistentTokenSquareException(
                        msg=InconsistentTokenSquareException.MSG,
                        err_code=InconsistentTokenSquareException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the token's current position is not the square's
        if opening_square.coord != token.current_position:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                original=pre_update_token,
                exception=TokenDeploymentPrimingException(
                    cls_mthd=method,
                    op=TokenDeploymentPrimingException.OP,
                    msg=TokenDeploymentPrimingException.MSG,
                    err_code=TokenDeploymentPrimingException.ERR_CODE,
                    mthd_rslt_type=TokenDeploymentPrimingException.MTHD_RSLT,
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
        