# src/space/builder/register/__init__.py

"""
Module: space.builder.register.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from builder import Builder
from register import Register
from result import BuildResult
from util import LoggingLevelRouter
from validator import Validator

T = TypeVar("T")


class RegisterBuilder(Builder, Generic[T]):
    _endpoint_validator: Validator[T]
    
    def __init__(
            self,
            endpoint_validator: Validator[T]
    ):
        """
        Args:
            endpoint_validator: Validator[T]
        """
        self._endpoint_validator = endpoint_validator
        
    
    @property
    def endpoint_validator(self) -> Validator[T]:
        return self._endpoint_validator
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, a: T, b: T) -> BuildResult[Register[T]]:
        pass
