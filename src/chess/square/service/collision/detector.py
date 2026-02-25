# src/chess/square/square/service/collision/detector.py

"""
Module: chess.square.service.collision.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.board import Board
from chess.coord import Coord
from chess.system import CollisionDetector, CollisionReport, LoggingLevelRouter, ValidationResult
from chess.square import (
    Square, SquareCollisionDetectionException, SquareContext, SquareCoordCollisionException, SquareIdCollisionException,
    SquareNameCollisionException, SquareValidator
)

class SquareCollisionDetector(CollisionDetector[Square]):
    """
    # ROLE: Detector, Consistency and Uniqueness Guarantor, Validation,

    # RESPONSIBILITIES:
    1.  Public facing collision detection microservice API.
    2.  Validates Squares before they are inserted into the Square dataset.
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

    # CONSTRUCTOR PARAMETERS:
        Local:
        None
        Inherited:
        None

    # LOCAL METHODS:
        *   detect(
                target: Square,
                dataset: List[Square],
                square_validator: SquareValidator = SquareValidator()
            ) -> CollisionReport[Square]
            
        *   detect_attribute_collisions(id: int, name: str, coord: Coord, board: Board) -> ValidationResult[int]

    # INHERITED METHODS:
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
            3.  If no collisions were detected in the loop send the target back in a no-collision report.
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
            *   SquareNameCollisionException
            *   SquareCoordCollisionException
        """
        method = "SquareCollisionDetector.detect"
        
        # Handle the case that, the target is not certified as safe.
        validation_result = square_validator.validate(candidate=target)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return CollisionReport.detection_failure(
                target=target,
                exception=SquareCollisionDetectionException(
                    msg=f"{method}: {SquareCollisionDetectionException.ERR_CODE}",
                    ex=validation_result.exception,
                )
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
                        msg=f"{method}: {SquareCollisionDetectionException.ERR_CODE}",
                        ex=SquareIdCollisionException(
                            f"{method}: {SquareIdCollisionException.MSG}",
                        )
                    )
                )
            # Handle the case that, the target shares its name with a dataset member.
            if member.name.upper() == target.name.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_detected(
                    target=target,
                    collider=member,
                    exception=SquareCollisionDetectionException(
                        msg=f"{method}: {SquareCollisionDetectionException.ERR_CODE}",
                        ex=SquareNameCollisionException(
                            f"{method}: {SquareNameCollisionException.MSG}",
                        )
                    )
                )
            # Handle the case that, the target shares its coord with a dataset member.
            if member.coord == target.coord:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_detected(
                    target=target,
                    collider=member,
                    exception=SquareCollisionDetectionException(
                        msg=f"{method}: {SquareCollisionDetectionException.ERR_CODE}",
                        ex=SquareCoordCollisionException(
                            f"{method}: {SquareCoordCollisionException.MSG}",
                        )
                    )
                )
        # --- After the uniqueness tests are passed send the no_collisions report to the caller. ---#
        return CollisionReport.no_collision_detected(target=target)
    
    @classmethod
    def detect_attribute_collisions(cls, id: int, name: str, coord: Coord, board: Board) -> ValidationResult[int]:
        method = "SquareCollisionDetector.detect_attribute_collisions"
        
        # --- Run the id search. ---#
        id_search_result = board.squares.search(context=SquareContext(id=id))
        
        # Handle the case that, the id search was aborted.
        if id_search_result.is_failure:
            return ValidationResult.failure(id_search_result.exception)
        # Handle the case that, the id has already been assigned to a different square.
        if id_search_result.is_success:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareIdCollisionException(msg=f"{method}:{SquareIdCollisionException.MSG}",)
            )
        # --- Run the name search. ---#
        name_search_result = board.squares.search(context=SquareContext(name=name))
        
        # Handle the case that, the name search was aborted.
        if name_search_result.is_failure:
            return ValidationResult.failure(name_search_result.exception)
        # Handle the case that, the name has already been assigned to a different square.
        if name_search_result.is_success:
            return ValidationResult.failure(
                SquareNameCollisionException(msg=f"{method}:{SquareNameCollisionException.MSG}", )
            )
        # --- Run the coord search. ---#
        coord_search_result = board.squares.search(context=SquareContext(coord=coord))
        
        # Handle the case that, the coord search was aborted.
        if coord_search_result.is_failure:
            return ValidationResult.failure(coord_search_result.exception)
        # Handle the case that, the id has already been assigned to a different square.
        if coord_search_result.is_success:
            # Handle the case that, the coord has already been assigned to a different square.
            if coord_search_result.is_success:
                return ValidationResult.failure(
                    SquareCoordCollisionException(msg=f"{method}:{SquareCoordCollisionException.MSG}", )
                )
        # --- Send the success result indicating no attribute conditions. ---#
        return ValidationResult.success(3)
    