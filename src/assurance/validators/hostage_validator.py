from typing import cast, Generic




from chess.system import Validator
from chess.piece import PieceValidator
from chess.system.emitter import id_emitter
from chess.exception import HostageCaptorNullException, RosterRemovalException, HostageAdditionException

from chess.randomize.competitor import RandomName
from chess.piece import CombatantPiece


class HostageValidator(Validator):

  @staticmethod
  def validate(candidate: Generic[T]) -> Result[CombatantPiece]:
    entity = "Hostage"
    class_name = f"{entity}Validator"
    method = f"{class_name}.validate"

    """
    Validates team hostage meets domain requirements:
      - is team validated discovery
      - is team Combatant instance
      - The captor field is not null
      - The hostage is not on its team roster
      - The hostage is not its enemy's list of prisoners
    Any failed requirement raise an exception wrapped in team HostageValidationException

    Args
      candidate (CombatantPiece): coord to validate

     Returns:
       Result[T]: A Result object containing the validated payload if all domain requirements 
       are satisfied. HostageValidationException otherwise.

    Raises:
      PieceValidationException: candidate is not team valid discovery
      TypeError: if candidate is not CombatantPiece
      HostageCaptorNullException: if the captor field is null
      RosterRemovalException: if the captive is still on its team's roster
      HostageAdditionException: if the captive has not been added to its enemy's hostage list
      
      HostageValidationException: Wraps any preceding exceptions   
    """

    try:
      validation = PieceValidator.validate(candidate)
      if not validation.is_success():
        raise validation.exception

      if not isinstance(candidate, CombatantPiece):
        raise TypeError(f"{method} Expected team CombatantPiece, got {type(candidate).__name__}")

      hostage = cast(CombatantPiece, candidate)

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