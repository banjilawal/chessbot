# src/fabrication/builder/fabrication/builder.py

"""
Module: fabrication.builder.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from pip._internal.wheel_builder import BuildResult

from fabrication import Builder, NodeBlueprint
from domain.structure.node import SquareNode
from util import LoggingLevelRouter


class NodeTreeBuilder(Builder[SquareNode]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create an object from the safe blueprint.

    Attributes:

    Provides:
        - def execute(blueprint: Blueprint[T]) -> BuildResult[T]

    Super Class:
    """
    
    def __init__(self):
        super().__init__()
    

    @LoggingLevelRouter.monitor
    def execute(self, blueprint: NodeBlueprint) -> BuildResult[SquareNode]:
        method = f"{self.__class__.__name__}.execute"
        
        tree = blueprint.tree
        for branch in tree.branches:
            cursor = branch[0]
            next = cursor
            while