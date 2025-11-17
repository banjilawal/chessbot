# chess/square/old_occupation_validator.py

"""
Module: chess.square.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

SCOPE:
-----
This module is strictly limited to constructing Piece instances safely.

**It does not** contain logic or rules for creating TravelEvent or
TravelEventFactory. Those are handled by OccupationEventBuilder before
execution,TravelEventFactory during execution.

**It does not** ensure existing Piece instances are valid. That is done
by the PieceValidator.

THEME:
-----
**Integrity, Consistency, Validation.** The module's design centers on team_name separating
complexities of the build process into team_name utility from the Piece constructor.

PURPOSE:
-------
To execute validated TravelEvent directives by orchestrating the necessary
state changes across the board_validator, pieces, and teams. It serves as the **engine
layer responsible for persistent state modification** based on accepted moves.

DEPENDENCIES:
------------
This module requires components from various sub-systems:
* chess.bounds: Movement strategy (Rank)
* chess.square: Location service structure (Square)
* chess.old_search: Board lookup utilities (BoardSearch)
* chess.owner: Piece subtypes (KingPiece, CombatantPiece, etc.)
* chess.team_name: Roster management, rollback_exception handling
* chess.notification: Base notification and roster types

CONTAINS:
--------
 * PieceFactory: The validator of Piece instances.
"""
from chess.pawn import PawnPiece
from chess.rank.service import RankService
from chess.system import (
  Builder, BuildResult, IdValidator, IdentityService, NameValidator, LoggingLevelRouter,
  SearchContext, ValidationResult
)
from chess.piece import (
  Piece, AttackBuildFailedException, KingPiece, CombatantPiece, PieceBuildFailedException,
  UnregisteredTeamMemberException
)
from chess.rank import Pawn, Rank, RankValidator, King
from chess.team import (
  Team, TeamService, TeamValidator, TeamSearch, PieceCollectionCategory, FullRankQuotaException,
  ConflictingTeamAssignmentException
)


