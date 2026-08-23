# src/sensor/detector/collider/square/detector.py

"""
Module: sensor.detector.collider.square.detector
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from report import CollisionReport
from result import AnalysisResult
from sensor import Collider
from collection.stack import SquareStackService
from transit.carrier import SquareCarrier
from util import LoggingLevelRouter


class SquareCollider(Collider[SquareCarrier]):
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
        -   Detector[T]
    """
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            attractor: SquareCarrier,
            stream: SquareStackService,
    ) -> CollisionReport:
        """
        Report if any schema member has the same id, schema or
        coord as the target.
        
        Action:
            1.  Send only exception chain in the CollisionReport if:
                    *   The target does not pass a validation check.
            2.  Otherwise, send:
                    *   The target.
                    *   The collider.
                    *   The exception indicating which unique property is shared.
        Args:
            attractor: SquareBlueprint
            stream: SquareStackService
        Returns:
               CollisionReport[Square]
        Raises:
            SquareIdCollisionException
            SquareNameCollisionException
            SquareCoordCollisionException
            SquareCollisionDetectorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the target does not pass a validation check.
        validation_result = stream.microservice.execute.execute(attractor)
        if validation_result.is_failure:
            return AnalysisResult.failure(
                SquareCollisionDetectorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCollisionDetectorException.MSG,
                    err_code=SquareCollisionDetectorException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Loop through the collider_candidates to find matches. ---#
        
        for square in stream.items:
            # Handle the case that, a candidate already has the target's id.
            if square.id == attractor.entity.id:
                # Return the collision details in the report.
                return CollisionReport.collision(
                    target_set=attractor,
                    collider=square,
                    colliding_variable=f"id",
                    collision_value=attractor.id,
                    exception=SquareIdCollisionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareIdCollisionException.MSG,
                        err_code=SquareIdCollisionException.ERR_CODE,
                    )
                )
            # Handle the case that, a candidate already has the target's name.
            if square.name.upper() == attractor.entity.name.upper():
                # Return the collision details in the report.
                return CollisionReport.collision(
                    target_set=attractor,
                    collider=square,
                    colliding_variable=f"name",
                    collision_value=attractor.name,
                    exception=SquareNameCollisionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareNameCollisionException.MSG,
                        err_code=SquareNameCollisionException.ERR_CODE,
                    )
                )
            # Handle the case that, a candidate already has the target's coord.
            if square.coord == attractor.entity.coord:
                # Return the collision details in the report.
                return CollisionReport.collision(
                    target_set=attractor,
                    collider=square,
                    colliding_variable=f"coord",
                    collision_value=attractor.coord,
                    exception=SquareCoordCollisionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCoordCollisionException.MSG,
                        err_code=SquareCoordCollisionException.ERR_CODE,
                    )
                )
        # --- Send the no collisions detected report. ---#
        return CollisionReport.no_collisions(attractor)
    