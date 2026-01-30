
from chess.rank import RankService
from chess.square import SquareContext
from chess.formation import FormationKey, FormationService
from chess.system import (
    BuildResult, Builder, IdentityService, InvariantBreachException, LoggingLevelRouter, id_emitter
)
from chess.team import Team, TeamService
from chess.token import TokenManifest, TokenManifestBuildFailedException


class TokenManifestBuilder(Builder[TokenManifest]):
    
    @LoggingLevelRouter.monitor
    def build(
            self,
            team: Team,
            roster_number: int,
            token_designation: str,
            id: int = id_emitter.piece_id,
            team_service: TeamService = TeamService(),
            rank_service: RankService = RankService(),
            identity_service: IdentityService = IdentityService(),
            formation_service: FormationService = FormationService(),
    ) -> BuildResult[TokenManifest]:
        """
        # ACTION:
            1.  If the team fails validation send the exception chain in the SearchResult.
            2.  Find each formation's team item by their designation ane put them in a list.
            3.  if any search fails return the exception instead of the list.
        # PARAMETERS:
            *   team (Team)
            *   team_service (TeamService)
         # RETURNS:
            *   SearchResult[List[[Square]] containing either:
                    - On error: Exception , payload null
                    - On finding a match: List[Square] in the payload.
                    - On no matches found: Exception null, payload null
        # RAISES:
            *   TypeError
            *   NullTeamContextException
            *   ZeroTeamContextFlagsException
            *   ExcessiveTeamContextFlagsException
            *   TeamContextValidationFailedException
            *   TeamContextValidationRouteException
        """
        method = "FormationService.get_team_square"
        
        # Handle the case that either roster_number or designation are not valid.
        identity_service = identity_service.validate_identity(
            id_candidate=roster_number,
            name_candidate=token_designation,
        )
        if identity_service.is_failure:
            # Return the exception chain on failure.
            if identity_service.is_failure:
                return BuildResult.failure(
                    TokenManifestBuildFailedException(
                        message=f"{method}: {TokenManifestBuildFailedException.DEFAULT_MESSAGE}",
                        ex=identity_service.exception
                    )
                )
        # Handle the case that the team does not get certified safe.
        team_validation = team_service.validator.validate(candidate=team)
        # Return the exception chain on failure.
        if team_validation.is_failure:
            return BuildResult.failure(
                TokenManifestBuildFailedException(
                    message=f"{method}: {TokenManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=team_validation.exception
                )
            )
        formation_search_result = formation_service.lookup_formation(
            super_key=FormationKey(designation=token_designation)
        )
        # Handle the case that the search fails.
        if formation_search_result.is_failure:
            # Return the exception chain on failure.
            if team_validation.is_failure:
                return BuildResult.failure(
                    TokenManifestBuildFailedException(
                        message=f"{method}: {TokenManifestBuildFailedException.DEFAULT_MESSAGE}",
                        ex=formation_search_result.exception
                    )
                )
        formation = formation_search_result.payload[0]
        square_search_result = team.board.squares.search_squares(
            context=SquareContext(name=formation.square_name)
        )
        # Handle the case that the square search fails.
        if square_search_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenManifestBuildFailedException(
                    message=f"{method}: {TokenManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=square_search_result.exception
                )
            )
        # Handle the case that no square was found.
        if square_search_result.is_empty:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenManifestBuildFailedException(
                    message=f"{method}: {TokenManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=InvariantBreachException(f"{method}: Square {formation.square_name} not found.")
                )
            )
        # Handle the case that the rank is not built.
        build_rank_result = rank_service.builder.build(formation.persona)
        if build_rank_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenManifestBuildFailedException(
                    message=f"{method}: {TokenManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=build_rank_result.exception
                )
            )
        # Handle the case that either roster_number or designation are not valid.
        return BuildResult.success(
            payload=TokenManifest(
                id=id,
                owner=team,
                roster_number=roster_number,
                designation=token_designation,
                rank=build_rank_result.payload,
                opening_square=square_search_result.payload[0],
            )
        )
            