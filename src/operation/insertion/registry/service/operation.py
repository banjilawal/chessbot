# src/operation/insertion/registry/service/operation.py

"""
Module: operation.insertion.registry.service.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import Microservice
from model import ServiceRegistry
from result import InsertionResult
from util import LoggingLevelRouter
from controller import ServiceRegistryController
from operation import BootstrapServiceRegistration, Insertion
from err import NewServiceRegistrationException, MicroserviceNullException


class RegisterNewService(Insertion[Microservice]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Add an operation to the ServiceRegistry

    Attributes:

    Provides:
        -   def execute(
                service: Microservice,
                registry: ServiceRegistry,
                bootstrap_service_registration: BootstrapServiceRegistration,
            ) -> InsertionResult:

    Super Class:
        Insertion
    """
    NAME = "register_new_service"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            service: Microservice,
            registry: ServiceRegistry,
            null_exception: MicroserviceNullException,
            bootstrap_service_registration: BootstrapServiceRegistration | None = None,
    ) -> InsertionResult:
        """
        Insert a new service to the registry.
        
        Action:
            1.  Send an exception chain in the InsertionResult if the bootstrap fails.
            2.  Otherwise, send the success result.
        Args:
            service: Microservice
            registry: ServiceRegistry
            null_exception: MicroserviceNullException
            bootstrap_service_registration: BootstrapServiceRegistration
        Returns:
            InsertionResult
        Raises:
            NewServiceRegistrationException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if bootstrap_service_registration is None:
            bootstrap_service_registration = BootstrapServiceRegistration()
            
        # Handle the case that, the service is flagged during bootstrapping.
        service_bootstrap_result = bootstrap_service_registration.execute(
            service=service,
            registry=registry,
            null_exception=null_exception,
        )
        if service_bootstrap_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NewServiceRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NewServiceRegistrationException.MSG,
                    err_code=NewServiceRegistrationException.ERR_CODE,
                    ex=service_bootstrap_result.exception
                )
            )
        # --- Complete the insertion steps. ---#
        registry.entries[service.NAME] = service
        registry.registration_counters[service.NAME] += 1
        
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()

# --- FINALLY: REGISTER THE OPERATION ---#
ServiceRegistryController.register_service(service=RegisterNewService)
        