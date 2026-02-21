# src/chess/edge/builder/exception/wrapper.py

"""
Module: chess.edge.builder.exception.wrapper
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""


from chess.system import BuildException

__all__ = [
    # ======================# EDGE_BUILD_FAILURE EXCEPTION #======================#
    "EdgeBuildException",
]


class EdgeBuildException(BuildException):
    pass