# src/logic/token/token/service/collision/detection.py

"""
Module: logic.token.service.collision.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from system import CollisionAnalysis, CollisionReport, LoggingLevelRouter
from model.token import (
    Token, TokenCollisionDetectionException, TokenDesignationCollisionException,
    TokenIdCollisionException, TokenOpeningSquareCollisionException, TokenStackService
)


class TokenCollisionAnalysis(CollisionAnalysis[Token]):
    """
     Role:
         - Collision Detection Worker
         - Consistency and Uniqueness Guarantor
         
     Responsibilities:
         1.  Report if any tokens are sharing attributes which should be unique.
         
     Attributes:
     Provides:
         -   detect(
                    cls,
                    target: Token,
                    token_stack: TokenStackService,
            ) -> CollisionReport
            
     Super:
        -   CollisionAnalysis[T]
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            target: Token,
            token_stack: TokenStackService,
    ) -> CollisionReport[Token]:
        """
        Report if any schema member has the same id, designation or
        opening_square_name as the target.
        
        Action:
            1.  Send only exception chain in the CollisionReport if:
                    *   The target does not pass a validation check.
            2.  Otherwise, send:
                    *   The target.
                    *   The collider.
                    *   The exception indicating which unique property is shared.
        Args:
            target: Token
            token_stack: TokenStackService
        Returns:
               CollisionReport[Token]
        Raises:
            TokenIdCollisionException
            TokenDesignationCollisionException
            TokenOpeningSquareCollisionException
            TokenCollisionDetectionException
        """
        method = f"{cls.__class__.__name__}.detect"
        
        # Handle the case that, the target does not pass a validation check.
        validation_result = token_stack.service.validator.search_service(
            candidate=target
        )
        if validation_result.is_failure:
            return CollisionReport.failure(
                exception=TokenCollisionDetectionException(
                    val=method,
                    var="token failed integrity validation",
                    msg=TokenCollisionDetectionException.MSG,
                    err_code=TokenCollisionDetectionException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Loop through the collider_candidates to find matches. ---#
        
        for token in token_stack.items:
            # Handle the case that, the target shares its id with a collider_candidates member.
            if token.id == target.id:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_occurred(
                    var="id",
                    target=target,
                    collider=token,
                    val=f"{token.id}",
                    exception=TokenIdCollisionException(
                        var="id",
                        val=f"{token.id}",
                        msg=TokenIdCollisionException.MSG,
                        err_code=TokenIdCollisionException.ERR_CODE
                    )
                )
            # Handle the case that, the target shares its designation with a collider_candidates member.
            if token.designation.upper() == target.designation.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_occurred(
                    var="designation",
                    target=target,
                    collider=token,
                    val=f"{token.designation}",
                    exception=TokenDesignationCollisionException(
                        var="designation",
                        val=f"{token.designation}",
                        msg=TokenDesignationCollisionException.MSG,
                        err_code=TokenDesignationCollisionException.ERR_CODE,
                    )
                )
            # Handle the case that, the target shares its opening_square_name with a collider_candidates member.
            if token.opening_square_name.upper()== target.opening_square_name.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_occurred(
                    var="opening_square_name",
                    target=target,
                    collider=token,
                    val=f"{token.opening_square_name}",
                    exception=TokenOpeningSquareCollisionException(
                        var="opening_square_name",
                        val=f"{token.opening_square_name}",
                        msg=TokenOpeningSquareCollisionException.MSG,
                        err_code=TokenOpeningSquareCollisionException.ERR_CODE,
                    )
                )
        # --- Send the no collisions detected report. ---#
        return CollisionReport.no_collision()
    