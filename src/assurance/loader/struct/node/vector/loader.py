# src/assurance/load/struct/node/vector/loader.py

"""
Module: assurance.load.struct.node.vector.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import NodeLoader, VectorNodeValidatorToolkit
from domain import VectorNode, VectorNodePrimeExtract
from err import (
    EmptyVectorNodeCarrierException, VectorNodeLoaderException,
    VectorNodeValidationRequestNullException
)
from exchange import VectorNodeValidationRequest
from transit import VectorNodeCarrier

from util import LoggingLevelRouter


class VectorNodeLoader(NodeLoader[VectorNode]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   VectorNodeValidationRequest
            -   VectorNodeCarrier
            -   VectorNodeBlueprint

    Attributes:
        toolkit: VectorNodeValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[VectorNodePrimeExtract[T]

    Super Class:
        NodeLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[VectorNodeValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[VectorNodeValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or VectorNodeValidatorToolkit())
    
    @property
    def toolkit(self) -> VectorNodeValidatorToolkit:
        return cast(VectorNodeValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[VectorNodePrimeExtract]:
        """
        Extract the VectorNodeBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a VectorNodeValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a VectorNodeCarrier
                        -   An empty VectorNodeCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a VectorNodePrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[VectorNodePrimeExtract]
        Raises:
            VectorNodeLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=VectorNodeValidationRequest,
            null_exception=VectorNodeValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeLoaderException.MSG,
                    err_code=VectorNodeLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[VectorNodeValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeLoaderException.MSG,
                    err_code=VectorNodeLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(VectorNodeCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeLoaderException.MSG,
                    err_code=VectorNodeLoaderException.ERR_CODE,
                    ex=EmptyVectorNodeCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyVectorNodeCarrierException.MSG,
                        err_code=EmptyVectorNodeCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = VectorNodePrimeExtract(carrier=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)