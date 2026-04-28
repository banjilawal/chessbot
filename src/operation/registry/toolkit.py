# src/operation/registry/toolkit.py

"""
Module: operation.registry.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from operation import (
    AddWorkerBootstrapper, DomainSearchBootstrapper, NameValidator, RegisterWorker, RegistryDomainSearch,
    RegistryWorkerSearch, ValidationBootstrapper, WorkerSearchBootstrapper
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
    """
    name_validator: NameValidator = NameValidator()
    register_worker: RegisterWorker = RegisterWorker()
    domain_search: RegistryDomainSearch = RegistryDomainSearch()
    worker_search: RegistryWorkerSearch = RegistryWorkerSearch()
    add_worker_bootstrapper: AddWorkerBootstrapper = AddWorkerBootstrapper()
    validation_bootstrapper: ValidationBootstrapper = ValidationBootstrapper()
    domain_search_bootstrapper: DomainSearchBootstrapper = DomainSearchBootstrapper()
    worker_search_bootstrapper: WorkerSearchBootstrapper = WorkerSearchBootstrapper()