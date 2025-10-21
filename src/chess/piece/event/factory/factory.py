# src/chess/piece/event/old_transaction.py

"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
# THEME:
# PURPOSE:
# DEPENDENCIES:
# CONTAINS:
 * `TravelEventFactory`
"""


from chess.square import Square
from chess.system import LoggingLevelRouter, BuildResult
from chess.board import Board, BoardSquareSearch, BoardSearchContext, SearchByCoordInvariantBreachException
from chess.piece import (
  Piece, KingPiece, CombatantPiece, AttackEvent, OccupationEvent, EncounterEvent, TravelEvent,
  ActorBindingBoardValidator, ResourceBindingBoardValidator, ActorAlreadyAtDestinationException
)


class TravelEventFactory:
  """
  Implements the `OccupationExecutor` class, which handles executing event
  directives in the chess engine. This includes moving pieces, capturing enemies,
  and coordinating rollback logic in case of inconsistencies or failed operations.

  Attributes:
    * `OccupationExecutor:` Main class responsible for executing event directives.
    * `_attack_enemy`: Static method for processing attacks on enemy pieces.
    * `_run_scan`: Static method for handling discoveries on occupied squares.
    * `_switch_squares`: Static method the transferring team piece to team different `Square`.
  """

  @staticmethod
  @LoggingLevelRouter.monitor
  def create(actor: Piece, destination_square: Square, board: Board) -> BuildResult[TravelEvent]:
    """
    # ACTION:
    Verify the `candidate` is a valid ID. The Application requires
    1. Candidate is not null.
    2. Is a positive integer.

    # PARAMETERS:
        * `candidate` (`int`): the id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `exception` (`Exception`) - An exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """
    method = "TravelEventFactory.execute"

    try:
      actor_binding_validation = ActorBindingBoardValidator.validate((actor, board))
      if actor_binding_validation.is_failure():
        return BuildResult(exception=actor_binding_validation.exception)

      resource_binding_validation = ResourceBindingBoardValidator.validate((destination_square, board))
      if resource_binding_validation.is_failure():
        return BuildResult(exception=resource_binding_validation.exception)

      if actor.current_position == destination_square.coord:
        return BuildResult(exception=ActorAlreadyAtDestinationException
        (f"{method}: {ActorAlreadyAtDestinationException.DEFAULT_MESSAGE}"))

      actor_square_search = BoardSquareSearch.search(
        board=board,
        search_context=BoardSearchContext(coord=actor.current_position)
      )

      if actor_square_search.is_empty():
        return BuildResult(exception=SearchByCoordInvariantBreachException(
          f"{method}: {SearchByCoordInvariantBreachException.DEFAULT_MESSAGE}"
        ))

      if actor_square_search.is_failure():
        return BuildResult(exception=actor_square_search.exception)

      actor_square = actor_square_search.payload[0]
      destination_occupant = destination_square.occupant

      if destination_occupant is None:
        return BuildResult(payload=OccupationEvent(
          actor=actor,
          actor_square=actor_square,
          destination_square=destination_square,
          execution_environment=board
        ))

      if not actor.is_enemy(destination_occupant) or isinstance(destination_occupant, KingPiece):
        return BuildResult(payload=EncounterEvent(
          actor=actor,
          subject=destination_occupant,
          subject_square=destination_square,
          execution_environment=board
        ))

      if actor.is_enemy(destination_occupant) and isinstance(destination_occupant, CombatantPiece):
      return BuildResult(payload=AttackEvent(
        actor=actor,
        actor_square=actor_square,
        enemy_combatant=destination_occupant,
        destination_square=destination_square,
        execution_environment=board
      ))
    except Exception as e:
        return BuildResult(exception=e)



