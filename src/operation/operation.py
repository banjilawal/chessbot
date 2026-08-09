# src/operation/operation.py

"""
Module: operation.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from authorization import Request


T = TypeVar("T", bound="Result")

class Operation(ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a task on a data-holding object or collection of data-holders.
        2.  The task produces a work product encapsulated in a Result object.

    Attributes:

    Provides:
        -   execute(request: Request[T]) -> T

    Super Class:
    """
    
    @classmethod
    def execute(cls, request: Request[T]) -> T:
        pass