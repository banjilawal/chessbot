"""
RankValidationException Hierarchy
"""
from assurance.exception.validation.base_validation import ValidationException


class RankValidationException(ValidationException):
    DEFAULT_MESSAGE = f"{ValidationException.DEFAULT_MESSAGE}"


class KingRankValidationException(RankValidationException):
    DEFAULT_MESSAGE = f"KingRank {ValidationException.DEFAULT_MESSAGE}"


class PawnRankValidationException(RankValidationException):
    DEFAULT_MESSAGE = f"PawnRank {ValidationException.DEFAULT_MESSAGE}"


class CastleRankValidationException(RankValidationException):
    DEFAULT_MESSAGE = f"CastleRank {ValidationException.DEFAULT_MESSAGE}"


class BishopRankValidationException(RankValidationException):
    DEFAULT_MESSAGE = f"BishopRank {ValidationException.DEFAULT_MESSAGE}"


class KnightRankValidationException(RankValidationException):
    DEFAULT_MESSAGE = f"KnightRank {ValidationException.DEFAULT_MESSAGE}"


class QueenRankValidationException(RankValidationException):
    DEFAULT_MESSAGE = f"QueenRank {ValidationException.DEFAULT_MESSAGE}"
