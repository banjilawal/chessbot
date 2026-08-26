# src/transit/dispatcher/builder/pattern/offset/knight/dispatcher/builder.py

"""
Module: transit.dispatcher.builder.pattern.offset.knight.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from transit.dispatcher.builder import OffsetBuilder
from topology.pattern import KnightSignature
from artifcat import BuildResult
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
        return cast(KnightSignatureBuilderToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, builder:KnightSignatureBuilder) -> BuildResult[KnightSignature]:
        method = f"{self.__class__.__name__}"
    
