# src/operation/registry/worker/insert/operation.py

"""
Module: operation.registry.worker.insert.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import WorkerRegistry
from result import InsertionResult
from util import LoggingLevelRouter
from err import NewWorkerRegistrationException
from controller import WorkerRegistryController
from operation import BootstrapWorkerRegistration, Insertion, Operation


class RegisterNewWorker(Insertion[Operation]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Add an operation to the WorkerRegistry

    Attributes:

    Provides:
        -   def execute(
                worker: Operation,
                registry: WorkerRegistry,
                bootstrap_worker_registration: BootstrapWorkerRegistration,
            ) -> InsertionResult:

    Super Class:
        Insertion
    """
    NAME = "register_new_worker"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            worker: Operation,
            registry: WorkerRegistry,
            bootstrap_worker_registration: BootstrapWorkerRegistration | None = None,
    ) -> InsertionResult:
        """
        Insert a new worker to the registry.
        
        Action:
            1.  Send an exception chain in the InsertionResult if the bootstrap fails.
            2.  Otherwise, send the success result.
        Args:
            worker: Operation
            registry: WorkerRegistry
            bootstrap_worker_registration: BootstrapWorkerRegistration
        Returns:
            InsertionResult
        Raises:
            NewWorkerRegistrationException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies ---#
        if bootstrap_worker_registration is None:
            bootstrap_worker_registration = BootstrapWorkerRegistration()
            
        # Handle the case that, the worker is flagged during bootstrapping.
        worker_bootstrap_result = bootstrap_worker_registration.execute(
            worker=worker,
            registry=registry,
        )
        if worker_bootstrap_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                NewWorkerRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NewWorkerRegistrationException.MSG,
                    err_code=NewWorkerRegistrationException.ERR_CODE,
                    ex=worker_bootstrap_result.exception
                )
            )
        # --- Complete the insertion steps. ---#
        registry.entries[worker.DOMAIN][worker.NAME] = worker
        registry.registration_counters[worker.DOMAIN][worker.NAME] += 1
        
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register(worker=RegisterNewWorker)
        