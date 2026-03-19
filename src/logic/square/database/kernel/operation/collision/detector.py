# src/logic/square/square/service/collision/detection.py

"""
Module: logic.square.service.collision.detector
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.square import (
    Square, SquareCollisionDetectorFailureException, SquareCoordCollisionException, SquareIdCollisionException,
    SquareNameCollisionException
)
from logic.square.database.kernel import SquareStackService
from logic.system import CollisionAnalysis, CollisionReport, LoggingLevelRouter


class SquareCollisionAnalysis(CollisionAnalysis[Square]):
    """
     Role:
         - Collision Detection Worker
         - Consistency and Uniqueness Guarantor
         
     Responsibilities:
         1.  Report if any squares are sharing attributes which should be unique.
         
     Attributes:
     Provides:
         -   detect(
                    cls,
                    target: Square,
                    square_stack: SquareStackService,
            ) -> CollisionReport
            
     Super:
        -   CollisionAnalysis[T]
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            target: Square,
            square_stack: SquareStackService,
    ) -> CollisionReport[Square]:
        """
        Report if any stack member has the same id, name or
        coord as the target.
        
        Action:
            1.  Send only exception chain in the CollisionReport if:
                    *   The target is not certified as safe.
            2.  Otherwise, send:
                    *   The target.
                    *   The collider.
                    *   The exception indicating which unique property is shared.
        Args:
            target: Square
            square_stack: SquareStackService
        Returns:
               CollisionReport[Square]
        Raises:
            SquareIdCollisionException
            SquareNameCollisionException
            SquareCoordCollisionException
            SquareCollisionDetectorFailureException
        """
        method = f"{cls.__class__.__name__}.detect"
        
        # Handle the case that, the target is not certified as safe.
        validation_result = square_stack.integrity_service.validation.execute(
            candidate=target
        )
        if validation_result.is_failure:
            return CollisionReport.failure(
                exception=SquareCollisionDetectorFailureException(
                    val=method,
                    var="square failed integrity validation",
                    msg=SquareCollisionDetectorFailureException.MSG,
                    err_code=SquareCollisionDetectorFailureException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Loop through the collider_candidates to find matches. ---#
        
        for square in square_stack.items:
            # Handle the case that, the target shares its id with a collider_candidates member.
            if square.id == target.id:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_occurred(
                    var="id",
                    target=target,
                    collider=square,
                    val=f"{square.id}",
                    exception=SquareIdCollisionException(
                            var="id",
                            val=f"{square.id}",
                            msg=SquareIdCollisionException.MSG,
                            err_code=SquareIdCollisionException.ERR_CODE
                    )
                )
            # Handle the case that, the target shares its name with a collider_candidates member.
            if square.name.upper() == target.name.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_occurred(
                    var="name",
                    target=target,
                    collider=square,
                    val=f"{square.name}",
                    exception=SquareNameCollisionException(
                            var="name",
                            val=f"{square.name}",
                            msg=SquareNameCollisionException.MSG,
                            err_code=SquareNameCollisionException.ERR_CODE,
                    )
                )
            # Handle the case that, the target shares its coord with a collider_candidates member.
            if square.coord == target.coord:
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_occurred(
                    var="coord",
                    target=target,
                    collider=square,
                    val=f"{square.coord}",
                    exception=SquareCoordCollisionException(
                            var="coord",
                            val=f"{square.coord}",
                            msg=SquareCoordCollisionException.MSG,
                            err_code=SquareCoordCollisionException.ERR_CODE,
                    )
                )
        # --- Send the no collisions detected report. ---#
        return CollisionReport.no_collision()
    