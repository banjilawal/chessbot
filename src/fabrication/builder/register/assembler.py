# src/fabrication/builder/register/fabrication/builder.py

"""
Module: fabrication.builder.register.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from fabrication.builder import Builder
from domain.metadata.blueprint import RegisterBlueprint
from artifcat import BuildResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="Register")

class RegisterBuilder(Builder, Generic[T]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a Register instance from the safe blueprint.

    Attributes:

    Provides:
        - def execute(self, blueprint: RegisterBlueprint[T],) -> BuildResult[T]

    Super Class:
        Builder
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: RegisterBlueprint[T],) -> BuildResult[T]:
        pass