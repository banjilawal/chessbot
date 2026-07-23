# src/toolkit/builder/model/arena/toolkit.py

"""
Module: toolkit.builder.model.arena.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import ArenaAssembler
from model import Arena
from root import ArenaRootCertifier
from toolkit import ModelBuilderToolkit


class ArenaBuilderToolkit(ModelBuilderToolkit[Arena]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles ArenaBuilder dependencies.

    Attributes:
        assembler: Optional[ArenaAssembler]
        root_certifier: Optional[ArenaRootCertifier]
            
    Provides:

    Super Class:
        ModelBuildToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[ArenaAssembler] | None = ArenaAssembler(),
            root_certifier: Optional[ArenaRootCertifier] |
                            None = ArenaRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[ArenaAssembler]
            root_certifier: Optional[ArenaRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> ArenaAssembler:
        return cast(ArenaAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> ArenaRootCertifier:
        return cast(ArenaRootCertifier, super().root_certifier)
    