class PieceFactory(Builder[Piece]):
  """
  Responsible for safely constructing Square instances.
  """

  @classmethod
  @LoggingLevelRouter.monitor
  def build(
          cls,
          id: int,
          name: str,
          rank: Rank,
          team: Team,
          rank_service: RankService = RankService(),
          team_service: TeamService = TeamService(),
          identity_service: IdentityService = IdentityService(),
  ) -> BuildResult[Piece]:
    """
    Constructs team_name new Square that works correctly.

    Args:
      visitor_name(str): Must pass NameValidator checks.
      bounds(Rank): The bounds which determines how the owner moves and its capture value.
      team_name(Team): Specifies if the owner is white or black.

    Returns:
    BuildResult[Piece]: A BuildResult containing either:
      - On success: A valid Piece instance in the payload
      - On failure: Error information and error details

    Raises:
    SquareBuildFailedException: Wraps any exceptions raised build. These are:
      * InvalidNameException: if visitor_name fails validate checks
      * InvalidRankException: if bounds fails validate checks
      * InvalidTeamException: if team_name fails validate checks
      * InvalidTeamAssignmentException: If owner.team_name is different from team_name parameter
      * FullRankQuotaException: If the team_name has no empty slots for the owner.bounds
      * FullRankQuotaException: If owner.team_name is equal to team_name parameter but team_name.roster still does
        not have the owner
    """
    method = "PieceFactory.build"

    try:
      
      piece = None
      if isinstance(rank, King):
        return cls.build_king_
      
      piece = Piece(id=id, name=name, rank=rank, team=team)
      if piece not in team.roster:
        team.roster.append(piece)
      
      return BuildResult(
        payload=Piece(
          id=id,
          name=name,
          rank=rank,
          team=team
        )
      )
      
      # id_validation = IdValidator.validate(visitor_id)
      # if not id_validation.is_success():
      #   LoggingLevelRouter.throw_if_invalid(PieceFactory, id_validation)

      name_validation = NameValidator.validate(name)
      if not name_validation.is_success():
        return BuildResult(exception=name_validation.exception)

      rank_validation = RankValidator.validate(rank)
      if not rank_validation.is_success():
        return BuildResult(exception=rank_validation.exception)

      team_validation = TeamValidator.validate(team)
      if not team_validation.is_success():
        return BuildResult(exception=team_validation.exception)

      search_result = TeamSearch.search(
        team=team,
        data_source=PieceCollectionCategory.ROSTER,
        search_context=SearchContext(rank=rank)
      )
      if not search_result.is_success():
        return BuildResult(exception=search_result.exception)

      if len(search_result.payload) >= rank.team_quota:
        return BuildResult(exception=FullRankQuotaException(
          f"{method}: FullRankQuotaException.DEFAULT_MESSAGE"
          )
        )

      piece = None
      if isinstance(rank, King):
        piece = KingPiece(name=name, rank=rank, team=team)
      else:
        piece = CombatantPiece(name=name, rank=rank, team=team)

      if not piece.team == team:
        return BuildResult(exception=ConflictingTeamAssignmentException(
          f"{method}: ConflictingTeamAssignmentException.DEFAULT_MESSAGE"
          )
        )

      if not piece.team == team:
        team.add_to_roster(piece)

      if piece not in team.roster:
        return BuildResult(exception=UnregisteredTeamMemberException(
          f"{method}: UnregisteredTeamMemberException.DEFAULT_MESSAGE"
          )
        )

      return BuildResult(payload=piece)

    except Exception as e:
      raise AttackBuildFailedException(f"{method}: {e}")
  
  @classmethod
  @LoggingLevelRouter.monitor
  def build_pawn_piece(cls, id: int, name: str, team: Team) -> BuildResult[PawnPiece]:
    """"""
    method = "PieceFactory.build_pawn_piece"
    try:
      attribute_validation = cls.validate_build_attributes(id, name, PawnPiece(), team)
      if attribute_validation.is_failure():
        return BuildResult(exception=attribute_validation.exception)
      piece = PawnPiece(id=id, name=name, rank=Pawn(), team=team)
      
      return BuildResult(
        payload=KingPiece(
          id=id,
          name=name,
          rank=King(),
          team=team
        )
      )
    
    except Exception as ex:
      return BuildResult.failure(
        PieceBuildFailedException(
          f"{method}: {PieceBuildFailedException.DEFAULT_MESSAGE}",
          ex
        )
      )
      
  @classmethod
  @LoggingLevelRouter.monitor
  def build_king_piece(cls, id: int, name: str, team: Team) -> BuildResult[KingPiece]:
    """"""
    method = "PieceFactory.build_king_piece"
    try:
      attribute_validation = cls.validate_build_attributes(id, name, King(), team)
      if attribute_validation.is_failure():
        return BuildResult(exception=attribute_validation.exception)
      piece = KingPiece(id=id, name=name, rank=King(), team=team)
      
    except Exception as ex:
      return BuildResult.failure(
        PieceBuildFailedException(
          f"{method}: {PieceBuildFailedException.DEFAULT_MESSAGE}",
          ex
        )
      )

  @classmethod
  @LoggingLevelRouter.monitor
  def validate_build_attributes(
          cls,
          id: int,
          name: str,
          rank: Rank,
          team: Team,
          rank_service: RankService = RankService(),
          team_service: TeamService = TeamService(),
          identity_service: IdentityService = IdentityService(),
  ) -> ValidationResult(int, str, Rank, Team):
    """"""
    method = "PieceFactory.validate_build_attributes"
    
    try:
      identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
      if identity_validation.is_failure():
        return BuildResult(exception=identity_validation.exception)
      
      rank_validation = rank_service.validate(candidate=rank)
      if rank_validation.is_failure():
        return BuildResult(exception=rank_validation.exception)
      
      team_validation = team_service.validate_team(candidate=team)
      if team_validation.is_failure():
        return BuildResult(exception=team_validation.exception)
      
      
      
      return ValidationResult.success((id, name, rank, team))
    except Exception as ex:
      return BuildResult(
        PieceBuildFailedException(
          f"{method}: {PieceBuildFailedException.DEFAULT_MESSAGE}",
          ex
        )
      )
  
# def main():
#   build_outcome = PieceFactory.build()
#   if build_outcome.is_success():
#     owner = build_outcome.payload
#     print(f"Successfully built owner: {owner}")
#   else:
#     print(f"Failed to build owner: {build_outcome.err}")
#   #
#   build_outcome = PieceFactory.build(1, None)
#   if build_outcome.is_success():
#     owner = build_outcome.payload
#     print(f"Successfully built owner: {owner}")
#   else:
#     print(f"Failed to build owner: {build_outcome.err}")
#
# if __name__ == "__main__":
#   main()