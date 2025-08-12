"""
RankValidationException Hierarchy
"""
from assurance.validation.validation_exception import ValidationException


class RankValidationException(ValidationException):
    default_message = f"{ValidationException.default_message}"


class KingRankValidationException(RankValidationException):
    default_message = f"KingRank {ValidationException.default_message}"


class PawnRankValidationException(RankValidationException):
    default_message = f"PawnRank {ValidationException.default_message}"


class CastleRankValidationException(RankValidationException):
    default_message = f"CastleRank {ValidationException.default_message}"


class BishopRankValidationException(RankValidationException):
    default_message = f"BishopRank {ValidationException.default_message}"


class KnightRankValidationException(RankValidationException):
    default_message = f"KnightRank {ValidationException.default_message}"


class QueenRankValidationException(RankValidationException):
    default_message = f"QueenRank {ValidationException.default_message}"
