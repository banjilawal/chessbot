# src/chess/square/database/core/util/detector/detector.py

"""
Module: chess.square.service.detector.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.system import CollisionDetector, CollisionReport, LoggingLevelRouter
from chess.square import (
    Square, SquareCollisionDetectionException, SquareDesignationCollisionException, SquareIdCollisionException,
    SquareOpeningSquareCollisionException, SquareValidator
)


class SquareCollisionDetector(CollisionDetector[Square]):
    """
    # ROLE: Detector, Consistency and Uniqueness Guarantor,

    # RESPONSIBILITIES:
    1.  Public facing collision detection microservice API.
    2.  Ensures consistency of Square datasets by enforcing uniqueness constraints.
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
            target: Square,
            dataset: List[Square],
            square_validator: SquareValidator = SquareValidator(),
    ) -> CollisionReport[Square]:
        """
        # ACTION:
            1.  If the target is not certified as safe, send both exception nd target in the CollisionReport.
            2.  Loop through the dataset to find id, designation or opening square matches. If any are found,
                send the: target, collider, and exception in the CollisionReport.
            3.  If no collisions were detected in the loop send the target back in in a no-collision report.
        # PARAMETERS:
            *   target (Square)
            *   dataset (List[Square])
            *   square_validator (SquareValidator)
        # RETURNS:
            *   CollisionReport[Square] containing either:
                    - On failure: Exception or non-empty list.
                    - On Collision: Square, Square
                    - On no collisions: Square
        # RAISES:
            *   SquareIdCollisionException
            *   SquareCollisionDetectionException
            *   SquareDesignationCollisionException
            *   SquareOpeningSquareCollisionException
        """
        method = "SquareCollisionDetector.detect"
        
        # Handle the case that the target is not certified as safe.
        validation_result = square_validator.validate(candidate=target)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return CollisionReport.detection_failure(
                target=target,
                exception=SquareCollisionDetectionException(
                    message=f"{method}: {SquareCollisionDetectionException.ERROR_CODE}",
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
                    exception=SquareCollisionDetectionException(
                        message=f"{method}: {SquareCollisionDetectionException.ERROR_CODE}",
                        ex=SquareIdCollisionException(
                            f"{method}: {SquareIdCollisionException.DEFAULT_MESSAGE}",
                        )
                    )
                )
            # Handle the case that, the target shares its designation with a dataset member.
            if member.designation.upper() == target.designation.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_detected(
                    target=target,
                    collider=member,
                    exception=SquareCollisionDetectionException(
                        message=f"{method}: {SquareCollisionDetectionException.ERROR_CODE}",
                        ex=SquareDesignationCollisionException(
                            f"{method}: {SquareDesignationCollisionException.DEFAULT_MESSAGE}",
                        )
                    )
                )
            # Handle the case that, the target shares its opening square with a dataset member.
            if member.opening_square_name.upper() == target.opening_square_name.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_detected(
                    target=target,
                    collider=member,
                    exception=SquareCollisionDetectionException(
                        message=f"{method}: {SquareCollisionDetectionException.ERROR_CODE}",
                        ex=SquareOpeningSquareCollisionException(
                            f"{method}: {SquareOpeningSquareCollisionException.DEFAULT_MESSAGE}",
                        )
                    )
                )
        # --- After the uniqueness tests are passed send the no_collisions report to the caller. ---#
        return CollisionReport.no_collision_detected(target=target)