# src/bootstrap/detector/token/bootstrapper.py

"""
Module: bootstrap.detector.token.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import TokenBlueprint
from err import (
    ExcessTeamContextFlagsException, TokenBlueprintNullException, TokenCollisionBootstrapperException,
    TokenStackNullException, ZeroTokenContextFlagsException
)
from microservice import IdentityService
from model import Token
from result import ValidationResult
from stack import TokenStackService
from util import LoggingLevelRouter
from validation import TokenValidator, PrimingValidator


class TokenCollisionBootstrapper:
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
            priming_validator: PrimingValidator | None = None,
    ) -> ValidationResult[TokenBlueprint]:
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
            target_blueprint: TokenBlueprint
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
        method = f"{cls.__class__.__name__}.execute"
        
        
        if priming_validator is None:
            priming_validator = PrimingValidator()
        if identity_service is None:
            identity_service = IdentityService()
        
        params = [target, target_blueprint]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenCollisionBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionBootstrapperException.MSG,
                    err_code=TokenCollisionBootstrapperException.ERR_CODE,
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
                TokenCollisionBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionBootstrapperException.MSG,
                    err_code=TokenCollisionBootstrapperException.ERR_CODE,
                    ex=ExcessTeamContextFlagsException(
                        msg=ExcessTeamContextFlagsException.MSG,
                        err_code=ExcessTeamContextFlagsException.ERR_CODE,
                    )
                )
            )
        stream_validation_result = priming_validator.validate(
            candidate=stream,
            target_type=TokenStackService,
            nullable=TokenStackNullException()
        )
        if stream_validation_result.is_failure:
            return ValidationResult.failure(
                TokenCollisionBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionBootstrapperException.MSG,
                    err_code=TokenCollisionBootstrapperException.ERR_CODE,
                    ex=stream_validation_result.exception
                )
            )
        
        if target is not None:
            return cls._validate_target(
                target=target,
                token_stack=stream.microservice.validator,
            )

        return cls._validate_blueprint(
            blueprint=target_blueprint,
            priming_validator=priming_validator,
            identity_service=identity_service
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_target(
            cls,
            target: Token,
            token_validator: TokenValidator,
    ) -> ValidationResult[TokenBlueprint]:
        method = f"{cls.__class__.__name__}._validate_target"
    
        validation_result = token_validator.validate(target)
        if validation_result.is_failure:
            return ValidationResult.failure(
                TokenCollisionBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionBootstrapperException.MSG,
                    err_code=TokenCollisionBootstrapperException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        return ValidationResult.success(
            TokenBlueprint(
                id=target.id,
                team=target.team,
                rank=target.rank,
                formation=target.formation,
                home_square=target.home_square,
            )
        )
        
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_blueprint(
            cls, 
            blueprint: TokenBlueprint, 
            priming_validator: PrimingValidator,
            identity_service: IdentityService,
    ) -> ValidationResult[TokenBlueprint]:
        method = f"{cls.__name__}.validate_blueprint"
    
        validation_result = priming_validator.execute(
            candidate=blueprint,
            target_type=TokenBlueprint,
            nullable=TokenBlueprintNullException(),
        )
    
        if validation_result.is_failure:
            return ValidationResult.failure(
                TokenCollisionBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionBootstrapperException.MSG,
                    err_code=TokenCollisionBootstrapperException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        identity_validation_result = identity_service.validate_identity(
            id_candidate=blueprint.id,
            name_candidate=blueprint.formation.designation,
        )
        if identity_validation_result.is_failure:
            return ValidationResult.failure(
                TokenCollisionBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenCollisionBootstrapperException.MSG,
                    err_code=TokenCollisionBootstrapperException.ERR_CODE,
                    ex=identity_validation_result.exception
                )
            )
        return ValidationResult.success(blueprint)