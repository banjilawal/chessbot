# src/operation/registry/service/operation.py

"""
Module: operation.registry.service.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import abstractmethod

from result import Result
from operation import Operation
from model import ServiceRegistry
from util import LoggingLevelRouter


class ServiceRegistryOperation(Operation[ServiceRegistry]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Execute a ServiceRegistry related state access or mutation task.

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