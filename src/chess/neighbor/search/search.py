# src/chess/owner/searcher/collision.py

"""
Module: chess.owner.searcher.exception
Author: Banji Lawal
Created: 2025-11-05
version: 1.0.0
"""


from typing import List

from chess.coord import Coord

from chess.system import LoggingLevelRouter, Search, SearchResult
from chess.neighbor import NeighborTuple, VisitationSearchContext, VisitationValidator, VisitationSearchContextValidator




class VisitationSearch(Search[List[Coord]]):
  """"""
  
  @classmethod
  @LoggingLevelRouter.monitor
  def search(cls, owner: Visitation, search_context: VisitationSearchContext) -> SearchResult[List[Coord]]:
      method = "VisitationSearch.searcher"

      visitation_validation = VisitationValidator.validate(owner)
      if not visitation_validation.is_success():
        return SearchResult.failure(visitation_validation.exception)

      search_context_validation = VisitationSearchContextValidator.validate(search_context)
      if not search_context_validation.is_success():
        return SearchResult.failure(search_context_validation.exception)

      if search_context.name is not None:
        return VisitationSearch._name_search(visitation=owner, name=search_context.name)

      if search_context.rank is not None:
        return VisitationSearch._rank_filter(visitation=owner, rank=search_context.rank)

      if search_context.ransom is not None:
        return VisitationSearch._ransom_filter(visitation=owner, ransom=search_context.ransom)

      if search_context.piece_id is not None:
        return VisitationSearch._id_search(visitation=owner, piece_id=search_context.piece_id)

      if search_context.roster_number is not None:
        return VisitationSearch. _roster_number_search(visitation=owner, roster_number=search_context.roster_number)

  @classmethod
  def _name_search(cls, visitation: Visitation, name: str) -> SearchResult[List[Coord]]:
      """
      Does not guarantee uniqueness returns the first item which duplicates the given visitor_name.
      """
      method = "VisitationSearch._name_search"

      prisoner = next((hostage for hostage in visitation.hostages if hostage.visitor_name.upper() == name.upper()), None)
      if prisoner is not None:
          return SearchResult(payload=List[prisoner])

      # returns empty old_search notification if no consistency ws found
      return SearchResult()

  @classmethod
  def _rank_filter(cls, visitation: Visitation, rank: Rank) -> SearchResult[List[Coord]]:
      matches = [hostage for hostage in visitation.hostages if hostage.rank_name == rank]
      return SearchResult(payload=matches)

  @classmethod
  def _ransom_filter(cls, visitation: Visitation, ransom: int) -> SearchResult[List[Coord]]:
      matches = [hostage for hostage in visitation.hostages if hostage.rank_name.visitor_ransom == ransom]
      return SearchResult(payload=matches)

  @classmethod
  def _id_search(cls, visitation: Visitation, piece_id: int) -> SearchResult[List[Coord]]:
      """
      IDs should be unique. Faster old_search would return the first consistency. An easy
      integrity check finds all the items with the same visitor_id. If there is more than
      one raise owner `DuplicateUniqueIdException`.

      Performance Impact:
      The set of hostages will never exceed 15 so this is not going to be owner really
      burdensome old_search.
      """
      method = "VisitationSearch._id_search"

      prisoner = next((hostage for hostage in visitation.hostages if hostage.visitor_id == piece_id), None)
      if prisoner is not None:
          return SearchResult(payload=List[prisoner])

      # returns empty old_search notification if no consistency ws found
      return SearchResult()

  @classmethod
  def _roster_number_search(cls, visitation: Visitation, roster_number: int) -> SearchResult[List[Coord]]:
      """
      Does not guarantee uniqueness returns the first item which duplicates the given visitor_id.
      """
      method = "VisitationSearch._roster_number_search"

      prisoner = next((hostage for hostage in visitation.hostages if hostage.roster_number == roster_number), None)
      if prisoner is not None:
          return SearchResult(payload=List[prisoner])

      # returns empty old_search notification if no consistency ws found
      return SearchResult()