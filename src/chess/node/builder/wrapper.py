# src/chess/node/builder/wrapper.py

"""
Module: chess.node.builder.wrapper
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.graph import NodeException
from chess.system import BuildFailedException

__all__ = [
    # ======================# NODE_BUILD_FAILURE EXCEPTION #======================#
    "NodeBuildFailedException",
]


class NodeBuildFailedException(NodeException, BuildFailedException):
    pass