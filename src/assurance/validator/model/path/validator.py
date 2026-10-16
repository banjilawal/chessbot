# src/assurance/validator/model/path/validator.py

"""
Module: assurance.validator.model.path.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import PathValidationLoader, PathValidatorToolkit, ModelValidator
from domain import Path, PathBlueprint, PathPrimeExtract, SquareRegister
from err import PathCarrierEmptyException, PathValidatorException
from exchange import SquareRegisterValidationRequest
from transit import PathCarrier, SquareRegisterCarrier

from util import IdFactory, LoggingLevelRouter


class PathValidator(ModelValidator[Path]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PathCarrier and its contents are safe to use.

    Attributes:
        loader: PathLoader

    Provides:
        -   def execute(candidate: Ant) -> ValidationResult[PathCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            loader: Optional[PathValidationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[PathLoader]
        """
        super().__init__(loader=loader or PathValidationLoader())
        
    @property
    def loader(self) -> PathValidationLoader:
        return cast(PathValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> PathValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PathCarrier]:
        """
        Assure a candidate is a safe PathCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a PathValidatorRequest.
                    -   The request's payload is either,
                            null, an empty PathCarrier, or the wrong type.
                    -   The endpoints or label are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[PathCarrier]
        Raises:
            PathValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(PathPrimeExtract, loading.payload)
        carrier = prime_extract.reference
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=PathCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathCarrierEmptyException.MSG,
                        err_code=PathCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_THE_LABEL_ATTRIBUTE. ---#
        label = blueprint.label
        if label is not None:
            label_validation = self.toolkit.number_validator.execute(label)
            # Handle the case that the endpoints are flagged.
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
            label = cast(int, label_validation.payload)
        # --- PROCESS_THE_ENDPOINTS_ATTRIBUTE. ---#
        endpoints_validation = self.toolkit.wrapper.square_register.extract_model(
            request=SquareRegisterValidationRequest(
                item=SquareRegisterCarrier(model=blueprint.endpoints),
                id=IdFactory.next_id(class_name="SquareRegisterValidationRequest"),

            )
        )
        # Handle the case that the endpoints are flagged.
        if endpoints_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=endpoints_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        endpoints = cast(SquareRegister, endpoints_validation.payload)
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Path.
        if prime_extract.recipient_wants_model:
            model = Path(label=label, endpoints=endpoints)
            payload = PathCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a PathBuilder that needs a Blueprint.
        payload = PathCarrier(
            blueprint=PathBlueprint(
                label=label,
                endpoints=endpoints,
            )
        )
        return ValidationResult.success(payload)



