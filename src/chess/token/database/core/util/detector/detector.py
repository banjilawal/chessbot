# src/chess/token/database/core/util/detector/detector.py

"""
Module: chess.token.database.core.util.detector.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations


from typing import List

from chess.system import CollisionDetector, CollisionReport, LoggingLevelRouter

from chess.token import Token, TokenDesignationAlreadyInUseException, TokenIdAlreadyInUseException, TokenValidator
from chess.token.database.core.util.detector.exception.wrapper import TokenCollisionDetectionException


class TokenCollisionDetector(CollisionDetector[Token]):
    
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
            1.  If any stack members share either an id, designation or opening square with the target send and
                exception in the SearchResult. Those three properties must be unique within the game.
            2.  If no matches are found send an empty SearchResult indicating there were no collisions.
        # PARAMETERS:
            *   target (Token)
            *   dataset (List[Token])
        # RETURNS:
            *   CollisionReport[Token] containing either:
                    - On failure: Exception or non-empty list.
                    - On Collision: Token, Token
                    - On no collisions: Token
        # RAISES:
            *  TokenIdAlreadyInUseException
            *  TokenDesignationAlreadyInUseException
            *   TokenOpeningSquareAlreadyInUseException
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
                        ex=TokenIdAlreadyInUseException(
                            f"{method}: {TokenIdAlreadyInUseException.DEFAULT_MESSAGE}",
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
                        ex=TokenDesignationAlreadyInUseException(
                            f"{method}: {TokenDesignationAlreadyInUseException.DEFAULT_MESSAGE}",
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
                        ex=TokenDesignationAlreadyInUseException(
                            f"{method}: {TokenDesignationAlreadyInUseException.DEFAULT_MESSAGE}",
                        )
                    )
                )
        # --- After the uniqueness tests are passed send the no_collisions report to the caller. ---#
        return CollisionReport.no_collision_detected(target=target)