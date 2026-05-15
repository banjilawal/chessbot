# src/toolkit/registry/service/toolkit.py

"""
Module: toolkit.registry.service.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from operation import RegisterNewService
from search import ServiceRegistrySearch


@dataclass
class ServiceRegistryToolkit:
    """
    Role:
        -   Utility Container

    Responsibilities:
        1.  Consolidates ServiceRegistry integrity operations and validation resources into
            a single entry point.

    Attributes:
        register_new_service: RegisterNewService
        service_registry_search: ServiceRegistryNameSearch

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
    register_new_service: RegisterNewService
    service_registry_search: ServiceRegistrySearch