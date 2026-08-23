# src/bootstrapper/priming.py

"""
Module: bootstrapper.priming
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TypeVar

from domain.metadata.blueprint import Blueprint
from operation.toolkit import Toolkit
from operation import Operator
from result import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T")

class AssemblyPrimer(Operator[T]):
    DOMAIN = "assembly_primer"
    
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