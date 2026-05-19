# src/microservice/bootstrap/insertion/registry/service/operation.py

"""
Module: microservice.boostrap.insertion.registry.service.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import Microservice
from model import ServiceRegistry
from result import ValidationResult
from util import LoggingLevelRouter
from controller import ServiceRegistryController
from err import NewServiceRegistrationException, MicroserviceNullException, RegistryKeyCollisionException
from operation import Bootstrap, RegistryEntryNameValidator, ValidationPrimer


class BootstrapServiceRegistration(Bootstrap[Microservice]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Validate a service is a safe Microservice before adding to the ServiceRegistry.

    Attributes:

    Provides:
        -   def execute(
                service: Microservice,
                registry: ServiceRegistry,
                null_exception: MicroserviceNullException,
                validation_primer: ValidationPrimer,
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
            validation_primer: ValidationPrimer | None = None,
            registry_entry_name_validator: RegistryEntryNameValidator| None = None,
    ) -> ValidationResult[Microservice]:
        """
        validate a service before adding it to ServiceRegistry.
        
        Action:
            1.  Send an exception chain in the ValidationResult if either condition occurs.
                    -   The service is not an Microservice.
                    -   Either, service.DOMAIN or service.NAME are not safe Strings.
                    -   The service's name has already been used in the domain.
            2.  Otherwise, send the success result.
        Args:
            service: Microservice
            registry: ServiceRegistry
            null_exception: MicroserviceNullException
            validation_primer: ValidationPrimer
            registry_entry_name_validator: RegistryEntryNameValidator
        Returns:
            ValidationResult[Microservice]
        Raises:
            NewServiceRegistrationException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if null_exception is None:
            null_exception = MicroserviceNullException()
        if validation_primer is None:
            validation_primer = ValidationPrimer()
        if registry_entry_name_validator is None:
            registry_entry_name_validator = RegistryEntryNameValidator()
        
        # Handle the case that, the service is not a valid microservice.
        service_validation_result = validation_primer.validate(
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
        key_validation_result = registry_entry_name_validator.validate(
            candidates=[service.NAME],
            validation_primer=validation_primer,
        )
        if key_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NewServiceRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NewServiceRegistrationException.MSG,
                    err_code=service_validation_result.ERR_CODE,
                    ex=key_validation_result.exception,
                )
            )
        # Handle the case that, the service's name has already been used in the domain.
        if service.NAME in registry.entries.keys():
            name_collision_result = cls._name_collision_helper(
                target=service,
                registry=registry,
            )
            if name_collision_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NewServiceRegistrationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=NewServiceRegistrationException.MSG,
                        err_code=service_validation_result.ERR_CODE,
                        ex=name_collision_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(service)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _name_collision_helper(
            cls,
            target: Microservice,
            registry: ServiceRegistry,
    ) -> ValidationResult[Microservice]:
        """
        Process the cases where the service's microservice_name has already been a key.

        Action:
            1.  If the service's name is being used by a different service in the domain send an
                exception chain in the ValidationResult.
            2.  Otherwise, send the success result.
        Args:
            target: Microservice
            registry: ServiceRegistry
        Returns:
            ValidationResult[Microservice]
        Raises:
            RegistryKeyCollisionException
        """
        method = f"{cls.__name__}._name_collision_helper"
        
        # Search for the registry using the service's domain and name.
        registered_service = registry.entries[target.NAME]
        
        # Handle the case that, the registered_service's type differs from the target's
        if not isinstance(type(registered_service), type(target)):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RegistryKeyCollisionException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=RegistryKeyCollisionException.MSG,
                        err_code=RegistryKeyCollisionException.ERR_CODE,
                        var=f"shared_key={target.NAME}",
                        val=f"registered_service_type=f{type(registered_service).__name__}",
                    )
                )
        # --- Otherwise, the target and the registered_service are the same. Return success. ---#
        return ValidationResult.success(target)

# --- FINALLY: REGISTER THE MICROSERVICE ---#
ServiceRegistryController.register_service(service=BootstrapServiceRegistration)
        