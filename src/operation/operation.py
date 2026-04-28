# src/operation/__ini__.py

"""
Module: operation.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar

from result import Result

T = TypeVar("T")

class Operation(ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Executes a task on a data-holding object or collection of data-holders.
        2.  The task produces a work product encapsulated in a Result object.

    Attributes:
        DOMAIN = "operation"
        OPERATION_NAME = "operation"

    Provides:
        -   def domains(self) -> List[str]:

    Super Class:
    """
    DOMAIN = "operation"
    OPERATION_NAME = "operation"
    
    @classmethod
    def execute(cls, *args, **kwargs) -> Result[Any]:
        pass