# src/pipeline/pipeline.py

"""
Module: pipeline.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from result import Result
from system import LoggingLevelRouter

T = TypeVar("T")

class Pipeline(ABC, Generic[T]):
    pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def run(self, *args, **kwargs) -> Result:
        pass
    
    # @classmethod
    # @abstractmethod
    # @LoggingLevelRouter.monitor
    # def enter(cls, *args, **kwargs) -> Result[Any]:
    #     pass
    #
    # @classmethod
    # @abstractmethod
    # @LoggingLevelRouter.monitor
    # def exit(cls, *args, **kwargs) -> Result[T]:
    #     pass