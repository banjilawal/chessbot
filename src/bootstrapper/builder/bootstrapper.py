# src/bootstrapper/builder/bootstrapper.py

"""
Module: bootstrapper.builder.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from bootstrapper import Bootstrapper
from result import BuildResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class BuilderBootstrapper(Bootstrapper, Generic[T]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs, ) -> BuildResult:
        pass