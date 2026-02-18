# src/chess/graph/edge/builder/exception/wrapper.py

"""
Module: chess.graph.edge.builder.exception.wrapper
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""


from chess.system import BuildFailedException

__all__ = [
    # ======================# EDGE_BUILD_FAILURE EXCEPTION #======================#
    "EdgeBuildFailedException",
]


class EdgeBuildFailedException(BuildFailedException):
    pass