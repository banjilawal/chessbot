# src/logic/square/square/service/collision/detector.py

"""
Module: logic.square.service.collision.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.system import CollisionDetector, CollisionDetectionResult, LoggingLevelRouter
from logic.square import (
    Square, SquareCollisionDetectionException, SquareCoordCollisionException, SquareIdCollisionException,
    SquareNameCollisionException, SquareStackService
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
            ) -> CollisionDetectionResult[Square]
            
        *   detect_attribute_collisions(id: int, name: str, coord: Coord, board: Board) -> ValidationResult[int]

    # INHERITED METHODS:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def detect(
            cls,
            target: Square,
            square_stack: SquareStackService,
    ) -> CollisionDetectionResult[Square]:
        """
        # ACTION:
            1.  If the target is not certified as safe, send both exception nd target in the CollisionDetectionResult.
            2.  Loop through the dataset to find id, designation or opening square matches. If any are found,
                send the: target, collider, and exception in the CollisionDetectionResult.
            3.  If no collisions were detected in the loop send the target back in a no-collision report.
        Args:
            target: Square
            square_stack: SquareStackService
            
        Returns:
               CollisionDetectionResult[Square]
               
        Raises:
            SquareIdCollisionException
            SquareCollisionDetectionException
            SquareNameCollisionException
            SquareCoordCollisionException
        """
        method = "SquareCollisionDetector.detect"
        
        # Handle the case that, the target is not certified as safe.
        validation_result = square_stack.integrity_service.validator.validate(
            candidate=target
        )
        if validation_result.is_failure:
            return CollisionDetectionResult.collision(
                exception=SquareCollisionDetectionException(
                    mthd=method,
                    op=SquareCollisionDetectionException.OP,
                    msg=SquareCollisionDetectionException.MSG,
                    err_code=SquareCollisionDetectionException.ERR_CODE,
                    rslt_type=SquareCollisionDetectionException.RSLT_TYPE,
                    ex=validation_result.exception
                )
            )
        # --- Loop through the dataset to find matches. ---#
        
        for square in square_stack.items:
            # Handle the case that, the target shares its id with a dataset member.
            if square.id == target.id:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionDetectionResult.collision(
                    var="id",
                    target=target,
                    collider=square,
                    val=f"{square.id}",
                    exception=SquareCollisionDetectionException(
                        mthd=method,
                        op=SquareCollisionDetectionException.OP,
                        msg=SquareCollisionDetectionException.MSG,
                        err_code=SquareCollisionDetectionException.ERR_CODE,
                        rslt_type=SquareCollisionDetectionException.RSLT_TYPE,
                        ex=SquareIdCollisionException(
                            var="id",
                            val=f"{square.id}",
                            msg=SquareIdCollisionException.MSG,
                            err_code=SquareIdCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, the target shares its name with a dataset member.
            if square.name.upper() == target.name.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionDetectionResult.collision(
                    var="name",
                    target=target,
                    collider=square,
                    val=f"{square.name}",
                    exception=SquareCollisionDetectionException(
                        mthd=method,
                        op=SquareCollisionDetectionException.OP,
                        msg=SquareCollisionDetectionException.MSG,
                        err_code=SquareCollisionDetectionException.ERR_CODE,
                        rslt_type=SquareCollisionDetectionException.RSLT_TYPE,
                        ex=SquareIdCollisionException(
                            var="name",
                            val=f"{square.name}",
                            msg=SquareNameCollisionException.MSG,
                            err_code=SquareNameCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, the target shares its coord with a dataset member.
            if square.coord == target.coord:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionDetectionResult.collision(
                    var="coord",
                    target=target,
                    collider=square,
                    val=f"{square.coord}",
                    exception=SquareCollisionDetectionException(
                        mthd=method,
                        op=SquareCollisionDetectionException.OP,
                        msg=SquareCollisionDetectionException.MSG,
                        err_code=SquareCollisionDetectionException.ERR_CODE,
                        rslt_type=SquareCollisionDetectionException.RSLT_TYPE,
                        ex=SquareCoordCollisionException(
                            var="name",
                            val=f"{square.name}",
                            msg=SquareCoordCollisionException.MSG,
                            err_code=SquareCoordCollisionException.ERR_CODE,
                        )
                    )
                )
        # --- After the uniqueness tests are passed send the no_collisions report to the caller. ---#
        return CollisionDetectionResult.no_collision()
    