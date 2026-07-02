# src/logic/token/service/operation/coord/exception.py

"""
Module: logic.token.service.operation.coord.operation
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import Coord, CoordService, DuplicateCoordPushException
from system import InsertionResult, LoggingLevelRouter
from model.token import InactiveTokenPushingCoordException, Token, TokenPushCoordException, TokenValidation


class TokenPushCoordProcess:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Maintain the token's integrity and consistency when a coord is pushed
            onto its positions schema.
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
            coord: Coord,
            coord_service: CoordService = CoordService(),
            token_validator: TokenValidation = TokenValidation(),
    ) -> InsertionResult:
        """
        Forwards a request that the CoordDatabase insert  a new record.

        Action:
            1.  Send an exception chain in the InsertionResult if:
                    *   Either the token or the coord are not certified as safe.
                    *   The token is already at the coord.
                    *   The CoordDatabase does not complete the insertion.
            2.  Otherwise, send the success result.
        Args:
            coord: Coord
            token: Token
            coord_service: CoordService
            token_validator: TokenValidator
        Returns:
            InsertionResult[bool]
        Raises:
            TokenPushCoordException
            InactiveTokenPushingCoordException
            DuplicateCoordPushException
        """
        method = "TokenService.execute_to_token"
        
        # Handle the case that, the token does not pass a validation check.
        token_validation_result = token_validator.execute(token)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                TokenPushCoordException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenPushCoordException.OP,
                    msg=TokenPushCoordException.MSG,
                    err_code=TokenPushCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPushCoordException.MTHD_RSLT,
                    ex=token_validation_result.exception
                )
            )
        # Handle the case that, token is not active
        if not token.is_active:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                TokenPushCoordException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenPushCoordException.OP,
                    msg=TokenPushCoordException.MSG,
                    err_code=TokenPushCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPushCoordException.MTHD_RSLT,
                    ex=InactiveTokenPushingCoordException(
                        var="token",
                        val=token.designation,
                        msg=InactiveTokenPushingCoordException.MSG,
                        err_code=InactiveTokenPushingCoordException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the coord does not pass a validation check.
        coord_validation_result = coord_service.validator.execute(coord)
        if coord_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                TokenPushCoordException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenPushCoordException.OP,
                    msg=TokenPushCoordException.MSG,
                    err_code=TokenPushCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPushCoordException.MTHD_RSLT,
                    ex=coord_validation_result.exception
                )
            )
        # Handle the case that, the token is already at the destination coord.
        if token.current_position == coord:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                TokenPushCoordException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenPushCoordException.OP,
                    msg=TokenPushCoordException.MSG,
                    err_code=TokenPushCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPushCoordException.MTHD_RSLT,
                    ex=DuplicateCoordPushException(
                        var=token.designation,
                        val=token.current_position,
                        msg=DuplicateCoordPushException.MSG,
                        err_code=DuplicateCoordPushException.ERR_CODE,
                    )
                )
            )
        # --- Integrity tests are passed. Start the insertion tasks. ---#
        
        # Copy the top of the schema.
        pre_insertion_top_coord = token.current_position
        # Run the insertion request.
        coord_insertion_result = token.positions.push(coord)
        
        # Handle the case that, the request was not completed.
        if coord_insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                TokenPushCoordException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenPushCoordException.OP,
                    msg=TokenPushCoordException.MSG,
                    err_code=TokenPushCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPushCoordException.MTHD_RSLT,
                    ex=coord_insertion_result.exception,
                )
            )
        # Update the token's previous position marker.
        token.previous_position = pre_insertion_top_coord
        # --- Send the work product. ---#
        return coord_insertion_result
