# src/bootstrap/validation/struct/binder/player/loader.py

"""
Module: bootstrap.validation.struct.binder.player.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import PlayerBinderLayerToolkit
from bootstrap import BinderValidationLoader
from domain import PlayerBinder, PlayerBinderPrimeExtract
from err import (
    PlayerBinderCarrierEmptyException, PlayerBinderConsistencyException,
    PlayerBinderLoaderException, PlayerBinderValidationRequestNullException
)
from exchange import PlayerBinderValidationRequest
from transit import PlayerBinderCarrier
from util import LoggingLevelRouter


class PlayerBinderLoader(BinderValidationLoader[PlayerBinder]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   PlayerBinderValidationRequest
            -   PlayerBinder
            -   PlayerBinderBlueprint

    Attributes:
        toolkit: PlayerBinderLayerToolkit

    Provides:
        -   def execute(item: Any) -> ValidationResult[PlayerBinder[T]

    Super Class:
        BinderLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[PlayerBinderLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[PlayerBinderLayerToolkit]
        """
        super().__init__(toolkit=toolkit or PlayerBinderLayerToolkit())
    
    @property
    def toolkit(self) -> PlayerBinderLayerToolkit:
        return cast(PlayerBinderLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, bootstrap: Any) -> ValidationResult[PlayerBinderPrimeExtract]:
        """
        Extract the PlayerBinderBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a PlayerBinderValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a PlayerBinderCarrier
                        -   An empty PlayerBinderCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a
                PlayerBinderPrimeExtract for the success result.
        Args:
            bootstrap: Any
        Returns:
            ValidationResult[PlayerBinderPrimeExtract]
        Raises:
            PlayerBinderLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=bootstrap,
            target_model=PlayerBinderValidationRequest,
            null_exception=PlayerBinderValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderLoaderException.MSG,
                    err_code=PlayerBinderLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[PlayerBinderValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderLoaderException.MSG,
                    err_code=PlayerBinderLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(PlayerBinderCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderLoaderException.MSG,
                    err_code=PlayerBinderLoaderException.ERR_CODE,
                    ex=PlayerBinderCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerBinderCarrierEmptyException.MSG,
                        err_code=PlayerBinderCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the blueprint has an inconsistency.
        if blueprint.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderLoaderException.MSG,
                    err_code=PlayerBinderLoaderException.ERR_CODE,
                    ex=PlayerBinderConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerBinderConsistencyException.MSG,
                        err_code=PlayerBinderConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = PlayerBinderPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)