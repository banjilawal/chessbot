# src/chess/system/relation/analysis/wrapper.py

"""
Module: chess.system.relation.analysis.wrapper
Author: Banji Lawal
Created: 2026-12-28
version: 1.0.0
"""

from chess.system import OperationException

__all__ = [
    # ======================# RELATION_ANALYSIS_FAILURE #======================#
    "AnalysisException",
]

# ======================# RELATION_ANALYSIS_FAILURE #======================#
class AnalysisException(OperationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in Analyzer.analysis that, prevented the relation analysis from completing.
        An exception was sent instead of a report.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "RELATION_ANALYSIS_FAILURE"
    MSG = "Relation analysis failed."
