# src/chess/rank/service/exception.py

"""
Module: chess.rank.service.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""


from chess.system import ServiceException

__all__ = [
    "RankServiceException",
]


class RankServiceException(ServiceException):
    """
    Super class of exception raised by RankCertifier objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "RankCertifier raised an exception."