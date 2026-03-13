# src/logic/node/tree/builder/builder.py

"""
Module: logic.node.tree.builder.builder
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from logic.node import NodeService, NodeTree
from logic.span import SquareSpan
from logic.system import BuildResult, Builder, LoggingLevelRouter


class NodeTreeBuilder(Builder[NodeTree]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            square_span: SquareSpan,
            node_service: NodeService = NodeService(),
            square_span_service: SquareSpanService(),
    ) -> BuildResult[NodeTreeBuilder]: