from enum import Enum



class PieceBuilder(Enum):
    """
    Builder class responsible for safely constructing `Piece` instances.

    `PieceBuilder` ensures that `Piece` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `PieceBuilder` 
     focuses on creation while `PieceValidator` is used for validating existing `Piece` instances that are passed 
     around the system.

    The builder runs through all validation checks individually to guarantee that any `Piece` instance it produces 
    meets all required specifications before construction completes
    
    Usage:
        ```python
        # Safe piece creation with validation
        build_outcome = EncounterBuilder.build(discovery_id=id_emitter.discovery_id, name="WN2", rank=Knight(), team=white_team)
        if not build_outcome.is_success():
            raise build_outcome.exception
        piece = build_outcome.payload
        ```
    
    See Also:
        `Piece`: The data structure being constructed
        `PieceValidator`: Used for validating existing `Piece` instances
        `BuildResult`: Return type containing the built `Piece` or error information
    """

    @staticmethod
    def build(piece_id: int, name: str, rank: Rank, team: Team) -> BuildResult[Piece]:
        """
        Constructs a new `Piece` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `Piece` meets all 
        specifications. If all checks are passed, a `Piece` instance will be returned. It is not necessary to perform 
        any additional validation checks on the returned `Piece` instance. This method guarantees if a `BuildResult` 
        with a successful status is returned, the contained `Piece` is valid and ready for use.

        Args:
            `discovery_id`(`int`): The unique id for the piece. Must pass `IdValidator` checks.
            `name`(`Name`): Must pass `NameValidator` checks.
            `rank`(`Rank`): The `rank` which determines how the piece moves and its capture value.
            `team`(`Team`): Specifies if the `piece` is white or black.

        Returns:
            BuildResult[Piece]: A `BuildResult` containing either:
                - On success: A valid `Piece` instance in the payload
                - On failure: Error information and exception details

        Raises:
           PieceBuilderException: Wraps any underlying validation failures that occur during the construction process.
           This includes:
                * `InvalidIdException`: if `discovery_id` fails validation checks
                * `NameValidationException`: if `name` fails validation checks
                * `InvalidRankException`: if `rank` fails validation checks
                * `InvalidTeamException`: if `team` fails validation checks
                * `InvalidTeamAssignmentException`: If `piece.team` is different from `team` parameter
                * `FullRankQuotaException`: If the `team` has no empty slots for the `piece.rank`
                * `FullRankQuotaException`: If `piece.team` is equal to `team` parameter but `team.roster` still does
                    not have the piece

        Note:
            The builder runs through all the checks on parameters and state to guarantee only a valid `Piece` is 
            created, while `PieceValidator` is used for validating `Piece` instances that are passed around after 
            creating. This separation of concerns makes the validation and building independent of each other and
            simplifies maintenance.

        Example:
            ```python
            # Valid piece creation
            build_outcome = EncounterBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
            ```
        """
        method = "EncounterBuilder.build"

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

            if len(TeamSearch.by_rank(rank, team).payload) >= rank.quota:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    FullRankQuotaException(FullRankQuotaException.DEFAULT_MESSAGE)
                )

            piece = None
            if isinstance(rank, King):
                piece = KingPiece(piece_id=piece_id, name=name, rank=rank, team=team)
            piece = CombatantPiece(piece_id=piece_id, name=name, rank=rank, team=team)

            if not piece.team == team:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    ConflictingTeamAssignmentException(ConflictingTeamAssignmentException.DEFAULT_MESSAGE)
                )

            if not piece.team == team:
                team.add_to_roster(piece)

            if piece not in team.roster:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    UnregisteredTeamMemberException(UnregisteredTeamMemberException.DEFAULT_MESSAGE)
                )

            return BuildResult(payload=piece)
        except Exception as e:
            raise PieceBuilderException(f"{method}: {PieceBuilderException.DEFAULT_MESSAGE}")


# def main():
#     build_outcome = EncounterBuilder.build()
#     if build_outcome.is_success():
#         piece = build_outcome.payload
#         print(f"Successfully built piece: {piece}")
#     else:
#         print(f"Failed to build piece: {build_outcome.exception}")
#     #
#     build_outcome = EncounterBuilder.build(1, None)
#     if build_outcome.is_success():
#         piece = build_outcome.payload
#         print(f"Successfully built piece: {piece}")
#     else:
#         print(f"Failed to build piece: {build_outcome.exception}")
#
# if __name__ == "__main__":
#     main()