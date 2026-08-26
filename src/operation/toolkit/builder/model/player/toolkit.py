# src/operation/toolkit/builder/model/player/toolkit.py

"""
Module: operation.toolkit.builder.model.player.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import PlayerAssembler
from domain.model import Player
from assurance.validator import PlayerRootCertifier
from operation.toolkit.builder.model.player.toolkit import ModelBuilderToolkit


class PlayerBuilderToolkit(ModelBuilderToolkit[Player]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles PlayerBuilder dependencies.

    Attributes:
        assembler: Optional[PlayerAssembler]
        root_certifier: Optional[PlayerRootCertifier]
            
    Provides:

    Super Class:
        ModelBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[PlayerAssembler] | None = PlayerAssembler(),
            root_certifier: Optional[PlayerRootCertifier] |
                            None = PlayerRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[PlayerAssembler]
            root_certifier: Optional[PlayerRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> PlayerAssembler:
        return cast(PlayerAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> PlayerRootCertifier:
        return cast(PlayerRootCertifier, super().integrity_checker)
    
