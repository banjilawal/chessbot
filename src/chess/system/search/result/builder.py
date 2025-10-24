# chess/square/old_occupation_validator.py

"""
Module: `chess.square.validation`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

SCOPE:
-----
This module is strictly limited to constructing `SearchResult` instances safely.

**It does not** contain logic or rules for creating `TravelEvent` or
`TravelEventFactory`. Those are handled by `OccupationEventBuilder` before
execution,`TravelEventFactory` during execution.

**It does not** ensure existing `SearchResult` instances are valid. That is done
by the `SearchResultValidator`.

THEME:
-----
**Integrity, Consistency, Validation.** The module's design centers on team separating
complexities of the build process into team utility from the `SearchResult` constructor.

PURPOSE:
-------
To execute validated `TravelEvent` directives by orchestrating the necessary
state changes across the board_validator, searchResults, and teams. It serves as the **engine
layer responsible for persistent state modification** based on accepted moves.

DEPENDENCIES:
------------
This module requires components from various sub-systems:
* `chess.rank`: Movement strategy (`Rank`)
* `chess.square`: Location data structure (`Square`)
* `chess.old_search`: Board lookup utilities (`BoardSearch`)
* `chess.searchResult`: SearchResult subtypes (`KingSearchResult`, `CombatantSearchResult`, etc.)
* `chess.team`: Roster management, rollback_exception handling
* `chess.notification`: Base notification and roster types

CONTAINS:
--------
 * `SearchResultBuilder`: The validation of `SearchResult` instances.
"""

from typing import TypeVar, Generic

from chess.system import Builder, BuildResult, SearchResult, LoggingLevelRouter, SearchResultBuildFailedException

T = TypeVar('T')

class SearchResultBuilder(Builder[SearchResult[Generic[T]]]):
  """
  Responsible for safely constructing `Square` instances.
  """


  @classmethod
  @LoggingLevelRouter.monitor
  def build(cls, payload: T, exception: Exception) -> BuildResult[SearchResult]:
    """
    Constructs team new `Square` that works correctly.

    Args:
      `name`(`str`): Must pass `NameValidator` checks.
      `rank`(`Rank`): The `rank` which determines how the searchResult moves and its capture value.
      `team`(`Team`): Specifies if the `searchResult` is white or black.

    Returns:
    BuildResult[SearchResult]: A `BuildResult` containing either:
      - On success: A valid `SearchResult` instance in the payload
      - On failure: Error information and error details

    Raises:
    `SquareBuildFailedException`: Wraps any exceptions raised build. These are:
      * `InvalidNameException`: if `name` fails validate checks
      * `InvalidRankException`: if `rank` fails validate checks
      * `InvalidTeamException`: if `team` fails validate checks
      * `InvalidTeamAssignmentException`: If `searchResult.team` is different from `team` parameter
      * `FullRankQuotaException`: If the `team` has no empty slots for the `searchResult.rank`
      * `FullRankQuotaException`: If `searchResult.team` is equal to `team` parameter but `team.roster` still does
        not have the searchResult
    """
    method = "TransactionResultBuilder.build"

    try:

      if payload is not None and exception is not None:
        return BuildResult(exception=SearchResultBuildFailedException(
          f"{method}: SearchResultBuildFailed. Either payload or rollback_exception can be null. Not both."
          )
        )

      return BuildResult(SearchResult(payload=payload, exception=exception))

    except Exception as e:
      return SearchResultBuildFailedException(f"{method}: {e}")




# def main():
#   build_outcome = SearchResultBuilder.build()
#   if build_outcome.is_success():
#     searchResult = build_outcome.payload
#     print(f"Successfully built searchResult: {searchResult}")
#   else:
#     print(f"Failed to build searchResult: {build_outcome.err}")
#   #
#   build_outcome = SearchResultBuilder.build(1, None)
#   if build_outcome.is_success():
#     searchResult = build_outcome.payload
#     print(f"Successfully built searchResult: {searchResult}")
#   else:
#     print(f"Failed to build searchResult: {build_outcome.err}")
#
# if __name__ == "__main__":
#   main()