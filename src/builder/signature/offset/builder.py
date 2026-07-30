# src/blueprint/pattern/offset/blueprint.py

"""
Module: blueprint.pattern.offset.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from blueprint import SignatureBlueprint
from util import LoggingLevelRouter

T = TypeVar("T", bound="OffsetSignature")

class OffsetBlueprint(SignatureBlueprint, Generic[T]):
    
    def __init__(self, blueprint_toolkit: OffsetBlueprintToolkit[T]):
        super().__init__(blueprint_toolkit=blueprint_toolkit)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: OffsetSignatureBlueprint[T]) -> BuildResult[OffsetSignature[T]]:
        pass

    
    
    