# src/logic/square/service/visitation/entry/entryer.py

"""
Module: logic.square.service.visitation.entry.entryer
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from copy import deepcopy

from logic.square import (
    Square, SquareOccupiedException, SquareState, SquareValidator, SquareValidator,
    SquareVisitorBoardException, SquareVisitorDisabledException, WrongOpeningSquareException
)
from logic.square.service.visitation.entry import SquareEntryException
from logic.system import LoggingLevelRouter, UpdateResult
from logic.token import Token, TokenBoardState, TokenService


class SquareEntryProcess:
    """
    Role:Update Handler, Consistency, Integrity Maintenance, Lifecycle Management

    Responsibilities:
    1.  Ensure integrity and consistency are maintained during the  square's occupation lifecycle.

    Super Class:
   None

    Provides:


    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR ARGS:
    None

    # LOCAL METHODS:
        *   entry_visit(token: Token, square: Square, square_validator: SquareValidator) -> UpdateResult[Square]
        *   terminate_visit(square: Square, square_validator: SquareValidator) -> DeletionResult[Token]

    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            square: Square,
            token_service: TokenService = TokenService(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> UpdateResult[Square]:
        """
        Action:
            1.  If the square is either unsafe put the square and exception chain  in the UpdateResult  then
                return the client. Else make a deep copy of the square.
            2.  If th  square is already occupied put the deep_copy and the exception chain  in the UpdateResult
                sent to the client.
            3.  If the token is either
                    *   Disabled.
                    *   Not certified safe.
                    *   Belongs to a different board.
                    *   unformed but want to entry from the wrong square.
                put deep_copy and the exception chain in the UpdateResult sent to the client.
            4.  Configure the square side of the square-token binding.
            5.  Configure the token side of the square-token binding.
            6.  Send deep_copy and the current square in the success result.

        Args:
            token: Token
            square: Square
            token_service: TokenService
            square_validator: SquareValidator

       Returns:
            UpdateResult[Square]

        Raises:
            EnterSquareProcessException
            SquareEntryException
            SquareOccupiedException
            SquareVisitorBoardException
            SquareVisitorDisabledException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # Handle the case that, the square does not pass a securityy test.
        square_security_test_result = cls._run_square_tests(square=square, square_validator=square_validator)
        if square_security_test_result.is_failure:
            return square_security_test_result
        
        # Handle the case that, the token does not pass a security test.
        token_security_test_result = cls._run_token_tests(token=token, square=square, token_service=token_service)
        if token_security_test_result.is_failure:
            return token_security_test_result
    
        # Handle the case that, an unformed token is trying to entry from the wrong square.
        deployment_test_result = cls._run_deployment_tests(square=square, token=token)
        if deployment_test_result.is_failure:
            return deployment_test_result
        
        # --- Integrity and consistency checks are passed. Perform visit registration tasks ---#
        return cls._register_token_visit(square=square, token=token)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _register_token_visit(cls, square: Square, token: Token) -> UpdateResult[Square]:
        """

        Action:
            1.  Send the square and an exception chain in the UpdateResult if:
                    - Pushing the square's coord onto the token's stack fails.
            2.  Otherwise, send the success result
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
        
        # --- Push the square's coord onto the stack. ---#
        coord_insertion_result = token.positions.push(square.coord)
        
        # Handle the case that, the push failed
        if coord_insertion_result.is_failure:
            square.occupant = None
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=SquareEntryException(
                    mthd=method,
                    op=SquareEntryException.OP,
                    msg=SquareEntryException.MSG,
                    err_code=SquareEntryException.ERR_CODE,
                    rslt_type=SquareEntryException.RSLT_TYPE,
                    ex=coord_insertion_result.exception,
                )
            )
        
        if token.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            token.board_state = TokenBoardState.DEPLOYED_ON_BOARD
        # --- Send the update success result to the client. ---#
        return UpdateResult.update_success(original=pre_update_square, updated=square)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_token_tests(
            cls,
            token: Token,
            square: Square,,
            token_service: TokenService,
    ) -> UpdateResult[Square]:
        """
        Tests if the token can enter the square.

        Action:
            1.  Send the square and an exception chain in the UpdateResult if:
                    -   The token is not certified as safe.
                    -   The token is disabled.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            square: Square
            token_service: TokenService
        Returns:
            UpdateResult[Square]
        Raises:
            SquareEntryException
            SquareOccupiedException
        """
        method = f"{cls.__module__}._run_token_tests"
        
        # Handle the case that, the token is not certified safe.
        token_validation_result = token_service.validator.validate(candidate=token)
        if token_validation_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=SquareEntryException(
                    mthd=method,
                    op=SquareEntryException.OP,
                    msg=SquareEntryException.MSG,
                    err_code=SquareEntryException.ERR_CODE,
                    rslt_type=SquareEntryException.RSLT_TYPE,
                    ex=token_validation_result.exception,
                )
            )
        # Handle the case that, the token belongs to a different board
        if token.team.board != square.board:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=SquareEntryException(
                    mthd=method,
                    op=SquareEntryException.OP,
                    msg=SquareEntryException.MSG,
                    err_code=SquareEntryException.ERR_CODE,
                    rslt_type=SquareEntryException.RSLT_TYPE,
                    ex=SquareVisitorBoardException(
                        msg=SquareVisitorBoardException.MSG,
                        err_code=SquareVisitorBoardException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the occupant is disabled
        if token.is_disabled:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=SquareEntryException(
                    mthd=method,
                    op=SquareEntryException.OP,
                    msg=SquareEntryException.MSG,
                    err_code=SquareEntryException.ERR_CODE,
                    rslt_type=SquareEntryException.RSLT_TYPE,
                    ex=SquareVisitorDisabledException(
                        msg=SquareVisitorDisabledException.MSG,
                        err_code=SquareVisitorDisabledException.ERR_CODE,
                    )
                )
            )
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
            SquareEntryException
            SquareOccupiedException
        """
        method = f"{cls.__module__}._run_square_tests"
        
        # Handle the case that, the square is not certified safe.
        square_validation_result = square_validator.validate(square)
        if square_validation_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=SquareEntryException(
                    mthd=method,
                    op=SquareEntryException.OP,
                    msg=SquareEntryException.MSG,
                    err_code=SquareEntryException.ERR_CODE,
                    rslt_type=SquareEntryException.RSLT_TYPE,
                    ex=square_validation_result.exception,
                )
            )
        # Handle the case that, the square is already occupied.
        if square.is_occupied:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=SquareEntryException(
                    mthd=method,
                    op=SquareEntryException.OP,
                    msg=SquareEntryException.MSG,
                    err_code=SquareEntryException.ERR_CODE,
                    rslt_type=SquareEntryException.RSLT_TYPE,
                    ex=SquareOccupiedException(
                        msg=SquareOccupiedException.MSG,
                        err_code=SquareOccupiedException.ERR_CODE,
                    ),
                )
            )
        return UpdateResult.update_success(original=square, updated=square)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_deployment_tests(
            cls,
            token: Token,
            square: Square,
    ) -> UpdateResult[Square]:
        """
        # ACTION:
            1.  If the token's opening name differs from the target's return a
            ValidationResult with the exception.
                Else return a Validation success result.
        Args:
            visitor: Token
            target: Square
        Returns:
            ValidationResult[Square]
        Raises:
            WrongOpeningSquareException
        """
        method = f"{cls.__name__}_run_deployment_tests"
        
        # Handle the case that, the token has already been deployed.
        if token.is_deployed:
            return UpdateResult.update_success(original=square, updated=square)
        
        # Handle the case that, the token should open on a different square.
        if square.name.upper() != token.opening_square_name.upper():
            # Return the exception chain on failure.
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=SquareEntryException(
                    mthd=method,
                    op=SquareEntryException.OP,
                    msg=SquareEntryException.MSG,
                    err_code=SquareEntryException.ERR_CODE,
                    rslt_type=SquareEntryException.RSLT_TYPE,
                    ex=WrongOpeningSquareException(
                        msg=WrongOpeningSquareException.MSG,
                        err_code=WrongOpeningSquareException.ERR_CODE
                    )
                )
            )
        # --- Send the success result to the caller. ---#
        return UpdateResult.update_success(original=square, updated=square)