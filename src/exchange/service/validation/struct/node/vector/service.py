# src/exchange/service/validation/struct/node/vector/service.py

"""
Module: exchange.service.validation.struct.node.vector.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import VectorNode
from exchange import NodeValidationService
from util import LoggingLevelRouter


class VectorNodeValidationService(
    NodeValidationService[VectorNode]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Vector
                _   VectorBlueprint
            products from VectorNodeValidationService.

    Attributes:
        service: VectorNodeValidationService
        
    Provides:
        -   def extract_model(
                    request: VectorNodeValidationRequest
            ) -> ValidationResult[Vector]
            
        -   def extract_blueprint(
                    request: VectorNodeValidationRequest
            ) -> ValidationResult[VectorBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[VectorNodeValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[VectorNodeValidationService]
        """
        super().__init__(service=service or VectorNodeValidationService())
    
    @property
    def service(self) -> VectorNodeValidationService:
        return cast(VectorNodeValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: VectorNodeValidationRequest,
    ) -> ValidationResult[VectorNode]:
        """
        Extract a Vector safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Vector from the success response then send it 
                to the client.
        Args:
            request: VectorNodeValidationRequest
        Result:
            ValidationResult[Vector]
        Raises:
            VectorNodeValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidationServiceException.MSG,
                    err_code=VectorNodeValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorNodeValidationResponse, result)
        if not response.valid_node:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidationServiceException.MSG,
                    err_code=VectorNodeValidationServiceException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        node = cast(VectorNode, response.valid_node)
        return ValidationResult.success(node)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: VectorNodeValidationRequest,
    ) -> ValidationResult[VectorNodeBlueprint]:
        """
        Extract a VectorBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the VectorBluprint from the success response
                then send it to the client.
        Args:
            request: VectorNodeValidationRequest
        Result:
            ValidationResult[VectorBlueprint]
        Raises:
            VectorNodeValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidationServiceException.MSG,
                    err_code=VectorNodeValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorNodeValidationResponse, result)
        if not response.valid_vector:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidationServiceException.MSG,
                    err_code=VectorNodeValidationServiceException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(VectorNodeBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)