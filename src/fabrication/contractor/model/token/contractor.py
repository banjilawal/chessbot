# src/fabrication/contractor/model/token/contractor.py

"""
Module: fabrication.contractor.model.token.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import BuildResult
from domain import Token, TokenBlueprint
from fabrication import ModelBuildSubcontractor
from util import LoggingLevelRouter

T = TypeVar("T", bound="Token")

class TokenSubcontractor(ModelBuildSubcontractor[T], ABC, Generic[T]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Instantiate a concrete Token.

    Attributes:

    Provides:
            -   def execute(blueprint: TokenBlueprint[T]) -> BuildResult[T]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint[T]) -> BuildResult[T]:
        """
        Routes a TokenBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: TokenBlueprint[T]
        Returns:
            BuildResult[T]
        Raises:
            TokenSubcontractorException
        """
        pass