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

from core.certifier import Certifier
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
    _root_certifier: Certifier[T]
    
    def __init__(self, assembler: Assembler[T], root_certifier: Certifier[T], ):
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
    def root_certifier(self) -> Certifier[T]:
        return self._root_certifier