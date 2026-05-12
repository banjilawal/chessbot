# src/operation/registry/worker/toolit.py

"""
Module: operation.registry.worker.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from operation import (
    AddWorkerBootstrapper, DomainSearchBootstrapper, NameValidator, RegisterWorker, WorkerRegistryDomainSearch,
    WorkerRegistryNameSearch, ValidationBootstrapper, WorkerRegistryNameSearchBootstrapper
)


@dataclass
class WorkerRegistryToolkit:
    """
    Role:
        -   Utility Container

    Responsibilities:
        1.  Consolidates WorkerRegistry integrity operations and validation resources into
            a single entry point.

    Attributes:
        name_validator: NameValidator
        register_worker: RegisterWorker
        domain_search: RegistryDomainSearch
        worker_search: RegistryWorkerSearch
        add_worker_bootstrapper: AddWorkerBootstrapper
        validation_bootstrapper: ValidationBootstrapper
        domain_search_bootstrapper: DomainSearchBootstrapper
        worker_search_bootstrapper: WorkerSearchBootstrapper

    Provides:

    Super Class:
    
    Notes:
        -   WorkerRegistry is a repo of operations that can be used in building toolkits.
        -   To avoid side effects WorkerRegistryController does not use the Toolkit subclass for consolidating
            its operations.
        -   To prevent side effects WorkerRegistryController Toolkit subclasses are avoided in
            WorkerRegistryController.
        -   The name is consistent with the toolkit role and responsibilities. despite not being
            a subclass of Toolkit.
    """
    name_validator: NameValidator = NameValidator()
    register_worker: RegisterWorker = RegisterWorker()
    domain_search: WorkerRegistryDomainSearch = WorkerRegistryDomainSearch()
    worker_search: WorkerRegistryNameSearch = WorkerRegistryNameSearch()
    add_worker_bootstrapper: AddWorkerBootstrapper = AddWorkerBootstrapper()
    validation_bootstrapper: ValidationBootstrapper = ValidationBootstrapper()
    domain_search_bootstrapper: DomainSearchBootstrapper = DomainSearchBootstrapper()
    worker_search_bootstrapper: WorkerRegistryNameSearchBootstrapper = WorkerRegistryNameSearchBootstrapper()