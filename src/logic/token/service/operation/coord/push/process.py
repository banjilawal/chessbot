# src/logic/token/service/operation/coord/handler.py

"""
Module: logic.token.service.operation.coord.handler
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import Coord
from logic.system import DeletionResult, LoggingLevelRouter
from logic.token import Token, TokenValidator


class TokenPushCoordProcess:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Maintain the token's integrity and consistency when a coord is pushed
            onto its positions stack.
        2.  Enforce chess constraints on coord pushes.

    Attributes:

    Provides:
            -   execute(
                        cls,
                        token: Token,
                        coord: Coord,
                        coord_service: CoordService = CoordService(),
                        token_validator: TokenValidator = TokenValidator(),
                ) -> InsertionResult
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_validator: TokenValidator = TokenValidator(),
    ) -> DeletionResult[Coord]:
        """
        Forwards a request that the CoordDatabase instance removed its latest insert.

        Action:
            1.  Send an exception chain in the DeletionResult if:
                    *   The token is unsafe or not actionable.
                    *   It has no position history.
                    *   It has not moved from its opening square.
            2.  Otherwise, pop the last move and send the success result.
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
        # --- Integrity are passed. Request that, the CoordDatabase instance pop the last record. ---#
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
        # --- Forward the work product to the client. ---#
        return popping_cord_stack_result
