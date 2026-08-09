# src/sensor/detector/collider/detector.py

"""
Module: sensor.detector.collider.detector
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from report import CollisionReport
from sensor import Collider
from stack import TokenStackService
from transit import TokenCarrier
from util import LoggingLevelRouter



class TokenCollider(Collider[TokenCarrier]):
    """
     Role:
         - Collision Detection Worker
         - Consistency and Uniqueness Guarantor
         
     Responsibilities:
         1.  Report if any tokens are sharing attributes which should be unique.
         
     Attributes:
     Provides:
         -   detect(
                    cls,
                    target: Token,
                    token_stack: TokenStackService,
            ) -> CollisionReport
            
     Super:
    """
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            attractor: TokenCarrier,
            stream: TokenStackService,
    ) -> CollisionReport:
        """
        Report if any schema member has the same id, designation or
        home_square_name as the target.
        
        Action:
            1.  Send only exception chain in the CollisionReport if:
                    *   The target does not pass a validation check.
            2.  Otherwise, send:
                    *   The target.
                    *   The collider.
                    *   The exception indicating which unique property is shared.
        Args:
            target: TokenBlueprint
            stream: TokenStackService
            identity_service: IdentityService
            priming_validator: PrimingValidator
        Returns:
               CollisionReport[Token]
        Raises:
            TokenIdCollisionException
            TokenDesignationCollisionException
            TokenOpeningSquareCollisionException
            TokenCollisionDetectionException
        """
        method = f"{self.__class__.__name__}.execute"
        # --- Loop through the collider_candidates to find matches. ---#
        
        for item in stream.items:
            # Handle the case that, a token already has the target's id.
            if item.id == attractor.entity.id:
                # Return the collision details in the report.
                return CollisionReport.collision(
                    collider=item,
                    target_set=attractor,
                    colliding_variable="id",
                    collision_value=item.id,
                    exception=TokenIdCollisionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenIdCollisionException.MSG,
                        err_code=TokenIdCollisionException.ERR_CODE,
                    )
                )
            # Handle the case that, a token already has the target's id.
            if item.name.upper() == attractor.entity.name.upper():
                # Return the collision details in the report.
                return CollisionReport.collision(
                    collider=item,
                    target_set=attractor,
                    colliding_variable="designation",
                    collision_value=item.name,
                    exception=TokenNameCollisionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenNameCollisionException.MSG,
                        err_code=TokenNameCollisionException.ERR_CODE,
                    )
                )
            # Handle the case that, the target shares its home_square_name with a collider_candidates member.
            if item.home_square.name.upper() == attractor.entity.formation.home_square_name.upper():
                # Return the collider, designation, and the exception.
                return CollisionReport.collision(
                    collider=item,
                    target_set=attractor,
                    colliding_variable="home_square",
                    collision_value=item.home_square,
                    exception=OpeningSquareCollisionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=OpeningSquareCollisionException.MSG,
                        err_code=OpeningSquareCollisionException.ERR_CODE,
                    )
                )
        # --- Send the no collisions detected report. ---#
        return CollisionReport.no_collisions(attractor)
    