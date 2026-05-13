# src/toolkit/registry/service/toolkit.py

"""
Module: toolkit.registry.service.toolkit_
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from operation import (
    AddServiceBootstrapper, DomainSearchBootstrapper, NameValidator, RegisterService, ServiceRegistryDomainSearch,
    ServiceRegistryNameSearch, ValidationBootstrapper, ServiceRegistryNameSearchBootstrapper
)


@dataclass
class ServiceRegistryToolkit:
    """
    Role:
        -   Utility Container

    Responsibilities:
        1.  Consolidates ServiceRegistry integrity operations and validation resources into
            a single entry point.

    Attributes:
        name_validator: NameValidator
        register_service: RegisterService
        domain_search: RegistryDomainSearch
        service_search: RegistryServiceSearch
        add_service_bootstrapper: AddServiceBootstrapper
        validation_bootstrapper: ValidationBootstrapper
        domain_search_bootstrapper: DomainSearchBootstrapper
        service_search_bootstrapper: ServiceSearchBootstrapper

    Provides:

    Super Class:
    
    Notes:
        -   ServiceRegistry is a repo of operations that can be used in building toolkits.
        -   To avoid side effects ServiceRegistryController does not use the Toolkit subclass for consolidating
            its operations.
        -   To prevent side effects ServiceRegistryController Toolkit subclasses are avoided in
            ServiceRegistryController.
        -   The name is consistent with the toolkit role and responsibilities. despite not being
            a subclass of Toolkit.
    """
    name_validator: NameValidator = NameValidator()
    register_service: RegisterService = RegisterService()
    domain_search: ServiceRegistryDomainSearch = ServiceRegistryDomainSearch()
    service_search: ServiceRegistryNameSearch = ServiceRegistryNameSearch()
    add_service_bootstrapper: AddServiceBootstrapper = AddServiceBootstrapper()
    validation_bootstrapper: ValidationBootstrapper = ValidationBootstrapper()
    domain_search_bootstrapper: DomainSearchBootstrapper = DomainSearchBootstrapper()
    service_search_bootstrapper: ServiceRegistryNameSearchBootstrapper = ServiceRegistryNameSearchBootstrapper()