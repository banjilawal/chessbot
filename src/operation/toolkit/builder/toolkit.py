# src/operation/toolkit/builder/toolkit.py

"""
Module: operation.toolkit.builder.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Generic, TypeVar

from fabrication.builder import Builder

from assurance.validator import Certifier
from operation.toolkit.builder.toolkit import Toolkit

T = TypeVar("T")

class BuilderToolkit(Toolkit, Generic[T]):
    """
    Role:
        -  Dependency Management
        
    Responsibilities:
        1.  Bundles Builder dependencies.

    Attributes:
        assembler: Assembler[T],
        root_certifier: RootCertifier[T]
        
    Provides:
    
    Super Class:
        Toolkit
    """
    _entry: Dict[str, Any] = {}
    _assembler: Builder[T]
    _root_certifier: Certifier[T]
    
    def __init__(self, assembler: Builder[T], root_certifier: Certifier[T], ):
        """
        Args:
            assembler: Assembler[T],
            root_certifier: RootCertifier[T]
        """
        super().__init__()
        self._entry = {
            "assembler": assembler,
            "root_certifier": root_certifier,
        }
        self._assembler = assembler
        self._root_certifier = root_certifier
        
    @property
    def assembler(self) -> Builder[T]:
        return self._assembler
    
    @property
    def root_certifier(self) -> Certifier[T]:
        return self._root_certifier
    