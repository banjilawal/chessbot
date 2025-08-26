from typing import Optional

from assurance.validation.obsolete.validation_result import ValidationResult
from assurance.exception.validation.base_validationpy import ValidationException
from chess.owner.base import Player


class PlayerNotNUllValidationFailed(ValidationException):
    DEFAULT_MESSAGE = "Player failed not null validation test"

class ObsoletePlayerValidator:

    @staticmethod
    def not_null_test(player: Optional[Player]) -> ValidationResult[Player]:

        if player is None:
            return ValidationResult.send_failed_valtidation_report(
                PlayerNotNUllValidationFailed("Player failed not null validation test"))

        return ValidationResult.send_passed_validation_report(payload=player)