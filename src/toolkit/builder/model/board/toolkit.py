# src/toolkit/builder/model/board/toolkit.py

"""
Module: toolkit.builder.model.board.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.assembler import BoardAssembler
from domain.model import Board
from assurance.checker import BoardRootCertifier
from toolkit.builder.model.board.toolkit import ModelBuilderToolkit


class BoardBuilderToolkit(ModelBuilderToolkit[Board]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles BoardBuilder dependencies.

    Attributes:
        assembler: Optional[BoardAssembler]
        root_certifier: Optional[BoardRootCertifier]
            
    Provides:

    Super Class:
        ModelBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[BoardAssembler] | None = BoardAssembler(),
            root_certifier: Optional[BoardRootCertifier] |
                            None = BoardRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[BoardAssembler]
            root_certifier: Optional[BoardRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> BoardAssembler:
        return cast(BoardAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> BoardRootCertifier:
        return cast(BoardRootCertifier, super().integrity_checker)
    
