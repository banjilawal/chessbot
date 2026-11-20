# src/exchange/service/validation/model/encounter/service.py

"""
Module: exchange.service.validation.model.encounter.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Encounter, EncounterBlueprint
from err import EncounterCarrierEmptyException, EncounterValidationServiceException
from exchange import EncounterValidationRequest
from microservice import ValidationMicroservice
from transit import EncounterCarrier, EncounterValidationDispatcher
from util import LoggingLevelRouter


class EncounterValidationService(ValidationMicroservice[Encounter]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Encounter
                _   EncounterBlueprint
            products from EncounterValidationService.

    Attributes:
        dispatcher: EncounterValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: EncounterValidationRequest
            ) -> ValidationResult[Encounter]
            
        -   def extract_blueprint(
                    request: EncounterValidationRequest
            ) -> ValidationResult[EncounterBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[EncounterValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[EncounterValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or EncounterValidationDispatcher())
    
    @property
    def dispatcher(self) -> EncounterValidationDispatcher:
        return cast(EncounterValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: EncounterValidationRequest) -> ValidationResult[Encounter]:
        """
        Extract an Encounter safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Encounter from the result then send it to the client.
        Args:
            request: EncounterValidationRequest
        Result:
            ValidationResult[Encounter]
        Raises:
            EncounterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationServiceException.MSG,
                    err_code=EncounterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(EncounterCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationServiceException.MSG,
                    err_code=EncounterValidationServiceException.ERR_CODE,
                    ex=EncounterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterCarrierEmptyException.MSG,
                        err_code=EncounterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Encounter, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: EncounterValidationRequest,
    ) -> ValidationResult[EncounterBlueprint]:
        """
        Extract an EncounterBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the EncounterBlueprint from the result then send it
                to the client.
        Args:
            request: EncounterValidationRequest
        Result:
            ValidationResult[EncounterBlueprint]
        Raises:
            EncounterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationServiceException.MSG,
                    err_code=EncounterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(EncounterCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationServiceException.MSG,
                    err_code=EncounterValidationServiceException.ERR_CODE,
                    ex=EncounterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterCarrierEmptyException.MSG,
                        err_code=EncounterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(EncounterBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)