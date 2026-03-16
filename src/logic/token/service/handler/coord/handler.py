# src/logic/token/service/handler/coord/handler.py

"""
Module: logic.token.service.handler.coord.handler
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from logic.system import DeletionResult, InsertionResult, LoggingLevelRouter
from logic.coord import (
    Coord, CoordService, DuplicateCoordPushException, PoppingCoordException, PushingCoordException
)
from logic.token import (
    InactiveTokenPoppingCoordException, InactiveTokenPushingCoordException, MoveUndoLimitException, Token,
    TokenCoordHandlerException, TokenValidator,  UnopenedTokenPoppingCoordException
)

class TokenCoordHandler:
    """
    # ROLE: Update Handler, Consistency, Integrity Maintenance, Lifecycle Management

    # RESPONSIBILITIES:
    1.  Ensure integrity and consistency are maintained during the pawn's promotion lifecycle.

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
    def undo_current_token_positon(
            cls,
            token: Token,
            token_validator: TokenValidator = TokenValidator(),
    ) -> DeletionResult[Coord]:
        """
        # ACTION:
            1.  If the token fails validation returns the exception in the DeletionResult.
            2.  If the token has not been activated with an opening item return the exception in the DeletionResult.
            3.  If the token has an empty coord stack return the exception in the DeletionResult.
            4.  If a new coord has not been pushed since the last undo send and exception in the DeletionResult.
                Else, forward the results of token.positions.pop_coord() to the caller.

        Args:
            token: Token
            token_validator: TokenValidator

        Returns:
            DeletionResult[Coord]

        Raises:
            PoppingCoordException
            MoveUndoLimitException
            TokenCoordHandlerException
            PoppingEmtpyCoordStackException
            InactiveTokenPoppingCoordException
            UnopenedTokenPoppingCoordException
        """
        method = f"{cls.__class__.__name__}undo_last_coord_push"
        
        # Handle the case that, the token is not certified as safe.
        validation_result = token_validator.validate(token)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=PoppingCoordException(
                        mthd=method,
                        op=PoppingCoordException.OP,
                        msg=PoppingCoordException.MSG,
                        err_code=PoppingCoordException.ERR_CODE,
                        rslt_type=PoppingCoordException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            )
        # Handle the case that, token is not active
        if not token.is_active:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=PoppingCoordException(
                        mthd=method,
                        op=PoppingCoordException.OP,
                        msg=PoppingCoordException.MSG,
                        err_code=PoppingCoordException.ERR_CODE,
                        rslt_type=PoppingCoordException.RSLT_TYPE,
                        ex=InactiveTokenPoppingCoordException(
                            var="token",
                            val=token.designation,
                            msg=InactiveTokenPoppingCoordException.MSG,
                            err_code=InactiveTokenPoppingCoordException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, the active token has not opened.
        if token.positions.size == 1:
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return DeletionResult.failure(
                    TokenCoordHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=TokenCoordHandlerException.MSG,
                        err_code=TokenCoordHandlerException.ERR_CODE,
                        ex=PoppingCoordException(
                            mthd=method,
                            op=PoppingCoordException.OP,
                            msg=PoppingCoordException.MSG,
                            err_code=PoppingCoordException.ERR_CODE,
                            rslt_type=PoppingCoordException.RSLT_TYPE,
                            ex=UnopenedTokenPoppingCoordException(
                                var="token",
                                val=token.designation,
                                msg=UnopenedTokenPoppingCoordException.MSG,
                                err_code=UnopenedTokenPoppingCoordException.ERR_CODE,
                            )
                        )
                    )
                )
        # Handle the case that, an attempt is made to undo more than one turn.
        if token.previous_coord == token.current_position:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=PoppingCoordException(
                        mthd=method,
                        op=PoppingCoordException.OP,
                        msg=PoppingCoordException.MSG,
                        err_code=PoppingCoordException.ERR_CODE,
                        rslt_type=PoppingCoordException.RSLT_TYPE,
                        ex=MoveUndoLimitException(
                            var=token.designation,
                            msg=MoveUndoLimitException.MSG,
                            err_code=MoveUndoLimitException.ERR_CODE,
                        )
                    )
                )
            )
        popping_cord_stack_result = token.positions.pop()
        
        # Handle the case that, the pop was not completed.
        if popping_cord_stack_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=PoppingCoordException(
                        mthd=method,
                        op=PoppingCoordException.OP,
                        msg=PoppingCoordException.MSG,
                        err_code=PoppingCoordException.ERR_CODE,
                        rslt_type=PoppingCoordException.RSLT_TYPE,
                        ex=popping_cord_stack_result.exception
                    )
                )
            )
        return popping_cord_stack_result
        
    @classmethod
    @LoggingLevelRouter.monitor
    def push_coord(
            cls,
            token: Token,
            coord: Coord,
            coord_service: CoordService = CoordService(),
            token_validator: TokenValidator = TokenValidator(),
    ) -> InsertionResult:
        """
        Action:
            1.  If the token or coord fail their validations return the exception in the InsertionResult.
            2.  If the position is already the updated position return the exception in the InsertionResult.
            3.  If the pushing the position to the token's coord stack fails encapsulate the exception then
                send the exception chain in the InsertionResult.'

        Args:
            coord: Coord
            token: Token
            coord_service: CoordService
            token_validator: TokenValidator

        Returns:
            DeletionResult[Coord]

        Raises:
            TokenServiceException
            OverMoveUndoLimitException
            TokenOpeningSquareNotFoundException
            PoppingEmtpyCoordStackException
        """
        method = "TokenService.push_coord_to_token"
        
        # Handle the case that, the token is not certified as safe.
        token_validation_result = token_validator.validate(token)
        if token_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=PushingCoordException(
                        mthd=method,
                        op=PushingCoordException.OP,
                        msg=PushingCoordException.MSG,
                        err_code=PushingCoordException.ERR_CODE,
                        rslt_type=PushingCoordException.RSLT_TYPE,
                        ex=token_validation_result.exception
                    )
                )
            )
        # Handle the case that, token is not active
        if not token.is_active:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=PushingCoordException(
                        mthd=method,
                        op=PushingCoordException.OP,
                        msg=PushingCoordException.MSG,
                        err_code=PushingCoordException.ERR_CODE,
                        rslt_type=PushingCoordException.RSLT_TYPE,
                        ex=InactiveTokenPushingCoordException(
                            var="token",
                            val=token.designation,
                            msg=InactiveTokenPushingCoordException.MSG,
                            err_code=InactiveTokenPushingCoordException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, the coord is not certified as safe.
        coord_validation_result = coord_service.validator.validate(coord)
        if coord_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=PushingCoordException(
                        mthd=method,
                        op=PushingCoordException.OP,
                        msg=PushingCoordException.MSG,
                        err_code=PushingCoordException.ERR_CODE,
                        rslt_type=PushingCoordException.RSLT_TYPE,
                        ex=coord_validation_result.exception
                    )
                )
            )
        # Handle the case that, the token is already at the destination coord.
        if token.current_position == coord:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=PushingCoordException(
                        mthd=method,
                        op=PushingCoordException.OP,
                        msg=PushingCoordException.MSG,
                        err_code=PushingCoordException.ERR_CODE,
                        rslt_type=PushingCoordException.RSLT_TYPE,
                        ex=DuplicateCoordPushException(
                            var=token.designation,
                            val=token.current_position,
                            msg=DuplicateCoordPushException.MSG,
                            err_code=DuplicateCoordPushException.ERR_CODE,
                        )
                    )
                )
            )
        pre_insertion_top_coord = token.current_position
        coord_insertion_result = token.positions.push(coord)
        
        # Handle the case that, the cord push was not completed.
        if coord_insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=PushingCoordException(
                        mthd=method,
                        op=PushingCoordException.OP,
                        msg=PushingCoordException.MSG,
                        err_code=PushingCoordException.ERR_CODE,
                        rslt_type=PushingCoordException.RSLT_TYPE,
                        ex=coord_insertion_result.exception
                    )
                )
            )
        # Update the token's previous position marker.
        token.previous_position = pre_insertion_top_coord
        return coord_insertion_result
