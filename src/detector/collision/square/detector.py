# src/detector/collision/square/detector.py

"""
Module: detector.collision.square.detector
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from blueprint import SquareBlueprint
from detection import Detector
from err import (
    SquareCollisionDetectorException, SquareCoordCollisionException, SquareIdCollisionException,
    SquareNameCollisionException
)
from model import Square
from report import CollisionReport
from result import AnalysisResult
from stack import SquareStackService
from util import LoggingLevelRouter


class SquareCollisionDetector(Detector[Square]):
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
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            attractor: SquareBlueprint,
            stream: SquareStackService,
    ) -> AnalysisResult[CollisionReport]:
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
        method = f"{cls.__class__.__name__}.detect"
        
        # Handle the case that, the target does not pass a validation check.
        validation_result = stream.microservice.run.build(attractor)
        if validation_result.is_failure:
            return AnalysisResult.failure(
                SquareCollisionDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=SquareCollisionDetectorException.MSG,
                    err_code=SquareCollisionDetectorException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Loop through the collider_candidates to find matches. ---#
        
        for square in stream.items:
            # Handle the case that, a candidate already has the target's id.
            if square.id == attractor.id:
                # Return the collision details in the report.
                return AnalysisResult.completed(
                    CollisionReport.collision(
                        target_set=attractor,
                        collider=square,
                        colliding_variable=f"id",
                        collision_value=attractor.id,
                        exception=SquareIdCollisionException(
                            cls_mthd=method,
                            cls_name=cls.__class__.__name__,
                            msg=SquareIdCollisionException.MSG,
                            err_code=SquareIdCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, a candidate already has the target's name.
            if square.name.upper() == attractor.name.upper():
                # Return the collision details in the report.
                return AnalysisResult.completed(
                    CollisionReport.collision(
                        target_set=attractor,
                        collider=square,
                        colliding_variable=f"name",
                        collision_value=attractor.name,
                        exception=SquareNameCollisionException(
                            cls_mthd=method,
                            cls_name=cls.__class__.__name__,
                            msg=SquareNameCollisionException.MSG,
                            err_code=SquareNameCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, a candidate already has the target's coord.
            if square.coord == attractor.coord:
                # Return the collision details in the report.
                return AnalysisResult.completed(
                    CollisionReport.collision(
                        target_set=attractor,
                        collider=square,
                        colliding_variable=f"coord",
                        collision_value=attractor.coord,
                        exception=SquareCoordCollisionException(
                            cls_mthd=method,
                            cls_name=cls.__class__.__name__,
                            msg=SquareCoordCollisionException.MSG,
                            err_code=SquareCoordCollisionException.ERR_CODE,
                        )
                    )
                )
        # --- Send the no collisions detected report. ---#
        return AnalysisResult.completed(CollisionReport.no_collisions(attractor))
    