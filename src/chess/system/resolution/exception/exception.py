# src/chess/system/resolution/exception.py

"""
module: chess.system.resolution.exception
author: Banji Lawal
date: 2025-11-20
version: 0.0.1
"""


from chess.system import ChessException, ServiceException

__all__ = [
    "ResolutionServiceException",
    "ResolutionException"
]


class ResolutionServiceException(ServiceException):
    ERROR_CODE = "RESOLUTION_SERVICE_ERROR"
    DEFAULT_MESSAGE = "ResolutionService raised an exception."


class ResolutionException(ChessException):
    ERROR_CODE = "RESOLUTION_FAILED_ERROR"
    DEFAULT_MESSAGE = "Resolution raised an exception."



