# src/bootstrap/validation/struct/binder/team/loader.py

"""
Module: bootstrap.validation.struct.binder.team.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import  TeamBinderLayerToolkit
from bootstrap import BinderValidationLoader
from domain import TeamBinder, TeamBinderPrimeExtract
from err import (
    TeamBinderCarrierEmptyException, TeamBinderConsistencyException,
    TeamBinderLoaderException
)
from exchange import TeamBinderValidationRequest
from transit import TeamBinderCarrier

from util import LoggingLevelRouter


class TeamBinderLoader(BinderValidationLoader[TeamBinder]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   TeamBinderValidationRequest
            -   TeamBinder
            -   TeamBinderBlueprint

    Attributes:
        toolkit: TeamBinderLayerToolkit

    Provides:
        -   def execute(item: Any) -> ValidationResult[TeamBinder[T]

    Super Class:
        BinderLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[TeamBinderLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TeamBinderLayerToolkit]
        """
        super().__init__(toolkit=toolkit or TeamBinderLayerToolkit())
    
    @property
    def toolkit(self) -> TeamBinderLayerToolkit:
        return cast(TeamBinderLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, bootstrap: Any) -> ValidationResult[TeamBinderPrimeExtract]:
        """
        Extract the TeamBinderBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a TeamBinderValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a TeamBinderCarrier
                        -   An empty TeamBinderCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a
                TeamBinderPrimeExtract for the success result.
        Args:
            bootstrap: Any
        Returns:
            ValidationResult[TeamBinderPrimeExtract]
        Raises:
            TeamBinderLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=bootstrap,
            target_model=TeamBinderValidationRequest,
            null_exception=TeamBinderValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderLoaderException.MSG,
                    err_code=TeamBinderLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[TeamBinderValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderLoaderException.MSG,
                    err_code=TeamBinderLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(TeamBinderCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderLoaderException.MSG,
                    err_code=TeamBinderLoaderException.ERR_CODE,
                    ex=TeamBinderCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamBinderCarrierEmptyException.MSG,
                        err_code=TeamBinderCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the blueprint has an inconsistency.
        if blueprint.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderLoaderException.MSG,
                    err_code=TeamBinderLoaderException.ERR_CODE,
                    ex=TeamBinderConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamBinderConsistencyException.MSG,
                        err_code=TeamBinderConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = TeamBinderPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)