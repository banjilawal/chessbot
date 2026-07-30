# src/builder/pattern/builder.py

"""
Module: builder.pattern.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from blueprint import Blueprint
from builder import Builder
from result import BuildResult
from toolkit import BuilderToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Signature")

class SignatureBuilder(Builder, ABC, Generic[T]):
    
    def __init__(self, builder_toolkit: BuilderToolkit[T]):
        super().__init__(builder_toolkit=builder_toolkit)
        
    @property
    def builder_toolkit(self) -> BuilderToolkit[T]:
        return cast(T, super().builder_toolkit)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
        pass