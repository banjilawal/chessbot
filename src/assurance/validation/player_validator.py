from typing import Optional

from assurance.validation.validatin_report import ValidationReport
from assurance.validation.validation_exception import ValidationException
from chess.player.player import Player


class PlayerNotNUllValidationFailed(ValidationException):
    default_message = "Player failed not null validation test"

class PlayerValidator:

    @staticmethod
    def is_not_null_test(player: Optional[Player]) -> ValidationReport[Player]:

        if player is None:
            return ValidationReport.send_failed_valtidation_report(
                PlayerNotNUllValidationFailed("Player failed not null validation test"))

        return ValidationReport.send_passed_validation_report(payload=player)