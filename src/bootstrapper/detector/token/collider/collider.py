# src/bootstrapper/detector/token/collider.py

"""
Module: bootstrapper.detector.token.collider
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from blueprint import TokenBlueprint
from err import (
    OpeningSquareCollisionException,TokenIdCollisionException, TokenNameCollisionException
)
from report import CollisionReport
from result import AnalysisResult
from stack import TokenStackService
from util import LoggingLevelRouter



class TokenCollider:
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
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            stream: TokenStackService,
            target: Optional[TokenBlueprint],
    ) -> AnalysisResult[CollisionReport]:
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
        method = f"{cls.__class__.__name__}.detect"
        # --- Loop through the collider_candidates to find matches. ---#
        
        for item in stream.items:
            # Handle the case that, a token already has the target's id.
            if item.id == target.id:
                # Return the collision details in the report.
                return AnalysisResult.completed(
                    CollisionReport.occurrence(
                        collider=item,
                        target_set=target,
                        colliding_variable="id",
                        collision_value=item.id,
                        exception=TokenIdCollisionException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=TokenIdCollisionException.MSG,
                            err_code=TokenIdCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, a token already has the target's id.
            if item.designation == target.formation.designation.upper():
                # Return the collision details in the report.
                return AnalysisResult.completed(
                    CollisionReport.occurrence(
                        collider=item,
                        target_set=target,
                        colliding_variable="designation",
                        collision_value=item.designation,
                        exception=TokenNameCollisionException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=TokenNameCollisionException.MSG,
                            err_code=TokenNameCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, the target shares its home_square_name with a collider_candidates member.
            if item.home_square.name.upper() == target.formation.home_square_name.upper():
                # Return the collider, designation, and the exception.
                return AnalysisResult.success(
                    CollisionReport.occurrence(
                        collider=item,
                        target_set=target,
                        colliding_variable="home_square",
                        collision_value=item.home_square,
                        exception=OpeningSquareCollisionException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=OpeningSquareCollisionException.MSG,
                            err_code=OpeningSquareCollisionException.ERR_CODE,
                        )
                    )
                )
        # --- Send the no collisions detected report. ---#
        return AnalysisResult.success(CollisionReport.no_collisions(target))
    