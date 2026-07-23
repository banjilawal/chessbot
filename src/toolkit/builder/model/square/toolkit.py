# src/toolkit/builder/model/square/toolkit.py

"""
Module: toolkit.builder.model.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import SquareAssembler
from model import Square
from root import SquareRootCertifier
from toolkit import ModelBuilderToolkit


class SquareBuilderToolkit(ModelBuilderToolkit[Square]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles SquareBuilder dependencies.

    Attributes:
        assembler: Optional[SquareAssembler]
        root_certifier: Optional[SquareRootCertifier]
            
    Provides:

    Super Class:
        ModelBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[SquareAssembler] | None = SquareAssembler(),
            root_certifier: Optional[SquareRootCertifier] |
                            None = SquareRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[SquareAssembler]
            root_certifier: Optional[SquareRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> SquareAssembler:
        return cast(SquareAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> SquareRootCertifier:
        return cast(SquareRootCertifier, super().root_certifier)
    
