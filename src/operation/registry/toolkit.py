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
    name_validator: NameValidator = NameValidator()
    register_worker: RegisterWorker = RegisterWorker()
    domain_search: RegistryDomainSearch = RegistryDomainSearch()
    worker_search: RegistryWorkerSearch = RegistryWorkerSearch()
    add_worker_bootstrapper: AddWorkerBootstrapper = AddWorkerBootstrapper()
    validation_bootstrapper: ValidationBootstrapper = ValidationBootstrapper()
    domain_search_bootstrapper: DomainSearchBootstrapper = DomainSearchBootstrapper()
    worker_search_bootstrapper: WorkerSearchBootstrapper = WorkerSearchBootstrapper()