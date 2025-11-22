# src/chess/coord/context/builder/exception.py

"""
Module: ches.coord.context.builder.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import SearchContextException


__all__ = [
    "SearchContextBuildFailedException",
]

# ======================# SEARCH_CONTEXT BUILD EXCEPTIONS #======================#
class SearchContextBuildFailedException(SearchContextException, BuildFailedException):
    """
    Raised when SearchContextBuilder encounters an error while building team_name team_name.
    Exists primarily to catch all exceptions raised builder team_name new searchContext
    """
    ERROR_CODE = "SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "SearchContext build failed."