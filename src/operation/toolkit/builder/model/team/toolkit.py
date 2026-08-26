# src/operation/toolkit/builder/model/team/toolkit.py

"""
Module: operation.toolkit.builder.model.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import TeamAssembler
from domain.model import Team
from assurance.validator import TeamRootCertifier
from operation.toolkit.builder.model.team.toolkit import ModelBuilderToolkit


class TeamBuilderToolkit(ModelBuilderToolkit[Team]):
    """
    Role:
        -  Dependency Management
        
    Responsibilities:
        1.  Bundles TeamBuilder dependencies.

    Attributes:
        assembler: Optional[TeamAssembler]
        root_certifier: Optional[TeamRootCertifier]
            
    Provides:

    Super Class:
        ModelBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[TeamAssembler] | None = TeamAssembler(),
            root_certifier: Optional[TeamRootCertifier] |
                            None = TeamRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[TeamAssembler]
            root_certifier: Optional[TeamRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> TeamAssembler:
        return cast(TeamAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> TeamRootCertifier:
        return cast(TeamRootCertifier, super().integrity_checker)
    
