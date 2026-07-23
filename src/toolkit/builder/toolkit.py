# src/toolkit/builder/toolkit.py

"""
Module: toolkit.builder.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from assembler import Assembler
from bootstrapper import PrimingValidator, EntityCarrierValidator
from microservice import IdentityService
from root import RootCertifier
from toolkit import Toolkit

T = TypeVar("T")

class BuilderToolkit(Toolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles Builder dependencies.

    Attributes:
        assembler: Assembler[T],
        root_certifier: RootCertifier[T]
        
    Provides:
    
    Super Class:
        Toolkit
    """
    _assembler: Assembler[T]
    _root_certifier: RootCertifier[T]
    
    def __init__(
            self,
            assembler: Assembler[T],
            root_certifier: RootCertifier[T],
    ):
        """
        Args:
            assembler: Assembler[T],
            root_certifier: RootCertifier[T]
        """
        super().__init__()
        self._assembler = assembler
        self._root_certifier = root_certifier
        
    @property
    def assembler(self) -> Assembler[T]:
        return self._assembler
    
    @property
    def root_certifier(self) -> RootCertifier[T]:
        return self._root_certifier