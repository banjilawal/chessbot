# src/microservice/registry/service/register/microservice.py

"""
Module: microservice.registry.service.register.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import ServiceRegistry
from result import InsertionResult
from util import LoggingLevelRouter
from err import ServiceOpNameCollisionException, ServiceRegistrationException
from microservice import Microservice, ServiceRegistryNameSearch, ServiceRegistryMicroservice


class RegisterService(ServiceRegistryMicroservice):
    """
    Role
        -   Service

    Responsibilities:
        1.  Registers a service to the registry while maintaining consistency and integrity.

    Attributes:
        MICROSERVICE_NAME = "register_service"

    Provides:
        -   def execute(
                    service: Microservice,
                    registry: ServiceRegistry,
                    service_search: RegistryServiceSearch | None = None,
            ) -> InsertionResult:

    Super Class:
        ServiceRegistryMicroservice
    """
    OPERATION_NAME = "register_service"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            service: Microservice,
            registry: ServiceRegistry,
            service_search: ServiceRegistryNameSearch | None = None,
    ) -> InsertionResult:
        """
        Register a new service to the registry.
        
        Action:
            1.  Send an exception chain in the InsertionResult if either condition occurs.
                    -   A different service exists in the same domain with the same microservice name.
                    -   Registering the service's entry in the registry dictionary fails.
            2.  Otherwise, send the success result.
        Args:
            service: Microservice
            registry: ServiceRegistry
            service_search: RegistryServiceSearch
        Returns:
            InsertionResult
        Raises:
            CoordBuildException
        """
        method = f"{cls.__name__}.execute"
        
        if service_search is None:
            service_search = ServiceRegistryNameSearch()
        
        service_search_result = service_search.execute(
            microservice_name=service.name,
            registry=registry
        )
        # Handle the case that, the search is not completed.
        if service_search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ServiceRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ServiceRegistrationException.MSG,
                    err_code=ServiceRegistrationException.ERR_CODE,
                    ex=service_search_result.exception,
                )
            )
        # --- Handoff processing to _collision_helper if the key has already been used. ---#
        if service_search_result.is_success:
            collision_processing_result = cls._collision_helper(registry)
            # handle the case that, there is a hash key collision.
            if collision_processing_result.is_failure:
                # Send the exception chain on failure.
                return InsertionResult.failure(
                    ServiceRegistrationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ServiceRegistrationException.MSG,
                        err_code=ServiceRegistrationException.ERR_CODE,
                        ex=collision_processing_result.exception,
                    )
                )
            # Send the success result if there is no hash collision.
            return InsertionResult.success()
        # --- Add a new entry to the registry if the key is new. ---#
        registry.entries[service.SERVICE_NAME] = service
        registry.registration_counters[service.MICROSERVICE_NAME] += 1
        
        # --- Send the success result . ---#
        return InsertionResult.success()
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _collision_helper(
            cls,
            colliding_key: str,
            new_service: Microservice,
            registry: ServiceRegistry,
    ) -> InsertionResult:
        """
        Process the cases where the service's microservice_name has already been a key.

        Action:
            1.  Send an exception chain in the InsertionResult if the current entry's value
                is different from the service to register.
            2.  Otherwise, increment the registration counter, then send the success result.
        Args:
            colliding_key: str
            new_service: Microservice
            registry: ServiceRegistry
        Returns:
            InsertionResult
        Raises:
            ServiceRegistrationException
            ServiceOpNameCollisionException
        """
        method = f"{cls.__name__}._collision_helper"
        
        # --- Get the microservice which is already using the key. ---#
        old_service = registry.entries[colliding_key]
        
        # Handle the case that the, old and new services are different.
        if old_service.MICROSERVICE_NAME.upper() != new_service.MICROSERVICE_NAME.upper():
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ServiceRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ServiceRegistrationException.MSG,
                    err_code=ServiceRegistrationException.ERR_CODE,
                    ex=ServiceOpNameCollisionException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ServiceOpNameCollisionException.MSG,
                        err_code=ServiceOpNameCollisionException.ERR_CODE,
                        var="var_registered_service",
                        val=old_service,
                    ),
                )
            )
        # --- If the microservices are the same, increment the registration counter ---#
        registry.registration_counters[new_service.MICROSERVICE_NAME] += 1
        
        return InsertionResult.success()
        