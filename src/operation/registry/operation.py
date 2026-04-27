# src/operation/finalize/operation.py

"""
Module: operation.finalize.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from model import Blueprint
from operation import Operation
from result import BuildResult, Result
from system import LoggingLevelRouter

T = TypeVar("T")


class ControllerOperation(Operation[Operation]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, product: T, blueprint: Blueprint[T]) -> Result[T]:
        pass