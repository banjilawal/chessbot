# src/chess/system/resolution/service.py


"""
module: chess.system.resolution.service
author: Banji Lawal
date: 2025-11-20
version: 0.0.1
"""
from chess import ServiceException


class ResolutionServiceException(ServiceException):
    ERROR_CODE = "RESOLUTION_SERVICE_ERROR"
    DEFAULT_MESSAGE = "ResolutionService raised an exception."