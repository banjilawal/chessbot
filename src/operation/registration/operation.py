# src/operation/registration/operation.py

"""
Module: operation.registration.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import abstractmethod

from model import WorkerRegistry
from result import Result
from system import LoggingLevelRouter
from operation import Operation


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