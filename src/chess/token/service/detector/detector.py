# src/chess/token/database/core/util/detector/detector.py

"""
Module: chess.token.service.detector.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations


from typing import List

from chess.system import CollisionDetector, CollisionReport, LoggingLevelRouter
from chess.token import (
    Token, TokenCollisionDetectionException, TokenDesignationCollisionException, TokenIdCollisionException,
    TokenOpeningSquareCollisionException, TokenValidator
)


class TokenCollisionDetector(CollisionDetector[Token]):
    """
    # ROLE: Detector, Consistency and Uniqueness Guarantor,

    # RESPONSIBILITIES:
    1.  Public facing collision detection microservice API.
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
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def detect(
            cls,
            target: Token,
            dataset: List[Token],
            token_validator: TokenValidator = TokenValidator(),
    ) -> CollisionReport[Token]:
        """
        # ACTION:
            1.  If the target is not certified as safe, send both exception nd target in the CollisionReport.
            2.  Loop through the dataset to find id, designation or opening square matches. If any are found,
                send the: target, collider, and exception in the CollisionReport.
            3.  If no collisions were detected in the loop send the target back in in a no-collision report.
        # PARAMETERS:
            *   target (Token)
            *   dataset (List[Token])
            *   token_validator (TokenValidator)
        # RETURNS:
            *   CollisionReport[Token] containing either:
                    - On failure: Exception or non-empty list.
                    - On Collision: Token, Token
                    - On no collisions: Token
        # RAISES:
            *   TokenIdCollisionException
            *   TokenCollisionDetectionException
            *   TokenDesignationCollisionException
            *   TokenOpeningSquareCollisionException
        """
        method = "TokenCollisionDetector.detect"
        
        # Handle the case that the target is not certified as safe.
        validation_result = token_validator.validate(candidate=target)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return CollisionReport.detection_failure(
                target=target,
                exception=TokenCollisionDetectionException(
                    message=f"{method}: {TokenCollisionDetectionException.ERROR_CODE}",
                    ex=validation_result.exception,
                ),
            )
        
        # --- Loop through the dataset to find matches. ---#
        for member in dataset:
            
            # Handle the case that, the target shares its id with a dataset member.
            if member.id == target.id:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_detected(
                    target=target,
                    collider=member,
                    exception=TokenCollisionDetectionException(
                        message=f"{method}: {TokenCollisionDetectionException.ERROR_CODE}",
                        ex=TokenIdCollisionException(
                            f"{method}: {TokenIdCollisionException.DEFAULT_MESSAGE}",
                        )
                    )
                )
            # Handle the case that, the target shares its designation with a dataset member.
            if member.designation.upper() == target.designation.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_detected(
                    target=target,
                    collider=member,
                    exception=TokenCollisionDetectionException(
                        message=f"{method}: {TokenCollisionDetectionException.ERROR_CODE}",
                        ex=TokenDesignationCollisionException(
                            f"{method}: {TokenDesignationCollisionException.DEFAULT_MESSAGE}",
                        )
                    )
                )
            # Handle the case that, the target shares its opening square with a dataset member.
            if member.opening_square_name.upper() == target.opening_square_name.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_detected(
                    target=target,
                    collider=member,
                    exception=TokenCollisionDetectionException(
                        message=f"{method}: {TokenCollisionDetectionException.ERROR_CODE}",
                        ex=TokenOpeningSquareCollisionException(
                            f"{method}: {TokenOpeningSquareCollisionException.DEFAULT_MESSAGE}",
                        )
                    )
                )
        # --- After the uniqueness tests are passed send the no_collisions report to the caller. ---#
        return CollisionReport.no_collision_detected(target=target)