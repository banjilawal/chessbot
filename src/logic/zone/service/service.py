# src/logic/zone/service/validator.py

"""
Module: logic.zone.service.service
Author: Banji Lawal
Created: 2026-03-29
version: 1.0.0
"""

from __future__ import annotations
from math import sqrt
from typing import Union, cast

from logic.scalar import Scalar, ScalarService
from logic.vector import Vector, VectorService
from logic.zone import Zone, ZoneBuilderProcess, ZoneOpsController, ZoneServiceException, ZoneValidatorTransaction
from logic.system import BuilderResult, ComputationResult, IdFactory, IntegrityService, id_emitter
from logic.zone.model.table import ZoneTable


class ZoneService(IntegrityService[Zone]):
    """
    Role:
        -   API
        -   Stateless microservice
        -   Lifecycle Manager
        -   Operations Provider

    Responsibilities:
        1.  Baremetal service request API for Zone operations.
        2.  Maintain the builder-validator security lifecycle for Zone instances.

    Attributes:
        SERVICE_NAME: ZoneService

        id: int
        name: name
        builder: Zonebuilder
        validator: ZoneValidator
        controller: ZoneOpsController

    Provides:
    
        -   euclidean_distance(u: Zone, v: Zone) -> ComputationResult[int]
        
        -   add_to_zone(
                    zone: Optional[Zone],
                    operand: Union[Vector, Zone],
                    vector_service: VectorService,
            ) -> ComputationResult[Zone]

        -   multiply_by_scalar(
                    zone: Zone,
                    scalar: Scalar,
                    scalar_service: ScalarService,
            ) -> ComputationResult[Zone]

        -   convert_vector_to_zone(
                    self,
                    vector: Vector,
                    vector_service: VectorService = VectorService()
            ) -> BuilderResult[Zone]

    Super Class:
        IntegrityService
    """
    SERVICE_NAME = "ZoneService"
    _table: ZoneTable
    _ops_controller: ZoneOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="ZoneService"),
            ops_controller: ZoneOpsController = ZoneOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: ZoneOpsController
        """
        super().__init__(id=id, name=name)
        self._table = ZoneTable()
        self._ops_controller = ops_controller

    @property
    def builder(self) -> ZoneBuilderProcess:
        return self._ops_controller.builder
    
    @property
    def validator(self) -> ZoneValidatorTransaction:
        return self._ops_controller.validator
    
    @property
    def ops_controller(self) -> ZoneOpsController:
        return self._ops_controller
    
    def add_to_zone(
            self,
            zone: Zone,
            operand: Union[Vector, Zone],
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Zone]:
        """
        Add an operand to a zone.
        
        Actions:
            1.  Send an exception chain in the ComputationResult if either:
                    -   The zone is unsafe.
                    -   The operand is unsafe.
                    -   Their summation is not computed.
            2.  Otherwise, send the success result.
        Args:
            zone: [Zone]
            operand: Union[Vector, Zone]
            vector_service: VectorService
        Returns:
            ComputationResult[Zone]
        Raises:
            ZoneServiceException
        """
        method = f"{self.__class__.__name__}.add_to_zone"
        
        # Request a summation from the controller.
        request_result = self._ops_controller.arithmetic.addition.execute(
            zone=zone,
            operand=operand,
            zone_service=self,
            vector_service=vector_service,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return ComputationResult.failure(
                ZoneServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ZoneServiceException.MSG,
                    err_code=ZoneServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
      
    def multiply_zone(
            self,
            zone: Zone,
            scalar: Scalar,
            scalar_service: ScalarService = ScalarService(),
    ) -> ComputationResult[Zone]:
        """
        Multiply a cord by a scalar.

        Actions:
            1.  Send an exception chain in the ComputationResult if either:
                    -   The zone is unsafe.
                    -   The scalar is unsafe.
                    -   Their product is not computed.
            2.  Otherwise, send the success result.
        Args:
            zone: [Zone]
            scalar: Scalar
            scalar_service: ScalarService
        Returns:
            ComputationResult[Zone]
        Raises:
            ZoneServiceException
        """
        method = f"{self.__class__.__name__}.multiply_zone"
        
        # Request a multiplication from the controller.
        request_result = self._ops_controller.arithmetic.multiplication.execute(
            zone=zone,
            scalar=scalar,
            zone_service=self,
            scalar_service=scalar_service,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return ComputationResult.failure(
                ZoneServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ZoneServiceException.MSG,
                    err_code=ZoneServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
        
    def distance(self, u: Zone, v: Zone) -> ComputationResult[int]:
        """
        Find the distance between two zones.

        Actions:
            1.  Send an exception chain in the ComputationResult if either:
                    -   A zone is unsafe.
                    -   Their distance is not computed.
            2.  Otherwise, send the success result.
        Args:
            u: Zone
            v: Zone
        Returns:
            ComputationResult[Zone]
        Raises:
            ZoneServiceException
        """
        method = f"{self.__class__.__name__}.distance"
        
        # Request a multiplication from the controller.
        request_result = self._ops_controller.arithmetic.distance.compute(
            u=u,
            v=v,
            zone_service=self,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return ComputationResult.failure(
                ZoneServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ZoneServiceException.MSG,
                    err_code=ZoneServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    def convert_vector_to_zone(
            self,
            vector: Vector,
            vector_service: VectorService = VectorService()
    ) -> ComputationResult[Zone]:
        """
        Convert a vector to a zone.

        Actions:
            1.  Send an exception chain in the ComputationResult if either:
                    -   The vector is unsafe.
                    -   A zone cannot be built from the vector's components.
            2.  Otherwise, send the success result.
        Args:
            vector: Vector,
            vector_service: VectorService
        Returns:
            ComputationResult[Zone]
        Raises:
            ZoneServiceException
        """
        method = f"{self.__class__.__name__}.convert_vector_to_zone"
        
        # Request a conversion from the controller.
        request_result = self._ops_controller.arithmetic.conversion.execute(
            vector=vector,
            zone_service=self,
            vector_service=vector_service,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return ComputationResult.failure(
                ZoneServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ZoneServiceException.MSG,
                    err_code=ZoneServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
