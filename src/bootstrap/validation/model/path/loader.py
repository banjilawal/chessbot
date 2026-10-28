# src/bootstrap/validation/model/path/loader.py

"""
Module: bootstrap.validation.context.path.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import PathLayerToolkit
from bootstrap import ModelValidationLoader
from domain import Path, PathPrimeExtract
from err import (
    PathCarrierEmptyException, PathValidationLoaderException, PathValidationRequestNullException
)
from exchange import PathValidationRequest
from transit import PathCarrier

from util import LoggingLevelRouter


class PathValidationLoader(ModelValidationLoader[Path]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   PathValidationRequest
            -   PathCarrier
            -   PathBlueprint

    Attributes:
        toolkit: PathLayerToolkit

    Provides:
        -   def execute(item: Any) -> ValidationResult[PathPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[PathLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[PathLayerToolkit]
        """
        super().__init__(toolkit=toolkit or PathLayerToolkit())
    
    @property
    def toolkit(self) -> PathLayerToolkit:
        return cast(PathLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[PathPrimeExtract]:
        """
        Extract the PathBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a PathValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a PathCarrier
                        -   An empty PathCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a PathPrimeExtract
                for the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[PathPrimeExtract]
        Raises:
            PathLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=item,
            target_model=PathValidationRequest,
            null_exception=PathValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationLoaderException.MSG,
                    err_code=PathValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[PathValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationLoaderException.MSG,
                    err_code=PathValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(PathCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationLoaderException.MSG,
                    err_code=PathValidationLoaderException.ERR_CODE,
                    ex=PathCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathCarrierEmptyException.MSG,
                        err_code=PathCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = PathPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)