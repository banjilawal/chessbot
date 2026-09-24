# src/validator/model/path/validator.py

"""
Module: validator.model.path.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, PathValidatorToolkit
from domain import Path, PathBlueprint, PathValidationRequest, SquareRegister
from err import (
    EmptySquareRegisterCarrierException, PathValidationRequestNullException,
    PathValidatorException
)
from transit import PathCarrier, SquareRegisterCarrier
from util import IdFactory, LoggingLevelRouter


class PathValidator(ModelValidator[Path]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Path instance is certified safe, reliable, and consistent before use.

    Attributes:
        toolkit: PathValidatorToolkit
        
    Provides:
        - def execute(candidate: Any) -> ValidationResult[PathCarrier]

    Super Class:
        ModelValidator
    """
    
    def __init__(self, toolkit: Optional[PathValidatorToolkit] | None = None):
        """
        Args:
            toolkit: Optional[PathValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or PathValidatorToolkit())
        
    @property
    def toolkit(self) -> PathValidatorToolkit:
        return cast(PathValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PathCarrier]:
        """
        Certify a PathCarrier's payload is either a Path or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    *   The request is either null or not a PathValidatorRequest.
                    *   The request's payload is either,
                            null
                            not a PathCarrier
                            an empty PathCarrier.
                    *   Either the id, board, or owner attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[PathCarrier]
        Raises:
            PathValidatorException
            BoardCarrierEmptyException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=candidate,
            target_model=PathValidationRequest,
            null_exception=PathValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        request = cast(PathValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(
            PathCarrier,
            carrier_validation.payload,
        )
        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that there is no blueprint.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=EmptySquareRegisterCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptySquareRegisterCarrierException.MSG,
                        err_code=EmptySquareRegisterCarrierException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that any label in the blueprint is flagged.
        blueprint_label = blueprint.label
        candidate_label = blueprint_label
        if blueprint_label is not None:
            label_validation = self.toolkit.helper.number_validator.execute(
                candidate=blueprint_label
            )
            if label_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PathValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathValidatorException.MSG,
                        err_code=PathValidatorException.ERR_CODE,
                        ex=label_validation.exception,
                    )
                )
            candidate_label = cast(int, label_validation.payload)
        # Handle the case that the squareRegister does not pass a validation check.
        endpoint_validation = self.toolkit.helper.endpoint_validator.execute(
            candidate=SquareRegisterValidationRequest(
                item=blueprint.endpoints,
                id=IdFactory.next_id(class_name="SquareRegisterValidationRequest"),
            ),
        )
        if endpoint_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=endpoint_validation.exception,
                )
            )
        # --- Extract the endpoints validation payload. ---#
        endpoint_carrier = cast(
            SquareRegisterCarrier,
            endpoint_validation.payload
        )
        # Handle the case that the endpoint_carrier does not contain a model.
        if not endpoint_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=EmptySquareRegisterCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptySquareRegisterCarrierException.MSG,
                        err_code=EmptySquareRegisterCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Extract validation payloads. ---#
        label = candidate_label
        endpoints = cast(SquareRegister, endpoint_carrier.entity)
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if carrier.is_carrying_model:
            payload = Path(label=label, endpoints=endpoints,)
            return ValidationResult.success(
                PathCarrier(model=payload)
            )
        # The blueprint case
        payload = PathBlueprint(label=label, endpoints=endpoints,)
        return ValidationResult.success(
            PathCarrier(blueprint=payload)
        )
        
        
