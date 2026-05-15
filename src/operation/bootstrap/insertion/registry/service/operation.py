# src/microservice/bootstrap/insertion/registry/service/microservice.py

"""
Module: microservice.boostrap.insertion.registry.service.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import MicroserviceNullException, NewServiceRegistrationException, RegistryKeyCollisionException
from microservice import Microservice
from model import ServiceRegistry
from operation import RegistryEntryNameValidator, ValidationBootstrapper
from result import ValidationResult
from util import LoggingLevelRouter
from controller import ServiceRegistryController



class BootstrapServiceRegistration(ServiceRegistry):
    """
    Role
        -   Service

    Responsibilities:
        1.  Validate a service is a safe Microservice before adding to the ServiceRegistry.
        2.  Detect key collisions in the before attempting to add a new entry in a Service Domain.

    Attributes:

    Provides:
        -   def execute(
                service: Microservice,
                registry: ServiceRegistry,
                null_exception: MicroserviceNullException,
                validation_bootstrapper: ValidationBootstrapper,
                registry_entry_name_validator: RegistryEntryNameValidator\,
            ) -> ValidationResult[Microservice]:

    Super Class:
        ServiceRegistryMicroservice
    """
    NAME = "insert_service"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            service: Microservice,
            registry: ServiceRegistry,
            null_exception: MicroserviceNullException | None = None,
            validation_bootstrapper: ValidationBootstrapper | None = None,
            registry_entry_name_validator: RegistryEntryNameValidator| None = None,
    ) -> ValidationResult[Microservice]:
        """
        validate a service before adding it to ServiceRegistry.
        
        Action:
            1.  Send an exception chain in the ValidationResult if either condition occurs.
                    -   The service is not anMicroservice.
                    -   The service.NAME are not safe Strings.
                    -   The service's name has already been used in the domain.
            2.  Otherwise, send the success result.
        Args:
            service: Microservice
            registry: ServiceRegistry
            null_exception: MicroserviceNullException
            validation_bootstrapper: ValidationBootstrapper
            registry_entry_name_validator: RegistryEntryNameValidator
        Returns:
            ValidationResult[Microservice
        Raises:
            NewServiceRegistrationException
            RegistryKeyCollisionException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies ---#
        if null_exception is None:
            null_exception = MicroserviceNullException()
        if validation_bootstrapper is None:
            validation_bootstrapper = ValidationBootstrapper()
        if registry_entry_name_validator is None:
            registry_entry_name_validator = RegistryEntryNameValidator()
        
        # Handle the case that, the service is not a valid microservice.
        service_validation_result = validation_bootstrapper.validate(
            candidate=service,
            target_model=Microservice,
            null_exception=null_exception,
        )
        if service_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NewServiceRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NewServiceRegistrationException.MSG,
                    err_code=service_validation_result.ERR_CODE,
                    ex=service_validation_result.exception,
                )
            )
        # Handle the case that, either the service's domain or name are not good strings.
        keys_validation_result = registry_entry_name_validator.validate(
            candidates=[service.NAME],
            validation_bootstrapper=validation_bootstrapper,
        )
        if keys_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NewServiceRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NewServiceRegistrationException.MSG,
                    err_code=service_validation_result.ERR_CODE,
                    ex=keys_validation_result.exception,
                )
            )
        # Handle the case that, the service's name has already been used in the domain.
        if service.NAME in registry.entries.keys():
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NewServiceRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NewServiceRegistrationException.MSG,
                    err_code=service_validation_result.ERR_CODE,
                    ex=RegistryKeyCollisionException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=RegistryKeyCollisionException.MSG,
                        err_code=RegistryKeyCollisionException.ERR_CODE,
                        var="microservice_name",
                        val=service.NAME,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(service)

# --- FINALLY: REGISTER THE MICROSERVICE ---#
ServiceRegistryController.register(service=BootstrapServiceRegistration)
        