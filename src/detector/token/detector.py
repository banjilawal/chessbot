# src/detector/collision/token/detector.py

"""
Module: detector.collision.token.detector
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from blueprint import TokenBlueprint
from detector import Detector
from err import (
    ExcessTeamContextFlagsException, OpeningSquareCollisionException, TokenBlueprintNullException,
    TokenCollisionDetectorException, TokenIdCollisionException, TokenNameCollisionException, TokenStackNullException,
    ZeroTokenContextFlagsException
)
from microservice import IdentityService
from model import Token
from report import CollisionReport
from result import AnalysisResult
from stack import TokenStackService
from util import LoggingLevelRouter
from validation import TokenValidator, ValidationPrimer


class TokenCollisionDetector(Detector[Token]):
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
        -   CollisionDetector[T]
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            stream: TokenStackService,
            target: Optional[TokenBlueprint] | None = None,
    ) -> AnalysisResult[CollisionReport]:
        """
        Report if any schema member has the same id, designation or
        opening_square_name as the target.
        
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
            validation_primer: ValidationPrimer
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
        
        for token in stream.items:
            # Handle the case that, a token already has the target's id.
            if token.id == target.id:
                # Return the collision details in the report.
                return AnalysisResult.completed(
                    CollisionReport.occurrence(
                        collider=token,
                        target_set=target,
                        colliding_variable="id",
                        collision_value=token.id,
                        exception=TokenIdCollisionException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=TokenIdCollisionException.MSG,
                            err_code=TokenIdCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, a token already has the target's id.
            if token.designation == target.formation.designation.upper():
                # Return the collision details in the report.
                return AnalysisResult.completed(
                    CollisionReport.occurrence(
                        collider=token,
                        target_set=target,
                        colliding_variable="designation",
                        collision_value=token.designation,
                        exception=TokenNameCollisionException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=TokenNameCollisionException.MSG,
                            err_code=TokenNameCollisionException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, the target shares its opening_square_name with a collider_candidates member.
            if token.opening_square.name.upper() == target.formation.opening_square_name.upper():
                # Return the collider, designation, and the exception.
                return AnalysisResult.success(
                    CollisionReport.occurrence(
                        collider=token,
                        target_set=target,
                        colliding_variable="opening_square",
                        collision_value=token.opening_square,
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
    