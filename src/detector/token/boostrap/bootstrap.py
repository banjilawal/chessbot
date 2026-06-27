# src/detector/collision/token/analyst.py

"""
Module: detector.collision.token.analyst
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
    TokenCollisionDetectorException,
    TokenIdCollisionException, TokenNameCollisionException, TokenStackNullException, ZeroTokenContextFlagsException
)
from microservice import IdentityService
from model import Token
from report import CollisionReport
from result import ValidationResult, ValidationResult
from stack import TokenStackService
from util import LoggingLevelRouter
from validation import TokenValidator, ValidationPrimer


class TokenCollisionDetectorBootstrapper:
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
        -   CollisionAnalyst[T]
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            stream: TokenStackService,
            target: Optional[Token] | None = None,
            target_blueprint: Optional[TokenBlueprint] | None = None,
            identity_service: IdentityService | None = None,
            validation_primer: ValidationPrimer | None = None,
            token_validator: TokenValidator | None = None,
    ) -> ValidationResult[TokenBlueprint]:
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
            target_blueprint: TokenBlueprint
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
        
        
        if validation_primer is None:
            validation_primer = ValidationPrimer()
        if identity_service is None:
            identity_service = IdentityService()
        
        params = [target, target_blueprint]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenCollisionDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionDetectorException.MSG,
                    err_code=TokenCollisionDetectorException.ERR_CODE,
                    ex=ZeroTokenContextFlagsException(
                        msg=ZeroTokenContextFlagsException.MSG,
                        err_code=ZeroTokenContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenCollisionDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionDetectorException.MSG,
                    err_code=TokenCollisionDetectorException.ERR_CODE,
                    ex=ExcessTeamContextFlagsException(
                        msg=ExcessTeamContextFlagsException.MSG,
                        err_code=ExcessTeamContextFlagsException.ERR_CODE,
                    )
                )
            )
        
        if target is not None:
            validation_result = token_validator.validate(target)
            if validation_result.is_failure:
                return ValidationResult.failure(
                    TokenCollisionDetectorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenCollisionDetectorException.MSG,
                        err_code=TokenCollisionDetectorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            return ValidationResult.success(
                TokenBlueprint(
                    id=target.id,
                    team=target.team,
                    rank=target.rank,
                    opening_square=target.opening_square,
                )
            )
        else:
            blueprint_validation_result = validation_primer.validate(
                candidate=target_blueprint,
                target_type=TokenBlueprint,
                nullable=TokenBlueprintNullException(),
            )
        
        stream_validation_result = validation_primer.validate(
            candidate=stream,
            target_type=TokenStackService,
            nullable=TokenStackNullException()
        )
        if stream_validation_result.is_failure:
            return ValidationResult.failure(
                TokenCollisionDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionDetectorException.MSG,
                    err_code=TokenCollisionDetectorException.ERR_CODE,
                    ex=stream_validation_result.exception
                )
            )

        if blueprint_validation_result.is_failure:
            return ValidationResult.failure(
                TokenCollisionDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionDetectorException.MSG,
                    err_code=TokenCollisionDetectorException.ERR_CODE,
                    ex=blueprint_validation_result.exception
                )
            )
        blueprint_identity_validation_result = identity_service.validate_identity(
            id_candidate=target_blueprint.id,
            name_candidate=target_blueprint.formation.designation,
        )
        if blueprint_identity_validation_result.is_failure:
            return ValidationResult.failure(
                TokenCollisionDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionDetectorException.MSG,
                    err_code=TokenCollisionDetectorException.ERR_CODE,
                    ex=blueprint_identity_validation_result.exception
                )
            )
        # --- Loop through the collider_candidates to find matches. ---#
        
        for token in stream.items:
            # Handle the case that, a token already has the target's id.
            if token.id == target_blueprint.id:
                # Return the collision details in the report.
                return ValidationResult.completed(
                    CollisionReport.occurrence(
                        collider=token,
                        target_set=target_blueprint,
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
            if token.designation == target_blueprint.formation.designation.upper():
                # Return the collision details in the report.
                return ValidationResult.completed(
                    CollisionReport.occurrence(
                        collider=token,
                        target_set=target_blueprint,
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
            if token.opening_square.name.upper() == target_blueprint.formation.opening_square_name.upper():
                # Return the collider, designation, and the exception.
                return ValidationResult.success(
                    CollisionReport.occurrence(
                        collider=token,
                        target_set=target_blueprint,
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
        return ValidationResult.success(CollisionReport.no_collisions(target_blueprint))
    