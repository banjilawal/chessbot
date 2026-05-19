# src/toolkit/registry/worker/toolkit.py

"""
Module: toolkit.registry.worker.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from operation import RegisterNewWorker
from search import WorkerRegistryDomainSearch, WorkerRegistryNameSearch


@dataclass
class WorkerRegistryToolkit:
    """
    Role:
        -   Dependency Container

    Responsibilities:
        1.  Consolidates WorkerRegistry integrity operations and validation resources into
            a single entry point.

    Attributes:
        register_new_worker: RegisterNewWorker
        worker_registry_domain_search: WorkerRegistryDomainSearch
        worker_registry_name_search: WorkerRegistryNameSearch

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
    register_new_worker: RegisterNewWorker
    worker_registry_domain_search: WorkerRegistryDomainSearch
    worker_registry_name_search: WorkerRegistryNameSearch