# src/space/builder/register/__init__.py

"""
Module: space.builder.register.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from ensurepip import bootstrap
from typing import Generic, TypeVar

from assembler import RegisterAssembler
from blueprint import Blueprint
from builder import Builder
from result import BuildResult
from root import RegisterRootCertifier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")


class RegisterBuilder(Builder, Generic[T]):
    """
    Role
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Register instance is born safe and reliable.

    Attributes:
            assembler: [RegisterAssembler[T]],
            bootstrapper: [RegisterRootCertifier[T]]

    Provides:
        -   def execute(self, blueprint: RegisterBlueprint[T]) -> BuildResult[Register]

     Super Class:
         Builder
     """
    
    def __init__(
            self, 
            assembler: [RegisterAssembler[T]],
            bootstrapper: [RegisterRootCertifier[T]],
    ):
        """
        Args:
            assembler: [RegisterAssembler[T]],
            bootstrapper: [RegisterRootCertifier[T]]            
        """
        super().__init__(bootstrapper=bootstrapper, assembler=assembler)
        
    @property
    def bootstrapper(self) -> RegisterRootCertifier[T]:
        return cast(RegisterRootCertifier[T], super().bootstrapper)
    
    @property
    def assembler(self) -> RegisterAssembler[T]:
        return cast(RegisterAssembler, super().assembler)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
        pass