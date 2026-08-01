# src/toolkit/builder/register/toolkit.py

"""
Module: toolkit.builder.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from fabrication.assembler import RegisterAssembler
from assurance.certifier import RegisterCertifier
from toolkit import BuilderToolkit

T = TypeVar("T", bound="Register")

class RegisterBuilderToolkit(BuilderToolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles RegisterBuilder dependencies.

    Attributes:
        assembler: [RegisterAssembler[T]],
        root_certifier: [RegisterRootCertifier[T]]
        
    Provides:
    
    Super Class:
        BuilderToolkit
    """
    
    def __init__(
            self,
            assembler: [RegisterAssembler[T]],
            root_certifier: [RegisterCertifier[T]],
    ):
        """
        Args:
            assembler: [RegisterAssembler[T]],
            root_certifier: [RegisterRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

        
    @property
    def assembler(self) -> [RegisterAssembler[T]]:
        return cast([RegisterAssembler[T]], super()._assembler)
        
    @property
    def root_certifier(self) -> [RegisterCertifier[T]]:
        return cast([RegisterCertifier[T]], super()._root_certifier)