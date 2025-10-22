# src/chess/piece/travel/context.py

"""
Module: chess.piece.travel.context
Author: Banji Lawal
Created: 2025-10-06

# SECTION 1 - Purpose:
This module provides a satisfaction of the `ChessBot` performance requirement.

# SECTION 2 - Scope:
The module covers old_search service providers, data owners and information requesters.

# SECTION 3 - Limitations:
  1. The module does not provide any attributes or actionable code. Properties in a
     data owner's collection determine what is in the SearchContext

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. separating entity responsibilities into from implementation details.
  2. Loose coupling of modules while maintaining a unified, consistent interface for high cohesion among components
    that have no direct relationship with each other.
  3. A consistent interface and aids discoverability, understanding and simplicity.

# SECTION 5 - Features Supporting Requirements:
1. Simplicity


# SECTION G - Feature Delivery Mechanism:
The module provides a data structure for passing old_search for filtering the data owner's collection.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `Context`

* From Python `abc` Library:
    `ABC`

# SECTION 8 - Contains:
1. `ExecutionContext`
"""

# src/chess/piece/travel/square.py

"""
Module: `chess.piece.travel.roster`
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0

Provides:
Concrete subclass of `ExecutionContext`.

Contains:
 * `TravelContext`
"""

from typing import Optional

from chess.board import Board
from chess.piece import Piece
from chess.system import ExecutionContext


class TravelContext(ExecutionContext):
  """
  # ROLE: Encapsulation

  # RESPONSIBILITIES:
  1. Simplify the number of parameters and their possible combinations passed to a old_search method.

  # PROVIDES:
  1. A dictionary of options and specifications of what the old_search service returns.

  # ATTRIBUTES:
    * See `Context` superclass for attributes.
  """
  """
  Additional dependencies an `TravelEvent` passes to an
  `TravelEventFactory` apart from the `actor_candidate` and `resource`.

  Attributes:
    `_board (`Board)`:
    `_destination_occupant (`Piece`):
  """

  _board: Optional[Board]
  _destination_occupant: Optional[Piece]

  # # Usage:
  # roster = OcContext(board_validator=board_validator, teams=all_teams)
  # outcome = executor.execute_directive(directive, roster.to_dict())

  def __init__(self, destination_occupant: Optional[Piece]=None, board: Optional[Board]=None):
    super().__init__()
    self._board = board
    self._destination_occupant = destination_occupant

  @property
  def board(self) -> Optional[Board]:
    return self._board

  @property
  def destination_occupant(self) -> Optional[Piece]:
    return self._destination_occupant
