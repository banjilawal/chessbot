# src/chess/square/analyzer/exception/debug/__init__.py

"""
Module: chess.square.analyzer.exception.debug.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_SQUARE_TOKEN_ANALYSIS_ROUTE EXCEPTION #======================#
    "SquareTokenAnalysisRouteException",
]

from chess.system import NoAnalysisRouteException


# ======================# UNHANDLED_SQUARE_TOKEN_ANALYSIS_ROUTE EXCEPTION #======================#
class SquareTokenAnalysisRouteException(NoAnalysisRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that SquareToken analysis failed because there was no analysis route for one of their states.
    
    # PARENT:
        *   NoAnalysisRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SQUARE_TOKEN_ANALYSIS_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SquareToken analysis failed: No analysis route existed for one of their states."