# src/detection/collision/token/detector.py

"""
Module: detection.token.detector
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, cast

from blueprint import TokenBlueprint
from detection import Detector, TokenCollider, TokenCollisionBootstrapper
from err import TokenCollisionDetectorException
from microservice import IdentityService
from model import Token
from report import CollisionReport
from result import AnalysisResult
from stack import TokenStackService
from util import LoggingLevelRouter
from validator import PrimingValidator


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
    _collider: TokenCollider
    _identity_service: IdentityService
    _priming_validator: PrimingValidator
    _bootstrapper: TokenCollisionBootstrapper

    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            stream: TokenStackService,
            target: Optional[Token] | None = None,
            target_blueprint: Optional[TokenBlueprint] | None = None,
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
            attractor: TokenBlueprint
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
        
        bootstrap_result = self._bootstrapper.execute(
            target=target,
            target_blueprint=target_blueprint,
            identity_service=self._identity_service,
            priming_validator=self._priming_validator,
        )
        if bootstrap_result.is_failure:
            # Return the collision details in the report.
            return AnalysisResult.failure(
                TokenCollisionDetectorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenCollisionDetectorException.MSG,
                    err_code=TokenCollisionDetectorException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        attractor = cast(TokenBlueprint, bootstrap_result.payload)
        # --- Send the no collisions detected report. ---#
        return self._collider.execute(stream=stream, attractor=attractor)