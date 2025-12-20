# src/chess/dyad/builder/exception.py

"""
Module: chess.dyad.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.dyad import SchemaAgentPairException

class SchemaAgentPairBuildFailedException(SchemaAgentPairException, BuildFailedException):
    pass