# src/operation/finalizer/finalizer.py

"""
Module: operation.finalizer.finalizer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from model import Blueprint
from result import BuildResult
from system import LoggingLevelRouter

T = TypeVar("T")


class Finalizer(ABC, Generic[T]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, product: T, blueprint: Blueprint[T]) -> BuildResult[T]:
        pass