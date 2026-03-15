# src/logic/token/token/service/collision/detector.py

"""
Module: logic.token.service.collision.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.system import CollisionDetector, CollisionDetectionResult, LoggingLevelRouter
from logic.token import (
    Token, TokenCollisionDetectionException, TokenCoordCollisionException, TokenIdCollisionException,
    TokenNameCollisionException, TokenStackService
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
   None

    # CONSTRUCTOR PARAMETERS:
        Local:
        None
        Inherited:
        None

    # LOCAL METHODS:
        *   detect(
                target: Token,
                dataset: List[Token],
                token_validator: TokenValidator = TokenValidator()
            ) -> CollisionDetectionResult[Token]
            
        *   detect_attribute_collisions(id: int, name: str, coord: Coord, board: Board) -> ValidationResult[int]

    # INHERITED METHODS:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def detect(
            cls,
            target: Token,
            token_stack: TokenStackService,
    ) -> CollisionDetectionResult[Token]:
        """
        # ACTION:
            1.  If the target is not certified as safe, send both exception nd target in the CollisionDetectionResult.
            2.  Loop through the dataset to find id, designation or opening token matches. If any are found,
                send the: target, collider, and exception in the CollisionDetectionResult.
            3.  If no collisions were detected in the loop send the target back in a no-collision report.
        Args:
            target: Token
            token_stack: TokenStackService
            
        Returns:
               CollisionDetectionResult[Token]
               
        Raises:
            TokenIdCollisionException
            TokenCollisionDetectionException
            TokenNameCollisionException
            TokenCoordCollisionException
        """
        method = "TokenCollisionDetector.detect"
        
        # Handle the case that, the target is not certified as safe.
        validation_result = token_stack.integrity_service.validator.validate(
            candidate=target
        )
        if validation_result.is_failure:
            return CollisionDetectionResult.collision(
                exception=TokenCollisionDetectionException(
                    mthd=method,
                    op=TokenCollisionDetectionException.OP,
                    msg=TokenCollisionDetectionException.MSG,
                    err_code=TokenCollisionDetectionException.ERR_CODE,
                    rslt_type=TokenCollisionDetectionException.RSLT_TYPE,
                    ex=validation_result.exception
                )
            )
        # --- Loop through the dataset to find matches. ---#
        
        for token in token_stack.items:
            # Handle the case that, the target shares its id with a dataset member.
            if token.id == target.id:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionDetectionResult.collision(
                    var="id",
                    target=target,
                    collider=token,
                    val=f"{token.id}",
                    exception=TokenCollisionDetectionException(
                        mthd=method,
                        op=TokenCollisionDetectionException.OP,
                        msg=TokenCollisionDetectionException.MSG,
                        err_code=TokenCollisionDetectionException.ERR_CODE,
                        rslt_type=TokenCollisionDetectionException.RSLT_TYPE,
                        ex=TokenIdCollisionException(
                            var="id",
                            val=f"{token.id}",
                            msg=TokenIdCollisionException.MSG,
                            err_code=TokenIdCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, the target shares its name with a dataset member.
            if token.name.upper() == target.name.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionDetectionResult.collision(
                    var="name",
                    target=target,
                    collider=token,
                    val=f"{token.name}",
                    exception=TokenCollisionDetectionException(
                        mthd=method,
                        op=TokenCollisionDetectionException.OP,
                        msg=TokenCollisionDetectionException.MSG,
                        err_code=TokenCollisionDetectionException.ERR_CODE,
                        rslt_type=TokenCollisionDetectionException.RSLT_TYPE,
                        ex=TokenIdCollisionException(
                            var="name",
                            val=f"{token.name}",
                            msg=TokenNameCollisionException.MSG,
                            err_code=TokenNameCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, the target shares its coord with a dataset member.
            if token.coord == target.coord:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionDetectionResult.collision(
                    var="coord",
                    target=target,
                    collider=token,
                    val=f"{token.coord}",
                    exception=TokenCollisionDetectionException(
                        mthd=method,
                        op=TokenCollisionDetectionException.OP,
                        msg=TokenCollisionDetectionException.MSG,
                        err_code=TokenCollisionDetectionException.ERR_CODE,
                        rslt_type=TokenCollisionDetectionException.RSLT_TYPE,
                        ex=TokenCoordCollisionException(
                            var="name",
                            val=f"{token.name}",
                            msg=TokenCoordCollisionException.MSG,
                            err_code=TokenCoordCollisionException.ERR_CODE,
                        )
                    )
                )
        # --- After the uniqueness tests are passed send the no_collisions report to the caller. ---#
        return CollisionDetectionResult.no_collision()
    