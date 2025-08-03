from typing import Optional

from assurance.validation.validation_result import ValidationResult
from assurance.validation.validation_exception import ValidationException
from chess.player.player import Player


class PlayerNotNUllValidationFailed(ValidationException):
    default_message = "Player failed not null validation test"

class PlayerValidator:

    @staticmethod
    def not_null_test(player: Optional[Player]) -> ValidationResult[Player]:

        if player is None:
            return ValidationResult.send_failed_valtidation_report(
                PlayerNotNUllValidationFailed("Player failed not null validation test"))

        return ValidationResult.send_passed_validation_report(payload=player)