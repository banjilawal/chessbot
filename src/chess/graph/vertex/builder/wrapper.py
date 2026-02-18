# src/chess/graph/vertex/builder/wrapper.py

"""
Module: chess.graph.vertex.builder.wrapper
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.graph import VertexException
from chess.system import BuildFailedException


class VertexBuildFailedException(VertexException, BuildFailedException):
    pass