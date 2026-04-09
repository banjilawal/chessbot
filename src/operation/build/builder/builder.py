# src/operation/builder/builder.py

"""
Module: operation.builder.builder
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

class Builder(ABC, Generic[T]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls,blueprint: Blueprint[T], *args, **kwargs ) -> BuildResult[T]:
        pass