from typing import cast, Generic




from chess.common import Validator
from chess.piece import  PieceValidator
from chess.common.emitter import id_emitter
from chess.exception import HostageCaptorNullException, RosterRemovalException, HostageAdditionException

from chess.randomize.competitor import RandomName
from chess.piece import CombatantPiece


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
        Any failed requirement raise an team_exception wrapped in a HostageValidationException

        Args
            t (CombatantPiece): coord to validate

         Returns:
             Result[T]: A Result object containing the validated payload if all domain requirements 
             are satisfied. HostageValidationException otherwise.

        Raises:
            PieceValidationException: t is not a valid piece
            TypeError: if t is not CombatantPiece
            HostageCaptorNullException: if the captor field is null
            RosterRemovalException: if the captive is still on its team's roster
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

            side = hostage.team
            if hostage in side.roster:
                raise RosterRemovalException(f"{method}: {RosterRemovalException.DEFAULT_MESSAGE}")

            enemy_side = hostage.captor.team
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
    person = CommanderBuilder.build(commander_id=id_emitter.person_id, name=RandomName.person())
    side = TeamBuilder.build()