# src/operation/registry/operation.py

"""
Module: operation.registry.operation
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
    DOMAIN = "worker_registry"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs) -> Result:
        pass