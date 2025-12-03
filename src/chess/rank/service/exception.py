# src/chess/rank/service/exception.py

"""
Module: chess.rank.service.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""


from chess.system import BuildFailedException, NullException, ServiceException, ValidationException

__all__ = [
    "RankServiceException",
    
    # ======================# NULL RANK_SERVICE EXCEPTIONS #======================#
    "NullRankServiceException",
    
    # ======================# RANK_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidRankServiceException",
    
    # ======================# RANK_SERVICE BUILD EXCEPTIONS #======================#
    "RankServiceBuildFailedException",
]


class RankServiceException(ServiceException):
    """
    Super class of exceptions raised by RankCertifier objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "RankCertifier raised an exception."


# ======================# NULL RANK_SERVICE EXCEPTIONS #======================#
class NullRankServiceException(RankServiceException, NullException):
    """Raised if an entity, method, or operation requires RankCertifier but gets null instead."""
    ERROR_CODE = "NULL_RANK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "RankCertifier cannot be null."


# ======================# RANK_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidRankServiceException(RankServiceException, ValidationException):
    """Catchall Exception for when RankServiceValidator fails candidates on a Piece-RankCertifier relationship test."""
    ERROR_CODE = "INVALID_RANK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "RankCertifier validation failed."


# ======================# RANK_SERVICE BUILD EXCEPTIONS #======================#
class RankServiceBuildFailedException(RankServiceException, BuildFailedException):
    """Catchall Exception for RankServiceBuilder when it encounters an error building a Rank."""
    ERROR_CODE = "RANK_SERVICE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "RankCertifier build failed."