# src/toolkit/builder/model/rank/toolkit.py

"""
Module: toolkit.builder.model.rank.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import RankAssembler
from model import Rank
from root import RankRootCertifier
from toolkit import ModelBuilderToolkit


class RankBuilderToolkit(ModelBuilderToolkit[Rank]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles RankBuilder dependencies.

    Attributes:
        assembler: Optional[RankAssembler]
        root_certifier: Optional[RankRootCertifier]
            
    Provides:

    Super Class:
        ModelBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[RankAssembler] | None = RankAssembler(),
            root_certifier: Optional[RankRootCertifier] |
                            None = RankRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[RankAssembler]
            root_certifier: Optional[RankRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> RankAssembler:
        return cast(RankAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> RankRootCertifier:
        return cast(RankRootCertifier, super().root_certifier)
    
