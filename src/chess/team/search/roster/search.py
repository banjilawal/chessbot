# src/chess/piece/event/transaction
"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Highlight the core feature (thread-safety)
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:

# CONTAINS:
 * ``
"""


from typing import List

from chess.piece import Piece
from chess.team import Team, PieceSearchContext, TeamValidator
from chess.system import Search, SearchResult
from chess.team.search import PieceSearchContextValidator


class TeamRosterSearch(Search):

  @classmethod
  def search(cls, team: Team, search_context: PieceSearchContext) -> SearchResult[List[Piece]]:
      method = "TeamRosterSearch.search"

      team_validation = TeamValidator.validate(team)
      if not team_validation.is_success():
        return SearchResult(exception=team_validation.exception)

      search_context_validation = PieceSearchContextValidator.validate(search_context)
      if not search_context_validation.is_success():
        return SearchResult(exception=search_context_validation.exception)


      if search_context.name is not None:
        return TeamRosterSearch._name_search(team=team, name=search_context.name)

      if search_context.rank is not None:
        return TeamRosterSearch._rank_filter(team=team, rank=search_context.rank)

      if search_context.ransom is not None:
        return TeamRosterSearch._ransom_filter(team=team, ransom=search_context.ransom)

      if search_context.piece_id is not None:
        return TeamRosterSearch._id_search(team=team, piece_id=search_context.piece_id)

      if search_context.roster_number is not None:
        return TeamRosterSearch. _roster_number_search(team=team, roster_number=search_context.roster_number)

  @classmethod
  def _name_search(cls, team: Team, name: str) -> SearchResult[List[Piece]]:
      """
      Does not guarantee uniqueness returns the first item which matches the given name.
      """
      method = "TeamRosterSearch._name_search"

      piece = next((member for member in team.roster if member.name.upper() == name.upper()), None)
      if piece is not None:
          return SearchResult(payload=List[piece])

      # returns empty search result if no match ws found
      return SearchResult()

  @classmethod
  def _rank_filter(cls, team: Team, rank: Rank) -> SearchResult[List[Piece]]:
      matches = [member for member in team.roster if member.rank == rank]
      return SearchResult(payload=matches)

  @classmethod
  def _ransom_filter(cls, team: Team, ransom: int) -> SearchResult[List[Piece]]:
      matches = [member for member in team.roster if member.rank.ransom == ransom]
      return SearchResult(payload=matches)

  @classmethod
  def _id_search(cls, team: Team, piece_id: int) -> SearchResult[List[Piece]]:
      """
      IDs should be unique. Faster search would return the first match. An easy
      integrity check finds all the items with the same id. If there is more than
      one raise a `DuplicateUniqueIdException`.

      Performance Impact:
      The set of roster will never exceed 15 so this is not going to be a really
      burdensome search.
      """
      method = "TeamRosterSearch._id_search"

      piece = next((member for member in team.roster if member.id == piece_id), None)
      if piece is not None:
          return SearchResult(payload=List[piece])

      # returns empty search result if no match ws found
      return SearchResult()

  @classmethod
  def _roster_number_search(cls, team: Team, roster_number: int) -> SearchResult[List[Piece]]:
      """
      Does not guarantee uniqueness returns the first item which matches the given id.
      """
      method = "TeamRosterSearch._roster_number_search"

      piece = next((member for member in team.roster if member.roster_number == roster_number), None)
      if piece is not None:
          return SearchResult(payload=List[piece])

      # returns empty search result if no match ws found
      return SearchResult()