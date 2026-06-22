# src/detector/square/detector.py

"""
Module: detector.square.detector
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from detector import Detector
from err import SquareCollisionDetectorException
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
        -   CollisionAnalyst[T]
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            target: Square,
            square_stack: SquareStackService,
    ) -> AnalysisResult:
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
            target: Square
            square_stack: SquareStackService
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
        validation_result = square_stack.microservice.validator.validate(target)
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
        
        for square in square_stack.items:
            # Handle the case that, the target shares its id with a collider_candidates member.
            if square.id == target.id:
                # Return target, the collider, and the exception explaining the collision.
                return AnalysisResult.failure(
                    SquareCollisionDetectorException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=SquareCollisionDetectorException.MSG,
                        err_code=SquareCollisionDetectorException.ERR_CODE,
                        exception=SquareIdCollisionException(
                            var="id",
                            val=f"{square.id}",
                            msg=SquareIdCollisionException.MSG,
                            err_code=SquareIdCollisionException.ERR_CODE
                        )
                    )
                )
            # Handle the case that, the target shares its schema with a collider_candidates member.
            if square.designation.upper() == target.name.upper():
                # Return target, the collider, and the exception explaining the collision.
                return CollisionReport.collision_occurred(
                    var="schema",
                    target=target,
                    collider=square,
                    val=f"{square.designation}",
                    exception=SquareNameCollisionException(
                            var="schema",
                            val=f"{square.designation}",
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
    