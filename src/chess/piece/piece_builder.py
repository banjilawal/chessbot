from enum import Enum

from chess.rank import Rank, King, RankValidator
from assurance import ThrowHelper

from chess.exception import RelationshipException
from chess.common import IdValidator, NameValidator, BuildResult
from chess.piece import Piece, KingPiece, CombatantPiece, PieceBuilderException
from chess.team import Team, TeamValidator, InvalidTeamAssignmentException
from chess.team.exception import RankQuotaFullException


class PieceBuilder(Enum):
    """
    Builder class responsible for safely constructing `Piece` instances.
    
    `PieceBuilder` ensures that `Piece` objects are always created successfully by
    performing comprehensive validation checks during construction. This separates
    the responsibility of building from validating - `PieceBuilder` focuses on
    creation while `PieceValidator` is used for validating existing `Piece` instances
    that are passed around the system.
    
    The builder runs through all validation checks individually to guarantee that
    any `Piece` instance it produces meets all required specifications before
    construction completes.
    
    Usage:
        ```python
        # Safe piece creation with validation
        build_outcome = PieceBuilder.build(piece_id=id_emitter.piece_id, name="WN2", rank=Knight(), team=white_team)
        if not build_outcome.is_success():
            raise build_outcome.exception
        piece = build_outcome.payload
        ```
    
    See Also:
        `PieceValidator`: Used for validating existing `Piece` instances
        `Piece`: The data structure being constructed
        `BuildResult`: Return type containing the built `Piece` or error information
    """

    @staticmethod
    def build(piece_id: int, name: str, rank: Rank, team: Team) -> BuildResult[Piece]:
        """
        Constructs a new `Piece` instance with comprehensive validation.

        Performs individual validation checks on each component to ensure the 
        resulting `Piece` meets all specifications. The method validates bounds, 
        null checks, and uses `PieceValidator` for final instance validation 
        before returning a successfully constructed `Piece`.

        This method guarantees that if a `BuildResult` with a successful status 
        is returned, the contained `Piece` is valid and ready for use.

        Args:
           `piece_id`(`int`): The unique id for the piece. Must pass `IdValidator` checks.
            `name`(`Name`): The human or cybernetic moving pieces in `Piece.roster`. The name
                must not be None and must pass `NameValidator` checks.must pass `NameValidator` checks.
            `rank`(`Rank`): The rank which determines how the piece moves and its capture value.
             `team`(`Team`): Specifies if the piece is white or black.

        Returns:
            BuildResult[Piece]: A `BuildResult` containing either:
                - On success: A valid `Piece` instance in the payload
                - On failure: Error information and exception details

        Raises:
           PieceBuilderException: Wraps any underlying validation failures
           that occur during the construction process. This includes:
            `IdValidationException`: if `piece_id` fails validation checks
            `NameValidationException`: if `name` fails validation checks
            `RankValidationException`: if `rank` fails validation checks
            `TeamValidationException`: if `team` fails validation checks
            `InvalidTeamAssignmentException`: If `piece.team` is different from `team` parameter
            `RankQuotaFullException`: If the `team` has no empty slots for the `piece.rank`
            `RankQuotaFullException`: If `piece.team` is equal to `team` parameter
                but `team.roster` still does not have the piece


        Note:
            The builder performs validation at construction time, while 
            `PieceValidator` is used for validating `Piece` instances that 
            are passed around after creation. 
            This separation of concerns makes the validation responsibilities clearer.

        Example:
            ```python
            # Valid piece creation
            build_outcome = PieceBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
            ```
        """
        method = "PieceBuilder.build"

        try:
            id_validation = IdValidator.validate(piece_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, id_validation)

            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, name_validation)

            rank_validation = RankValidator.validate(rank)
            if not rank_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, rank_validation)

            team_validation = TeamValidator.validate(team)
            if not team_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, team_validation)

            piece = None
            if isinstance(rank, King):
                piece = KingPiece(piece_id=piece_id, name=name, rank=rank, team=team)
            piece = CombatantPiece(piece_id=piece_id, name=name, rank=rank, team=team)

            if not piece.team == team:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    InvalidTeamAssignmentException(InvalidTeamAssignmentException.DEFAULT_MESSAGE)
                )
            if piece.team == team and team.rank_tally(piece.rank) >= piece.rank.quota:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    RankQuotaFullException(RankQuotaFullException.DEFAULT_MESSAGE)
                )
                
            if not piece.team == team and team.rank_tally(piece.rank) < piece.rank.quota:
                team.add_to_roster(piece)

            if piece not in team.roster:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    RelationshipException(RelationshipException.DEFAULT_MESSAGE)
                )

            return BuildResult(payload=piece)
        except Exception as e:
            raise PieceBuilderException(f"{method}: {PieceBuilderException}")


# def main():
#     build_outcome = PieceBuilder.build()
#     if build_outcome.is_success():
#         piece = build_outcome.payload
#         print(f"Successfully built piece: {piece}")
#     else:
#         print(f"Failed to build piece: {build_outcome.exception}")
#     #
#     build_outcome = PieceBuilder.build(1, None)
#     if build_outcome.is_success():
#         piece = build_outcome.payload
#         print(f"Successfully built piece: {piece}")
#     else:
#         print(f"Failed to build piece: {build_outcome.exception}")
#
# if __name__ == "__main__":
#     main()