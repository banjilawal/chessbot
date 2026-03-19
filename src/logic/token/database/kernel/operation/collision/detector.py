# src/logic/token/token/service/collision/detection.py

"""
Module: logic.token.service.collision.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.system import CollisionDetectionProcess, CollisionReport, LoggingLevelRouter
from logic.token import (
    Token, TokenCollisionDetectorFailureException, TokenDesignationCollisionException,
    TokenIdCollisionException, TokenOpeningSquareCollisionException, TokenStackService
)


class TokenCollisionDetectionProcess(CollisionDetectionProcess[Token]):
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
        -   CollisionDetectionProcess[T]
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            target: Token,
            token_stack: TokenStackService,
    ) -> CollisionReport[Token]:
        """
        Report if any stack member has the same id, designation or
        opening_square_name as the target.
        
        Action:
            1.  Send only exception chain in the CollisionReport if:
                    *   The target is not certified as safe.
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
            TokenCollisionDetectorFailureException
        """
        method = f"{cls.__class__.__name__}.detect"
        
        # Handle the case that, the target is not certified as safe.
        validation_result = token_stack.integrity_service.validator.execute(
            candidate=target
        )
        if validation_result.is_failure:
            return CollisionReport.failure(
                exception=TokenCollisionDetectorFailureException(
                    val=method,
                    var="token failed integrity validation",
                    msg=TokenCollisionDetectorFailureException.MSG,
                    err_code=TokenCollisionDetectorFailureException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Loop through the dataset to find matches. ---#
        
        for token in token_stack.items:
            # Handle the case that, the target shares its id with a dataset member.
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
            # Handle the case that, the target shares its designation with a dataset member.
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
            # Handle the case that, the target shares its opening_square_name with a dataset member.
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
    