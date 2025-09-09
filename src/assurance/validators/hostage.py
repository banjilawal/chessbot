from typing import cast, Generic

from assurance.exception.validation.hostage import HostageValidationException

from chess.common.result import Result
from assurance.validators.base import Validator, T
from assurance.validators.piece import PieceValidator

from chess.creator.builder.competitor import CompetitorBuilder
from chess.creator.builder.side import SideBuilder
from chess.creator.emit import id_emitter
from chess.exception.hostage import HostageCaptorNullException, RosterRemovalException, HostageAdditionException

from chess.randomize.competitor import RandomName
from chess.token.model import CombatantPiece


class HostageValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[CombatantPiece]:
        entity = "Hostage"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a hostage meets domain requirements:
            - is a validated piece
            - is a Combatant instance
            - The captor field is not null
            - The hostage is not on its team roster
            - The hostage is not its enemy's list of prisoners
        Any failed requirement raise an exception wrapped in a HostageValidationException

        Args
            t (CombatantPiece): coord to validate

         Returns:
             Result[T]: A Result object containing the validated payload if all domain requirements 
             are satisfied. HostageValidationException otherwise.

        Raises:
            PieceValidationException: t is not a valid piece
            TypeError: if t is not CombatantPiece
            HostageCaptorNullException: if the captor field is null
            RosterRemovalException: if the captive is still on its side's roster
            HostageAdditionException: if the captive has not been added to its enemy's hostage list
            
            HostageValidationException: Wraps any preceding exceptions      
        """

        try:
            validation = PieceValidator.validate(t)
            if not validation.is_success():
                raise validation.exception

            if not isinstance(t, CombatantPiece):
                raise TypeError(f"{method} Expected a CombatantPiece, got {type(t).__name__}")

            hostage = cast(CombatantPiece, t)

            if hostage.captor is None:
                raise HostageCaptorNullException(f"{method}: {HostageCaptorNullException.DEFAULT_MESSAGE}")

            side = hostage.side
            if hostage in side.roster:
                raise RosterRemovalException(f"{method}: {RosterRemovalException.DEFAULT_MESSAGE}")

            enemy_side = hostage.captor.side
            if hostage not in enemy_side.hostages:
                raise HostageAdditionException(f"{method}: {HostageAdditionException.DEFAULT_MESSAGE}")


            return Result(payload=hostage)

        except (
            TypeError,
            HostageCaptorNullException,
            RosterRemovalException,
            HostageAdditionException
        ) as e:
            raise HostageValidationException(
                f"{method}: {HostageValidationException.DEFAULT_MESSAGE}"
            ) from e



def main():
    person = CompetitorBuilder.build(competitor_id=id_emitter.person_id, name=RandomName.person())
    side = SideBuilder.build()