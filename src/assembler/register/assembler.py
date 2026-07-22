# src/assembler/register/assembler.py

"""
Module: assembler.register.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from assembler import Assembler
from blueprint import RegisterBlueprint
from result import BuildResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="Register")

class RegisterAssembler(Assembler, Generic[T]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a Register instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: RegisterBlueprint[T],) -> BuildResult[T]

    Super Class:
        Assembler
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: RegisterBlueprint[T],) -> BuildResult[T]:
        pass