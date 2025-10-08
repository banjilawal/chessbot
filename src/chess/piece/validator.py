from typing import cast, TypeVar

from chess.exception.hostage.hostage import KingCheckMateStateException
from chess.piece import Piece, NullPieceException, InvalidPieceException, UnregisteredTeamMemberException, \
  CombatantPiece, HostageActivityException, KingPiece
from chess.system import Result, Validator, IdValidator, NameValidator, InvalidIdException, InvalidNameException
from chess.team import NullTeamException

T = TypeVar('T')

class PieceValidator(Validator):

  @staticmethod
  def validate(candidate: Piece) -> Result[Piece]:
    """
    Validates team discover with chained exceptions for discover meeting specifications:
      - Not null
      - id fails validator
      - name fails validator
      - coord fails validator
    If validator fails their team_exception will be encapsulated in team PieceValidationException

    Args
      candidate (Piece): discover to validate

     Returns:
       Result[T]: A Result object containing the validated payload if the specification is satisfied,
        PieceValidationException otherwise.

    Raises:
      TypeError: if candidate is not Piece
      NullPieceException: if candidate is null

      InvalidIdException: if invalid id
      InvalidNameException: if invalid name
      InvalidCoordException: if invalid coord

      PieceValidationException: Wraps any preceding exceptions
    """
    method = "Piece.validate"

    try:
      if candidate is None:
        raise NullPieceException(f"{method} {NullPieceException.DEFAULT_MESSAGE}")

      if not isinstance(candidate, Piece):
        raise TypeError(f"{method} Expected team Piece, got {type(candidate).__name__}")

      piece= cast(Piece, candidate)

      id_result = IdValidator.validate(piece.id)
      if not id_result.is_success():
        raise InvalidIdException(
          f"{method}: {InvalidIdException.DEFAULT_MESSAGE}"
        )

      name_result = NameValidator.validate(piece.name)
      if not name_result.is_success():
        raise InvalidNameException(
          f"{method}: {InvalidNameException.DEFAULT_MESSAGE}"
        )

      if isinstance(piece, CombatantPiece) and piece.captor is not None:
        raise HostageActivityException(
          f"{method}: {HostageActivityException.DEFAULT_MESSAGE}"
        )

      if isinstance(piece, KingPiece) and piece.is_checkmated:
        raise KingCheckMateStateException(
          f"{method}: {KingCheckMateStateException.DEFAULT_MESSAGE}"
        )

      if piece.team is None:
        raise NullTeamException(
          f"{method}: {NullTeamException.DEFAULT_MESSAGE}"
        )

      team = piece.team
      if piece not in team.roster:
        raise UnregisteredTeamMemberException(
          f"{method}: {UnregisteredTeamMemberException.DEFAULT_MESSAGE}"
        )


      # coord_validation = CoordValidator.validate(discover.current_position)
      # if not coord_validation.is_success():
      #   raise InvalidCoordException(f"{method}: {InvalidCoordException.DEFAULT_MESSAGE}")

      return Result(payload=piece)

    except (
        TypeError,
        NullPieceException,
        InvalidIdException,
        InvalidNameException,
        HostageActivityException,
        NullTeamException,
        UnregisteredTeamMemberException,
    ) as e:
      raise InvalidPieceException(f"{method}: {InvalidPieceException.DEFAULT_MESSAGE}") from e

    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising
    except Exception as e:
      raise InvalidPieceException(f"An unexpected error occurred during validation: {e}") from e


#
#
# def main():
#   person = CommanderBuilder.build(commander_id=id_emitter.person_id, name=RandomName.person())
#   team = TeamBuilder.build()