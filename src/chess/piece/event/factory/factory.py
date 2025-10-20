# src/chess/piece/event/transaction.py

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
from chess.piece.event.validation import OldTravelActorValidator
from chess.rank import King
from chess.square import Square, SquareValidator
from chess.system import Builder, LoggingLevelRouter, BuildResult
from chess.board import Board, BoardPieceSearch, BoardSquareSearch, BoardSearchContext




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

  @classmethod
  @LoggingLevelRouter.monitor
  def create(cls, actor: Piece, destination_square: Square, board: Board) -> BuildResult[TravelEvent]:
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
      actor_validation = OldTravelActorValidator.validate(actor_candidate=actor, execution_resource=board)
      if actor_validation.is_failure():
        return BuildResult(execption=actor_validation.exception)
      actor_square = actor_validation.payload

      #========= Resource Sanity Checks =========#
      square_validation = SquareValidator.validate(destination_square)
      if square_validation.is_failure():
        return BuildResult(exception=square_validation.exception)

      square_search = BoardSquareSearch.search(
        board=board,
        search_context=BoardSearchContext(id=destination_square.id))
      if square_search.is_empty():
        return BuildResult(exception=TravelEventResourceNotFoundException(
           f"{method}: {TravelEventResourceNotFoundException.DEFAULT_MESSAGE}"
        ))

      if square_search.is_failure():
        return BuildResult(exception=square_search.exception)

      #========= Actor's Square Sanity Checks and  =========#
      actor_square_search = BoardSquareSearch.search(
        board=board,
        search_context=BoardSearchContext(coord=actor.current_position)
      )

      if actor_square_search.is_empty():
        return BuildResult(exception=EventActorSquareNotFoundException(
          f"{method}: {EventActorSquareNotFoundException.DEFAULT_MESSAGE}"
        ))

      if actor_square_search.is_failure():
        return BuildResult(exception=actor_square_search.exception)

      actor_square = actor_square_search.payload[0]

      if actor_square == destination_square:
        return BuildResult(exception=AutoTravelPieceException(
          f"{method}: {AutoTravelPieceException.DEFAULT_MESSAGE}"
        ))

      destination_occupant = destination_square.occupant

      if destination_occupant is None:
        return BuildResult(payload=OccupationEventValidator(
          actor=actor,
          actor_square=actor_square,
          destination_square=destination_square,
          execution_environment=board
        ))

      if not actor.is_enemy(destination_occupant) or isinstance(destination_occupant.rank, King):
        return BuildResult(payload=EncounterEvent(
          actor=actor,
          subject=destination_occupant,
          subject_square=destination_square,
          execution_environment=board
        ))

      return BuildResult(payload=AttackEvent(
        actor=actor,
        actor_square=actor_square,
        enemy_combatant=destination_occupant,
        destination_square=destination_square,
        execution_environment=board
      ))
    except Exception as e:
        return BuildResult(exception=e)



