# src/operation/registry/worker/operation.py

"""
Module: operation.registry.worker.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import abstractmethod

from result import Result
from operation import Operation
from model import WorkerRegistry
from util import LoggingLevelRouter


class WorkerRegistryOperation(Operation[WorkerRegistry]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a WorkerRegistry related state access or mutation task.

    Attributes:
        DOMAIN = "registration"

    Provides:
        -   def domains(self) -> List[str]:

    Super Class:
    """
    DOMAIN = "registration"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs) -> Result:
        pass