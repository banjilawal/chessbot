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
    _a: T
    _b: T
    _endpoint_validator: Validator[T]
    
    def __init__(
            self,
            a: T,
            b: T,
            endpoint_validator: Validator[T]
    ):
        """
        Args:
            a: T,
            b: T,
            endpoint_validator: Validator[T]
        """
        self._a = a
        self._b = b
        self._endpoint_validator = endpoint_validator
        
    @property
    def a(self) -> T:
        return self._a
    
    @property
    def b(self) -> T:
        return self._b
    
    @property
    def endpoint_validator(self) -> Validator[T]:
        return self._endpoint_validator
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[Register[T]]:
        pass
