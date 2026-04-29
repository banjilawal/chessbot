# src/operation/bootstrap/bootstrap.py

"""
Module: operation.bootstrap.bootstrap
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TypeVar

from toolkit import Toolkit
from model import Blueprint
from operation import Operation
from result import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T")

class AssemblyBootstrapper(Operation[T]):
    DOMAIN = "assembly_bootstrapper"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            blueprint: Blueprint[T],
            toolkit: Toolkit[T],
            *args,
            **kwargs,
    ) -> ValidationResult[Blueprint[T]]:
        pass