# src/logic/token/token/service/collision/detector.py

"""
Module: logic.token.service.collision.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.system import CollisionDetector, CollisionReport, LoggingLevelRouter
from logic.token import (
    Token, TokenColliderException, TokenIdCollisionException, TokenDesignationCollisionException,
    TokenOpeningSquareCollisionException, TokenStackService
)

class TokenCollisionDetector(CollisionDetector[Token]):
    """
    # ROLE: Detector, Consistency and Uniqueness Guarantor, Validation,

    # RESPONSIBILITIES:
    1.  Public facing collision detection microservice API.
    2.  Validates Tokens before they are inserted into the Token dataset.
    2.  Ensures consistency of Token datasets by enforcing uniqueness constraints.
    3.  Sends report indicating target, collider and which attribute caused the collision.

    # PARENT:
        *   CollisionDetector

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See CollisionDetector class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
    None

    # LOCAL METHODS:
    None
    
    # INHERITED METHODS:
        *   See CollisionDetector class for inherited methods.
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def detect(
            cls,
            target: Token,
            token_stack: TokenStackService,
    ) -> CollisionReport[Token]:
        """
        Args:
            1.  If the target is not certified as safe send a detector_failure result.
            2.  If the target collides with any stack member over
                    *   An id
                    *   A designation
                    *   An opening square
                Send a collision_detected result.
            3.  Otherwise, send a no_collisions result.
            
        Args:
            target: Token
            token_stack: TokenStackService
            
        Returns:
               CollisionReport[Token]
               
        Raises:
            TokenIdCollisionException
            TokenColliderException
            TokenDesignationCollisionException
            TokenOpeningSquareCollisionException
        """
        method = "TokenCollisionDetector.detect"
        
        # Handle the case that, the target is not certified as safe.
        validation_result = token_stack.integrity_service.validator.validate(
            candidate=target
        )
        if validation_result.is_failure:
            return CollisionReport.detector_failure(
                exception=TokenColliderException(
                    mthd=method,
                    op=TokenColliderException.OP,
                    msg=TokenColliderException.MSG,
                    err_code=TokenColliderException.ERR_CODE,
                    rslt_type=TokenColliderException.RSLT_TYPE,
                    ex=validation_result.exception
                )
            )
        # --- Loop through the dataset to find matches. ---#
        
        for token in token_stack.items:
            # Handle the case that, the target shares its id with a dataset member.
            if token.id == target.id:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision(
                    var="id",
                    target=target,
                    collider=token,
                    val=f"{token.id}",
                    exception=TokenColliderException(
                        mthd=method,
                        op=TokenColliderException.OP,
                        msg=TokenColliderException.MSG,
                        err_code=TokenColliderException.ERR_CODE,
                        rslt_type=TokenColliderException.RSLT_TYPE,
                        ex=TokenIdCollisionException(
                            var="id",
                            val=f"{token.id}",
                            msg=TokenIdCollisionException.MSG,
                            err_code=TokenIdCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, the target shares its designation with a dataset member.
            if token.designation.upper() == target.designation.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision(
                    var="designation",
                    target=target,
                    collider=token,
                    val=f"{token.designation}",
                    exception=TokenColliderException(
                        mthd=method,
                        op=TokenColliderException.OP,
                        msg=TokenColliderException.MSG,
                        err_code=TokenColliderException.ERR_CODE,
                        rslt_type=TokenColliderException.RSLT_TYPE,
                        ex=TokenDesignationCollisionException(
                            var="designation",
                            val=f"{token.designation}",
                            msg=TokenDesignationCollisionException.MSG,
                            err_code=TokenDesignationCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, the target shares its opening_square_name with a dataset member.
            if token.opening_square_name.upper()== target.opening_square_name.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision(
                    var="opening_square_name",
                    target=target,
                    collider=token,
                    val=f"{token.opening_square_name}",
                    exception=TokenColliderException(
                        mthd=method,
                        op=TokenColliderException.OP,
                        msg=TokenColliderException.MSG,
                        err_code=TokenColliderException.ERR_CODE,
                        rslt_type=TokenColliderException.RSLT_TYPE,
                        ex=TokenOpeningSquareCollisionException(
                            var="opening_square_name",
                            val=f"{token.opening_square_name}",
                            msg=TokenOpeningSquareCollisionException.MSG,
                            err_code=TokenOpeningSquareCollisionException.ERR_CODE,
                        )
                    )
                )
        # --- After the uniqueness tests are passed send the no_collisions report to the caller. ---#
        return CollisionReport.no_collision()
    