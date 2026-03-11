# src/logic/square/service/visitation/handler.py

"""
Module: logic.square.service.visitation.handler
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from copy import deepcopy

from logic.square import (
    NoVisitForTerminationException, Square, SquareService, SquareState, SquareVisitorDisabledException,
    StartSquareVisitException, TerminateSquareVisitException, TokenVisitHandlerException,
    VisitingOccupiedSquareException, VisitingWrongOpeningSquareException, VisitorFromWrongBoardException
)
from logic.system import DeletionResult, LoggingLevelRouter, UpdateResult, ValidationResult
from logic.token import Token, TokenBoardState, TokenService


class TokenVisitHandler:
    """
    # ROLE: Consistency, Integrity Maintenance, Lifecycle Management, Util

    # RESPONSIBILITIES:
    1.  Ensure integrity and consistency  are maintained in all stages of the square occupation lifecycle.

    # PARENT:
        *   IntegrityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   token-service (TokenService)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR ARGS:
        Local:
            *   token_service (TokenService)
        Inherited:
        None

    # LOCAL METHODS:
        *   start_visit(token: Token, square: Square, square_validator: SquareValidator) -> UpdateResult[Square]
        *   terminate_visit(square: Square, square_validator: SquareValidator) -> DeletionResult[Token]
        
    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def start_visit(
            cls,
            token: Token,
            square: Square,
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
    ) -> UpdateResult[Square]:
        """
        # ACTION:
            1.  If the square is either unsafe put the square and exception chain  in the UpdateResult  then
                return the client. Else make a deep copy of the square.
            2.  If th  square is already occupied put the deep_copy and the exception chain  in the UpdateResult
                sent to the client.
            3.  If the token is either
                    *   Disabled.
                    *   Not certified safe.
                    *   Belongs to a different board.
                    *   unformed but want to start from the wrong square.
                put deep_copy and the exception chain in the UpdateResult sent to the client.
            4.  Configure the square side of the square-token binding.
            5.  Configure the token side of the square-token binding.
            6.  Send deep_copy and the current square in the success result.
        Args:
            token: Token
            square: Square
            token_service: TokenService
            square_service: SquareService
            
       Returns:
            UpdateResult[Square]
            
        Raises:
            TokenVisitHandlerException
            StartSquareVisitException
            VisitingOccupiedSquareException
            VisitorFromWrongBoardException
            SquareVisitorDisabledException
        """
        method = "SquareService.add_occupant"
        
        # Handle the case that, the item is not certified safe.
        square_validation = square_service.validator.validate(candidate=square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=StartSquareVisitException(
                        mthd=method,
                        op=StartSquareVisitException.OP,
                        msg=StartSquareVisitException.MSG,
                        err_code=StartSquareVisitException.ERR_CODE,
                        rslt_type=StartSquareVisitException.RSLT_TYPE,
                        ex=square_validation.exception,
                    )
                )
            )
        # --- Make a deep copy of the square for the original field, after its validated. ---#
        pre_update_square = deepcopy(square)
        
        # Handle the case that, the square is already occupied.
        if square.is_occupied:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=StartSquareVisitException(
                        mthd=method,
                        op=StartSquareVisitException.OP,
                        msg=StartSquareVisitException.MSG,
                        err_code=StartSquareVisitException.ERR_CODE,
                        rslt_type=StartSquareVisitException.RSLT_TYPE,
                        ex=VisitingOccupiedSquareException(
                            val=square,
                            var=f"{square.name}",
                            err_code=VisitingOccupiedSquareException.ERR_CODE,
                            msg=f"{square.name} is already occupied by {square.occupant.designation}."
                        ),
                    )
                )
            )
        # Handle the case that, the token is not certified safe.
        token_validation = token_service.validator.validate(candidate=token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=StartSquareVisitException(
                        mthd=method,
                        op=StartSquareVisitException.OP,
                        msg=StartSquareVisitException.MSG,
                        err_code=StartSquareVisitException.ERR_CODE,
                        rslt_type=StartSquareVisitException.RSLT_TYPE,
                        ex=token_validation.exception,
                    )
                )
            )
        # Handle the case that, the token belongs to a different board
        if token.team.board != square.board:
            square_board_id = square.board.id
            token_board_id = token.team.board.id
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=StartSquareVisitException(
                        mthd=method,
                        op=StartSquareVisitException.OP,
                        msg=StartSquareVisitException.MSG,
                        err_code=StartSquareVisitException.ERR_CODE,
                        rslt_type=StartSquareVisitException.RSLT_TYPE,
                        ex=VisitorFromWrongBoardException(
                            val=token,
                            var=f"{token.designation}",
                            err_code=VisitorFromWrongBoardException.ERR_CODE,
                            msg=f"{token.designation} belongs to board {token_board_id}. "
                                f"Square {square.name} belongs to board {square_board_id}."
                        )
                    )
                )
            )
        # Handle the case that, the occupant is disabled
        if token.is_disabled:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=TokenVisitHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=StartSquareVisitException(
                        mthd=method,
                        op=StartSquareVisitException.OP,
                        msg=StartSquareVisitException.MSG,
                        err_code=StartSquareVisitException.ERR_CODE,
                        rslt_type=StartSquareVisitException.RSLT_TYPE,
                        ex=SquareVisitorDisabledException(
                            val=token,
                            var=f"{token.designation}",
                            msg=SquareVisitorDisabledException.MSG,
                            err_code=SquareVisitorDisabledException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, an unformed token is trying to start from the wrong square.
        if token.is_not_deployed:
            validate_token_opening_square_result = cls._verify_token_opens_from_square(
                square=square,
                token=token
            )
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=TokenVisitHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=StartSquareVisitException(
                        mthd=method,
                        op=StartSquareVisitException.OP,
                        msg=StartSquareVisitException.MSG,
                        err_code=StartSquareVisitException.ERR_CODE,
                        rslt_type=StartSquareVisitException.RSLT_TYPE,
                        ex=validate_token_opening_square_result.exception
                    )
                )
            )
        # --- Integrity and consistency checks are passed. Start the visit. ---#
        
        # Set the square side of the relationship.
        square.occupant = token
        square.state = SquareState.OCCUPIED
        
        # Set the token side of the relationship.
        token.positions.push(square.coord)
        if token.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            token.board_state = TokenBoardState.DEPLOYED_ON_BOARD
        
        # --- Send the update success result to the client. ---#
        return UpdateResult.update_success(original=pre_update_square, updated=square)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def terminate_visit(
            cls,
            square: Square,
            square_service: SquareService = SquareService(),
    ) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the square fails its safety checks send and exception chain in the DeletionResult.
            2.  If the square is empty send an exception chain in the DeletionResult.
            3.  Store the square's occupant in a temp variable.
            4.  Set square.occupant to null and  square.state to empty.

        Args:
            square: Square
            square_service: SquareService
        Returns:
            DeletionResult[Token]
        Raises:
            TokenVisitHandlerException
            TerminateSquareVisitException
            NoVisitForTerminationException
        """
        method = "TokenVistHandler.terminate_visit"
        
        # Handle the case that, the square is not certified as safe.
        validation = square_service.validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenVisitHandlerException(
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=TerminateSquareVisitException(
                        mthd=method,
                        op=TerminateSquareVisitException.OP,
                        msg=TerminateSquareVisitException.MSG,
                        err_code=TerminateSquareVisitException.ERR_CODE,
                        rslt_type=TerminateSquareVisitException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            )
        # Handle the case that, the square is empty.
        if square.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenVisitHandlerException(
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=TerminateSquareVisitException(
                        mthd=method,
                        op=TerminateSquareVisitException.OP,
                        msg=TerminateSquareVisitException.MSG,
                        err_code=TerminateSquareVisitException.ERR_CODE,
                        rslt_type=TerminateSquareVisitException.RSLT_TYPE,
                        ex=NoVisitForTerminationException(
                            val=square,
                            var=f"{square.name}",
                            msg=NoVisitForTerminationException.MSG,
                            err_code=NoVisitForTerminationException.ERR_CODE,
                        )
                    )
                )
            )
        # --- Process the removal logic that maintains integrity and consistency. ---#
        
        # Store the square's occupant.
        token = square.occupant
        
        # Break the relationship between the square and the token then update the square's state.
        square.occupant = None
        square.state = SquareState.EMPTY
        
        # --- Send the success result to the client. ---#
        DeletionResult.success(payload=token)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _verify_token_opens_from_square(
            cls,
            target: Square,
            visitor: Token
    ) -> ValidationResult[Square]:
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
            VisitingWrongOpeningSquareException
        """
        method = "TokenVisitHandler._verify_token_forms_on_square"
        
        # Handle the case that, the occupant belongs to a different square.
        if target.name.upper() != visitor.opening_square_name.upper():
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenVisitHandlerException(
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=StartSquareVisitException(
                        mthd=method,
                        op=StartSquareVisitException.OP,
                        msg=StartSquareVisitException.MSG,
                        err_code=StartSquareVisitException.ERR_CODE,
                        rslt_type=StartSquareVisitException.RSLT_TYPE,
                        ex=VisitingWrongOpeningSquareException(
                            val=visitor,
                            var=f"{visitor.designation}",
                            err_code=VisitingWrongOpeningSquareException.ERR_CODE,
                            msg=f"{target.name} does not match "
                                f"{visitor.designation}.opening_square={visitor.opening_square_name}:"
                        )
                    )
                )
            )
        # --- Send the success result to the caller. ---#
        return ValidationResult.success(payload=target)

