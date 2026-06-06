# src/operation/square/entry/operation.py

"""
Module: operation.square.entry.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import TokenFreedomAnalyzer
from err import MovePermissionAnalyzerException, SquareVisitorBoardException
from err.analyzer.move.disabled.exception import DisabledTokenMoveException
from model import Square, Token
from report import MoveOrder, TokenFreedomReport
from result import MethodResultType, ValidationResult
from util import LoggingLevelRouter
from validation import SquareValidator


class MovePermissionAnalyzer:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Square entry exception owner.
        2.  Preserve original and updated square data for rollbacks.
        3.  Ensure both the token and the squares are consistent throughout
            square entry lifecycle.

    Attributes:
    
    Provides:
        -   execute(
                    token: Token,
                    square: Square,
                    token_freedom_analyzer: TokenFreedomAnalyzer,
                    square_validator: SquareValidator,
            ) -> UpdateResult[Square]:

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            square: Square,
            square_validator: SquareValidator | None = None,
            token_freedom_analyzer: TokenFreedomAnalyzer | None = None,
    ) -> ValidationResult[MoveOrder]:
        """
        Action:
            1.  Send the original square along with an exception chain in the validation result if:
                    -   The square or token are insecure.
                    -   The token is disabled
                    -   The token belongs to a different board.
                    -   The new token is being deployed to the wrong square.
                    -   The square is already occupied.
                    -   The square accepts the token but the token cannot update its position.
            2.  Otherwise, each updates its state.
            3.  Send the success result.
        Args:
            token: Token
            square: Square
            token_freedom_analyzer: TokenFreedomAnalyzer
            square_validator: SquareValidator
       Returns:
            UpdateResult[Square]
        Raises:
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if square_validator is None:
            square_validator = SquareValidator()
        if token_freedom_analyzer is None:
            token_freedom_analyzer = TokenFreedomAnalyzer()
        
        token_freedom_analysis_result = token_freedom_analyzer.analyze(token)
        # Handle the case that, the freedom_analysis is not completed.
        if token_freedom_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MovePermissionAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=token_freedom_analysis_result.exception,
                )
            )
        report = cast(TokenFreedomReport, token_freedom_analysis_result.payload)
        # Handle the case that, the token is not free.
        if report.token_is_not_free:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MovePermissionAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=DisabledTokenMoveException(
                        msg=DisabledTokenMoveException.MSG,
                        err_code=DisabledTokenMoveException.ERR_CODE,
                    ),
                )
            )
        # Handle the case, that the square is flagged by the validator.
        square_validation_result = square_validator.validate(square)
        if square_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MovePermissionAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=square_validation_result.exception,
                )
            )
        # Handle the case that, the token and square are on different boards.
        if token.team.board != square.board:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MovePermissionAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=SquareVisitorBoardException(
                        msg=SquareVisitorBoardException.MSG,
                        err_code=SquareVisitorBoardException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the token is already on the square.
        
        # Handle the case that, the square does not pass a security test.
        square_security_test_result = cls._run_square_tests(
            square=square,
            square_validator=square_validator
        )
        if square_security_test_result.is_failure:
            return square_security_test_result
        
        # Handle the case that, the token does not pass a security test.
        token_security_test_result = cls._run_token_tests(
            token=token,
            square=square,
            token_freedom_analyzer=token_freedom_analyzer
        )
        if token_security_test_result.is_failure:
            return token_security_test_result
        
        # Handle the case that, an unformed token is trying to entry from the wrong square.
        deployment_test_result = cls._run_deployment_tests(
            square=square,
            token=token
        )
        if deployment_test_result.is_failure:
            return deployment_test_result
        
        # --- Security tests are passed. Return the registration result to the caller. ---#
        return cls._register_token_visit(square=square, token=token)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _register_token_visit(cls, square: Square, token: Token) -> UpdateResult[Square]:
        """
        Puts the token into the square.

        Action:
            1.  Send the square and an exception chain in the UpdateResult if:
                    - Pushing the square's coord onto the token's schema fails.
            2.  Otherwise, after:
                    -   The square makes the token its occupant
                    -   The token updates its position
                    -   Each updates its state.
            3.  Send the success result.
        Args:
            square: Square
            token: Token
        Returns:
            UpdateResult[Square]
        """
        method = f"{cls.__name__}._register_token_visit"
        
        #  Make a deep copy of the square.
        pre_update_square = deepcopy(square)
        # --- Set the square side of the relationship. ---#
        square.occupant = token
        square.state = SquareState.OCCUPIED
        
        # --- Push the square's coord onto the schema. ---#
        coord_insertion_result = token.positions.push(square.coord)
        
        # Handle the case that, the push failed
        if coord_insertion_result.is_failure:
            # Rollback the square.
            square.occupant = None
            square.state = SquareState.EMPTY
            
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=MovePermissionAnalyzerException(
                    cls_mthd=method,
                    op=MovePermissionAnalyzerException.OP,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MovePermissionAnalyzerException.MTHD_RSLT,
                    ex=coord_insertion_result.exception,
                )
            )
        # --- Update the token's deployment state. ---#
        if token.deployment_state == DeploymentState.NOT_DEPLOYED:
            token.deployment_state = DeploymentState.DEPLOYED
            
        # --- Forward the work product to the caller. ---#
        return UpdateResult.update_success(original=pre_update_square, updated=square)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_token_tests(
            cls,
            token: Token,
            square: Square,
            token_freedom_analyzer: TokenFreedomAnalyzer,
    ) -> UpdateResult[Square]:
        """
        Tests if the token can enter the square.

        Action:
            1.  Send the square and an exception chain in the UpdateResult if:
                    -   The token does not pass a validation check.
                    -   The token is disabled.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            square: Square
            token_freedom_analyzer: TokenFreedomAnalyzer
        Returns:
            UpdateResult[Square]
        Raises:
            MovePermissionAnalyzerException
            SquareOccupiedException
        """
        method = f"{cls.__module__}._run_token_tests"
        
        # Handle the case that, the tokenis not safe.
        token_validation_result = token_freedom_analyzer.validator.search_service(candidate=token)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=MovePermissionAnalyzerException(
                    cls_mthd=method,
                    op=MovePermissionAnalyzerException.OP,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MovePermissionAnalyzerException.MTHD_RSLT,
                    ex=token_validation_result.exception,
                )
            )
        # Handle the case that, the token belongs to a different board
        if token.team.board != square.board:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=MovePermissionAnalyzerException(
                    cls_mthd=method,
                    op=MovePermissionAnalyzerException.OP,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MovePermissionAnalyzerException.MTHD_RSLT,
                    ex=SquareVisitorBoardException(
                        msg=SquareVisitorBoardException.MSG,
                        err_code=SquareVisitorBoardException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the occupant is disabled
        if token.is_disabled:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=MovePermissionAnalyzerException(
                    cls_mthd=method,
                    op=MovePermissionAnalyzerException.OP,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MovePermissionAnalyzerException.MTHD_RSLT,
                    ex=SquareVisitorDisabledException(
                        msg=SquareVisitorDisabledException.MSG,
                        err_code=SquareVisitorDisabledException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return UpdateResult.update_success(original=square, updated=square)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_square_tests(
            cls,
            square: Square,
            square_validator: SquareValidator
    ) -> UpdateResult[Square]:
        """
        Tests if the square can be visited.
        
        Action:
            1.  Send the square and an exception chain in the UpdateResult if:
                    -   The square is not safe.
                    -   The square is already occupied.
            2.  Otherwise, send the success result.
        Args:
            square: Square
            square_validator: SquareValidator
        Returns:
            UpdateResult[Square]
        Raises:
            MovePermissionAnalyzerException
            SquareOccupiedException
        """
        method = f"{cls.__module__}._run_square_tests"
        
        # Handle the case that, the squareis not safe.
        square_validation_result = square_validator.validate(square)
        if square_validation_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=MovePermissionAnalyzerException(
                    cls_mthd=method,
                    op=MovePermissionAnalyzerException.OP,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MovePermissionAnalyzerException.MTHD_RSLT,
                    ex=square_validation_result.exception,
                )
            )
        # Handle the case that, the square is already occupied.
        if square.is_occupied:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=MovePermissionAnalyzerException(
                    cls_mthd=method,
                    op=MovePermissionAnalyzerException.OP,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MovePermissionAnalyzerException.MTHD_RSLT,
                    ex=SquareOccupiedException(
                        msg=SquareOccupiedException.MSG,
                        err_code=SquareOccupiedException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return UpdateResult.update_success(original=square, updated=square)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_deployment_tests(
            cls,
            token: Token,
            square: Square,
    ) -> UpdateResult[Square]:
        """
        Tests if  new tokens are deployed to the correct square.
        
        # ACTION:
            1.  If the token has not been deployed and the it has not been assigned to the square,
                send the square along wih exception chain in the UpdateResult.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            square: Square
        Returns:
            ValidationResult[Square]
        Raises:
            MovePermissionAnalyzerException
            WrongOpeningSquareException
        """
        method = f"{cls.__name__}_run_deployment_tests"
        
        # If the token has already been deployed return.
        if token.is_deployed:
            return UpdateResult.update_success(original=square, updated=square)
        
        # Handle the case that, the token should open on a different square.
        if square.name.upper() != token.opening_square_name.upper():
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=MovePermissionAnalyzerException(
                    cls_mthd=method,
                    op=MovePermissionAnalyzerException.OP,
                    msg=MovePermissionAnalyzerException.MSG,
                    err_code=MovePermissionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MovePermissionAnalyzerException.MTHD_RSLT,
                    ex=WrongOpeningSquareException(
                        msg=WrongOpeningSquareException.MSG,
                        err_code=WrongOpeningSquareException.ERR_CODE
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return UpdateResult.update_success(original=square, updated=square)