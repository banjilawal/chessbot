# src/builder/pattern/offset/knight/builder.py

"""
Module: builder.pattern.offset.knight.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import OffsetBuilder
from pattern import KnightSignature
from result import BuildResult
from util import LoggingLevelRouter


class KnightOffsetBuilder(OffsetBuilder[KnightSignature]):
    
    def __init__(self, builder_toolkit: Optional[KnightSignatureBuilderToolkit]):
        """
        Args:
            builder_toolkit: Optional[KnightSignatureBuilderToolkit]
        """
        super().__init__(builder_tookit=builder_toolkit or KnightSignatureBuilderToolkit())
        
        
    @property
    def builder_toolkit(self) -> KnightSignatureBuilderToolkit:
        return cast(KnightSignatureBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint:KnightSignatureBlueprint) -> BuildResult[KnightSignature]:
        method = f"{self.__class__.__name__}"
    
