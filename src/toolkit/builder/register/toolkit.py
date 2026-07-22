# src/toolkit/builder/register/toolkit.py

"""
Module: toolkit.builder.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from assembler import RegisterAssembler
from root import RegisterRootCertifier
from toolkit import BuilderToolkit

T = TypeVar("T", bound="Register")

class RegisterBuilderToolkit(BuilderToolkit, Generic[T]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider
        
    Responsibilities:
        1.  Aggregates workers and services an entity requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        assembler: Assembler[T],
        root_certifier: RootCertifier[T]
        
    Provides:
    
    Super Class:
        Toolkit
    """
    _assembler: [RegisterAssembler[T]]
    _root_certifier: [RegisterRootCertifier[T]]
    
    def __init__(
            self,
            assembler: [RegisterAssembler[T]],
            root_certifier: [RegisterRootCertifier[T]],
    ):
        """
        Args:
            assembler: Assembler[T],
            root_certifier: RootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

        
    @property
    def assembler(self) -> [RegisterAssembler[T]]:
        return cast([RegisterAssembler[T]], super()._assembler)
        
    @property
    def root_certifier(self) -> [RegisterRootCertifier[T]]:
        return cast([RegisterRootCertifier[T]], self._root_certifier)